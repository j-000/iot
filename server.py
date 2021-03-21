from sqlalchemy import create_engine
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker
)
from flask import Flask
import os
import config
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)


if os.getenv('ENV') == 'production':
    app.config.from_object(config.ProductionConfig)
elif os.getenv('ENV') == 'development':
    app.config.from_object(config.DevelopmentConfig)
else:
    raise NotImplementedError('ENV Variable not set.')


engine = create_engine(app.config.get('SQLALCHEMY_DATABASE_URI'), convert_unicode=True, connect_args={'check_same_thread': False})
db = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
