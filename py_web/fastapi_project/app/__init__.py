from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from app.config import settings  # 导入配置
from app.core.db import Base, engine  # 导入数据库基类和引擎
from app.core.mq import init_mq, close_mq  # 导入MQ初始化和关闭函数
from app.api.v1 import api_router  # 导入API路由

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("fastapi")

def create_app() -> FastAPI:
    """创建并配置FastAPI应用（应用工厂模式）"""
    # 创建FastAPI实例
    app = FastAPI(
        title=settings.PROJECT_NAME,  # API文档标题
        version=settings.PROJECT_VERSION  # API版本
    )
    
    # 配置CORS（解决跨域问题）
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # 允许所有域名（生产环境需指定具体域名）
        allow_credentials=True,
        allow_methods=["*"],  # 允许所有HTTP方法
        allow_headers=["*"],  # 允许所有请求头
    )
    
    # 创建数据库表（如果不存在）
    Base.metadata.create_all(bind=engine)
    
    # 注册API路由（所有接口路径前会加上"/api/v1"）
    app.include_router(api_router, prefix="/api/v1")
    
    # 应用启动事件（启动时执行）
    @app.on_event("startup")
    def startup_event():
        logger.info("应用启动中...")
        init_mq()  # 初始化MQ
        logger.info(f"应用启动完成。访问 http://localhost:8000/docs 查看API文档")
    
    # 应用关闭事件（关闭时执行）
    @app.on_event("shutdown")
    def shutdown_event():
        logger.info("应用关闭中...")
        close_mq()  # 关闭MQ连接
        logger.info("应用已关闭")
    
    return app
