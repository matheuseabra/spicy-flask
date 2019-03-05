import os

from flask import Flask
from . import db
from . import blog
from . import auth


def create_app(test_config=None):
    # create and confgiure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(
        app.instance_path, 'blog.sqlite'),)

    # Load the instance config, if exists
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    # check that the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    app.register_blueprint(auth.blueprint)
    app.register_blueprint(blog.blueprint)
    app.add_url_rule('/', endpoint='index')

    return app
