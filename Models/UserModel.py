from config import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    fullname = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    level_id = db.Column(db.Integer, db.ForeignKey('level.id_level'), nullable=False)

    
    def to_dict(self):
        return{
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'fullname': self.fullname,
            'status': self.status,
            'level_id': self.level_id
            
        }