import os
from flask import Flask
from models import db

def create_app():
    app = Flask(__name__)
    app.secret_key = "supersecretkey"

    # Database path (inside instance folder)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'users.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)

    # Register blueprints
    from routes.auth import auth_bp
    from routes.main import main_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
