from flask import Blueprint, request, jsonify
from app.services.db_service import create_user, get_user
from app.services.mq_service import send_message

api_bp = Blueprint('api', __name__)

@api_bp.route('/users', methods=['POST'])
def create_user_api():
    """创建用户接口"""
    data = request.get_json()
    
    if not data or 'username' not in data or 'email' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        user = create_user(data['username'], data['email'])
        
        # 发送消息到MQ
        send_message({
            'action': 'user_created',
            'user_id': user.id,
            'username': user.username
        })
        
        return jsonify(user.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_api(user_id):
    """获取用户信息接口"""
    try:
        user = get_user(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        return jsonify(user.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500
