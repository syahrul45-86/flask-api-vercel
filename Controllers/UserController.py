from flask import jsonify, request
from Models.UserModel import User
from Models.LevelModel import Level
from config import db

def get_users():
    users = User.query.all()
    users_with_levels = []
    
    for user in users:
        levels = Level.query.get(user.level_id)
        users_with_levels.append({
            'id' : user.id,
            'username': user.username,
            'password': user.password,
            'fullname': user.fullname,
            'status': user.status,
            'level_name' : levels.name if levels else "no levels"
        })
        

    return jsonify(users_with_levels)

# ROUTE: GET user berdasarkan ID

def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    levels = Level.query.get(user.level_id)
    user_data = {
        'id' : user.id,
        'username': user.username,
        'password': user.password,
        'fullname': user.fullname,
        'status': user.status,
        'level_name' : levels.name if levels else "no levels"
    }
    return jsonify(user_data)


def create_user():
    new_user_data = request.get_json()
    new_user = User(
        username=new_user_data['username'],
        password=new_user_data['password'],
        fullname=new_user_data['fullname'],
        status=new_user_data['status'],
        level_id = new_user_data['level_id']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'user added successfully', 'User': new_user.to_dict()}),201


def update_user(user_id):
    user =User.query.get(user_id)
    if not user:
        return jsonify({'error': 'user not found'}),404
    
    updated_data = request.get_json()
    user.username = updated_data.get('username', user.username)
    user.password = updated_data.get('password', user.password)
    user.fullname = updated_data.get('fullname', user.fullname)
    user.status = updated_data.get('status', user.status)
    user.level_id = updated_data.get('level_id', user.level_id)

    
    db.session.commit()
    return jsonify({'message': 'user successfully updated', 'user': user.to_dict()})


def update_user_partial(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'error': 'user not found'}), 404

    updated_data = request.get_json()
    if 'username' in updated_data:
        user.username = updated_data['username']
    if 'password' in updated_data:
        user.password = updated_data['password']
    if 'fullname' in updated_data:
        user.fullname = updated_data['fullname']
    if 'status' in updated_data:
        user.status = updated_data['status']
    if 'level_id' in updated_data:
        levels = Level.query.get(updated_data['level_id'])
        if levels:
            user.level_id = updated_data['level_id']
        else:
            return jsonify({'error': 'levelnot found'}), 404

    db.session.commit()
    return jsonify({'message': 'level updated successfully', 'book': levels.to_dict()})

def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'user not found'}),404
    
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'user deleted successfully'})