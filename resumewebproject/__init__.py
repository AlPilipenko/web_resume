from flask import Flask
import os

from resumewebproject.config import Config



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)


    from resumewebproject.main.routes import main
    app.register_blueprint(main)

    from resumewebproject.errors.handlers import errors
    app.register_blueprint(errors)

    return app
