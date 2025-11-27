import os

class Settings:
    # 项目基本信息
    PROJECT_NAME: str = "FastAPI MySQL MQ Demo"
    PROJECT_VERSION: str = "1.0.0"
    
    # MySQL配置
    MYSQL_HOST: str = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT: int = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_USER: str = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD", "123456")  # 替换为你的密码
    MYSQL_DB: str = os.getenv("MYSQL_DB", "fastapi_db")            # 需提前创建数据库
    SQLALCHEMY_DATABASE_URI: str = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    
    # MQ配置（带开关）
    MQ_ENABLED: bool = os.getenv("MQ_ENABLED", "True").lower() in ("false", "1", "t")  # MQ开关
    MQ_HOST: str = os.getenv("MQ_HOST", "localhost")
    MQ_PORT: int = int(os.getenv("MQ_PORT", 5672))
    MQ_USER: str = os.getenv("MQ_USER", "guest")
    MQ_PASSWORD: str = os.getenv("MQ_PASSWORD", "guest")
    MQ_QUEUE: str = os.getenv("MQ_QUEUE", "fastapi_user_queue")

# 实例化配置，供其他文件导入使用
settings = Settings()
