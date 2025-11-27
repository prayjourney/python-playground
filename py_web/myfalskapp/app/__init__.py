from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

# 初始化数据库
db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # 初始化扩展
    db.init_app(app)
    
    # 注册蓝图
    from app.controllers.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # 创建数据库表
    with app.app_context():
        db.create_all()
        
        # 初始化MQ服务
        from app.services.mq_service import init_mq
        init_mq(app)
    
    return app
