from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel
from typing import Optional, List

# 创建FastAPI应用实例
app = FastAPI(
    title="简单的FastAPI示例",
    description="包含多种请求类型的演示",
    version="1.0.0"
)

# 定义请求体模型
class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None
    tags: List[str] = []

class User(BaseModel):
    username: str
    full_name: Optional[str] = None

# 1. 基本GET请求
@app.get("/")
def read_root():
    """根路径，返回欢迎信息"""
    return {"message": "欢迎使用FastAPI示例"}

# 2. 带路径参数的GET请求
@app.get("/items/{item_id}")
def read_item(
    item_id: int = Path(..., title="项目ID", ge=1),
    q: Optional[str] = Query(None, title="查询参数", max_length=50)
):
    """根据ID获取项目信息，支持可选查询参数"""
    return {"item_id": item_id, "q": q}

# 3. POST请求（单请求体）
@app.post("/items/")
def create_item(item: Item):
    """创建新项目"""
    item_dict = item.dict()
    if item.price < 10:
        item_dict.update({"警告": "价格过低"})
    return item_dict

# 4. PUT请求（路径参数+请求体）
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """更新项目信息"""
    return {"item_id": item_id, **item.dict()}

# 5. 多请求体参数
@app.post("/items/{item_id}/user/")
def create_item_for_user(
    item_id: int,
    item: Item,
    user: User,
    priority: int = Body(..., ge=1, le=10)
):
    """为用户创建项目，包含多个请求体参数"""
    results = {
        "item_id": item_id,
        "item": item,
        "user": user,
        "priority": priority
    }
    return results

# 6. 带路径参数验证的请求
@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(
    user_id: int = Path(..., title="用户ID", ge=100, le=9999),
    item_id: str = Path(..., title="项目ID", min_length=3, max_length=10),
    q: Optional[str] = None
):
    """带复杂参数验证的请求示例"""
    return {"user_id": user_id, "item_id": item_id, "q": q}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
