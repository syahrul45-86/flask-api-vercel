from flask import Blueprint
from Controllers.UserController import get_users, get_user, create_user, update_user, update_user_partial, delete_user

user_bp = Blueprint('User_bp', __name__)

user_bp.route('/api/users', methods=['GET'])(get_users)

user_bp.route('/api/users/<int:user_id>', methods=['GET'])(get_user)

user_bp.route('/api/users' ,methods=['POST'])(create_user)

user_bp.route('/api/users/<int:user_id>', methods=['PATCH'])(update_user)

user_bp.route('/api/users/<int:user_id>', methods=['PUT'])(update_user_partial)

user_bp.route('/api/users/<int:user_id>', methods=['DELETE'])(delete_user)