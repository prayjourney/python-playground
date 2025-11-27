from fastapi import APIRouter
from app.api.v1.endpoints import users  # 导入用户接口

# 创建API路由汇总实例
api_router = APIRouter()

# 包含用户接口路由（所有用户接口路径前会加上"/users"）
api_router.include_router(users.router, prefix="/users", tags=["users"])

# 如需添加其他接口（如订单接口），按同样方式添加
# from app.api.v1.endpoints import orders
# api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
