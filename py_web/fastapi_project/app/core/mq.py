import pika
import threading
import json
import logging
from app.config import settings

logger = logging.getLogger("fastapi.mq")

# 全局MQ连接和通道
mq_connection = None
mq_channel = None
mq_consumer_thread = None

def init_mq():
    """初始化MQ连接和消费者"""
    if not settings.MQ_ENABLED:
        logger.info("MQ is disabled")
        return
        
    try:
        # 创建连接凭证
        credentials = pika.PlainCredentials(
            settings.MQ_USER, 
            settings.MQ_PASSWORD
        )
        
        # 建立连接
        global mq_connection, mq_channel
        mq_connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=settings.MQ_HOST,
            port=settings.MQ_PORT,
            credentials=credentials,
            heartbeat=600
        ))
        
        # 创建通道
        mq_channel = mq_connection.channel()
        
        # 声明队列
        mq_channel.queue_declare(queue=settings.MQ_QUEUE, durable=True)
        
        logger.info("MQ initialized successfully")
        
        # 启动消费者线程
        start_consumer()
        
    except Exception as e:
        logger.error(f"Failed to initialize MQ: {str(e)}")

def start_consumer():
    """启动MQ消费者"""
    if not settings.MQ_ENABLED or not mq_channel:
        return
        
    global mq_consumer_thread
    
    def consume():
        def callback(ch, method, properties, body):
            try:
                data = json.loads(body)
                logger.info(f"Received MQ message: {data}")
                # 处理消息的业务逻辑
                ch.basic_ack(delivery_tag=method.delivery_tag)
            except Exception as e:
                logger.error(f"Error processing MQ message: {str(e)}")
                ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
        
        mq_channel.basic_qos(prefetch_count=1)
        mq_channel.basic_consume(
            queue=settings.MQ_QUEUE, 
            on_message_callback=callback
        )
        
        logger.info("MQ consumer started")
        mq_channel.start_consuming()
    
    mq_consumer_thread = threading.Thread(target=consume, daemon=True)
    mq_consumer_thread.start()

def send_message(message):
    """发送消息到MQ"""
    if not settings.MQ_ENABLED or not mq_channel:
        logger.info("MQ is disabled, message not sent")
        return False
        
    try:
        mq_channel.basic_publish(
            exchange='',
            routing_key=settings.MQ_QUEUE,
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=2,  # 消息持久化
            )
        )
        logger.info(f"Message sent to MQ: {message}")
        return True
    except Exception as e:
        logger.error(f"Failed to send message to MQ: {str(e)}")
        return False

def close_mq():
    """关闭MQ连接"""
    if mq_connection and mq_connection.is_open:
        mq_connection.close()
        logger.info("MQ connection closed")
