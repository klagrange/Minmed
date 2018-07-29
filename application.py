from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import SQLALCHEMY_DATABASE_URI

db = SQLAlchemy()
Base = declarative_base()

def create_app(**config_overrides):
    app = Flask(__name__)

    # load config
    app.config.from_pyfile('settings.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # apply overrides for tests
    app.config.update(config_overrides)

    # setup ORM
    db.init_app(app)
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    
    import registration.models
    Base.metadata.create_all(bind=engine)
    Base.query = db_session.query_property()

    # import blueprints
    from registration.views import attach_db_session
    registration_app = attach_db_session(db_session)
    from home.views import home_app

    # register blueprints
    app.register_blueprint(registration_app)
    app.register_blueprint(home_app)

    return app