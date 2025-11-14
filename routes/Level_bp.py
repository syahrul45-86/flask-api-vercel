from flask import Blueprint
from Controllers.LevelController import get_levels, get_levelid, add_level, update_level, delete_level

level_bp = Blueprint('level_bp', __name__)

level_bp.route('/api/levels', methods=['GET'])(get_levels)

level_bp.route('/api/levels/<int:id>', methods=['GET'])(get_levelid)

level_bp.route('/api/levels', methods=['POST'])(add_level)

level_bp.route('/api/levels/<int:id>', methods=['PUT'])(update_level)

level_bp.route('/api/levels/<int:id>', methods=['DELETE'])(delete_level)