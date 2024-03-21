from flask import Flask
from med.config import Config
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
from  flask_migrate import Migrate
# from flask_marshmallow import Marshmallow
from flask_toastr import Toastr


db = SQLAlchemy()
# login_manager = LoginManager()
migrate = Migrate()
# ma = Marshmallow()
toastr = Toastr()

# login_manager.login_view = 'main.index'
# login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    # login_manager.init_app(app)
    migrate.init_app(app, db)
    # ma.init_app(app)
    toastr.init_app(app)

    from med.main.routes import main
    # from embed.user.routes import user
    # from embed.admin.routes import admin

    app.register_blueprint(main)
    # app.register_blueprint(user)
    # app.register_blueprint(admin)

    return app