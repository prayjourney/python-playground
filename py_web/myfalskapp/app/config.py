import os

class Config:
    # 基础配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    
    # MySQL配置
    MYSQL_HOST = os.environ.get('MYSQL_HOST') or 'localhost'
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT') or 3306)
    MYSQL_USER = os.environ.get('MYSQL_USER') or 'root'
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or '123456'
    MYSQL_DB = os.environ.get('MYSQL_DB') or 'myflaskdb'
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # MQ配置
    MQ_ENABLED = os.environ.get('MQ_ENABLED', 'True').lower() in ('true', '1', 't')
    MQ_HOST = os.environ.get('MQ_HOST') or 'localhost'
    MQ_PORT = int(os.environ.get('MQ_PORT') or 5672)
    MQ_USER = os.environ.get('MQ_USER') or 'guest'
    MQ_PASSWORD = os.environ.get('MQ_PASSWORD') or 'guest'
    MQ_QUEUE = os.environ.get('MQ_QUEUE') or 'flask_queue'
