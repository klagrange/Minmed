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

    # import blueprints
    from home.views import home_app

    # register blueprints
    app.register_blueprint(home_app)

    return app

if __name__ == "__main__":
    app = create_app()
    print(app.config)

    from sqlalchemy import Column, Integer, String
    class User(Base):
        __tablename__ = 'users'
   
        id = Column(Integer, primary_key=True)
        name = Column(String)
        fullname = Column(String)
        password = Column(String)

        def __repr__(self):
            return "<User(name='%s', fullname='%s', password='%s')>" % (
                             self.name, self.fullname, self.password)

    print(User.__table__)