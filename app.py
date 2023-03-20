from flask import Flask

from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from api.model.movie import db, MoviesModel
import os
from config import Config
import api.route.singer as abc

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.register_blueprint(abc.singer_info)
    # db_path = os.path.join(os.path.dirname(__file__), 'app.db')
    # db_uri = 'sqlite:///{}'.format(db_path) 
    # app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    # db.init_app(app)
    # db.app = app
    # migrate = Migrate(app, db)
    # ma = Marshmallow(app)
    return app

if __name__ == '__main__':
    from argparse import ArgumentParser
    
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default= 5000, type= int, help = 'port to start')
    args = parser.parse_args()
    port = args.port

    app = create_app()
    # with app.app_context():
        # db.create_all()
        # new_movie = MoviesModel(name="The Shawshank Redemption", casts= "Tim Robbins", gernes="Dramma")
        # db.session.add(new_movie)
        # db.session.commit()
    app.run(host='0.0.0.0', port = port, debug = True)