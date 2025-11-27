from app import db
from app.models.user import User
import logging

logger = logging.getLogger(__name__)

def create_user(username, email):
    """创建新用户"""
    try:
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        logger.info(f"User created: {username}")
        return user
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error creating user: {str(e)}")
        raise

def get_user(user_id):
    """获取用户信息"""
    try:
        user = User.query.get(user_id)
        return user
    except Exception as e:
        logger.error(f"Error getting user: {str(e)}")
        raise
