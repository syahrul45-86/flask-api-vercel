from flask import jsonify,request
from Models.LevelModel import Level
from config import db

def get_levels():
    levels = Level.query.all()
    return jsonify([level.to_dict() for level in levels])



def get_levelid(id):
    levelid = Level.query.get(id)
    if not levelid:
        return jsonify({'error': 'level not found'}),404
    return jsonify(levelid.to_dict())


def add_level():
    new_level_data = request.get_json()
    new_level = Level(name=new_level_data['name'])
    db.session.add(new_level)
    db.session.commit()
    return jsonify({'message' : 'level added successfully', 'level':new_level.to_dict()}),201


def update_level(id):
    levels = Level.query.get(id)
    if not levels:
        return({'error': 'level not found'}),404
    
    update_data = request.get_json()
    levels.name = update_data.get('name',levels.name)
    db.session.commit()
    return jsonify({'message': 'level update successfullty', 'level': levels.to_dict()})


def delete_level(id):
    levels = Level.query.get(id)
    if not levels:
        return jsonify({'error': 'level not found'}),404
    db.session.delete(levels)
    db.session.commit()
    return jsonify({'message' : 'level successfully delete'})
