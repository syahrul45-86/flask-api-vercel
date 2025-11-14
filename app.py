from config import app, db
from Routes.User_bp import user_bp
from Routes.Level_bp import level_bp

# register blueprint
app.register_blueprint(user_bp)
app.register_blueprint(level_bp)

# Saat di local (run manual)
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # berjalan hanya local

# Vercel akan mencari variabel bernama 'app'
handler = app
