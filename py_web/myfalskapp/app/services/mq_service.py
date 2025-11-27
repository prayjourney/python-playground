import pika
import threading
import json
from flask import current_app
import logging

logger = logging.getLogger(__name__)

# 全局MQ连接和通道
connection = None
channel = None
consumer_thread = None

def init_mq(app):
    """初始化MQ连接"""
    if not app.config['MQ_ENABLED']:
        logger.info("MQ is disabled")
        return
        
    try:
        # 创建连接
        credentials = pika.PlainCredentials(
            app.config['MQ_USER'], 
            app.config['MQ_PASSWORD']
        )
        global connection, channel
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=app.config['MQ_HOST'],
            port=app.config['MQ_PORT'],
            credentials=credentials
        ))
        channel = connection.channel()
        
        # 声明队列
        channel.queue_declare(queue=app.config['MQ_QUEUE'], durable=True)
        
        logger.info("MQ initialized successfully")
        
        # 启动消费者线程
        start_consumer()
        
    except Exception as e:
        logger.error(f"Failed to initialize MQ: {str(e)}")

def start_consumer():
    """启动MQ消费者"""
    if not current_app.config['MQ_ENABLED']:
        return
        
    global consumer_thread
    
    def consume():
        def callback(ch, method, properties, body):
            try:
                data = json.loads(body)
                logger.info(f"Received MQ message: {data}")
                # 处理消息的逻辑可以在这里添加
                ch.basic_ack(delivery_tag=method.delivery_tag)
            except Exception as e:
                logger.error(f"Error processing MQ message: {str(e)}")
                ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
        
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(
            queue=current_app.config['MQ_QUEUE'], 
            on_message_callback=callback
        )
        
        logger.info("MQ consumer started")
        channel.start_consuming()
    
    consumer_thread = threading.Thread(target=consume, daemon=True)
    consumer_thread.start()

def send_message(message):
    """发送消息到MQ"""
    if not current_app.config['MQ_ENABLED']:
        logger.info("MQ is disabled, message not sent")
        return False
        
    try:
        channel.basic_publish(
            exchange='',
            routing_key=current_app.config['MQ_QUEUE'],
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
