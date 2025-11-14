from config import app, db
from routes.User_bp import user_bp
from routes.Level_bp import level_bp

# === ROUTE ROOT UNTUK TEST ===
@app.route("/")
def home():
    return {"message": "API is running on Vercel"}

# === REGISTER BLUEPRINT ===
app.register_blueprint(user_bp)
app.register_blueprint(level_bp)

# === LOCAL DEVELOPMENT MODE ===
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

# === HANDLER UNTUK VERCEL ===
handler = app
