from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from config.config import *
from urllib.parse import quote

Base = declarative_base()
DBSession = scoped_session(sessionmaker())
postgres_engine = None

database_credentials = get_database_credentials()

postgres_connection_string = 'postgresql+psycopg2://{}:{}@{}/{}'.format(database_credentials['DATABASE_USERNAME'], quote(database_credentials['DATABASE_PASSWORD']), database_credentials['DATABASE_HOST'], database_credentials['DATABASE_NAME'])

postgres_engine = create_engine(postgres_connection_string)
conn = postgres_engine.connect()

DBSession.configure(bind=postgres_engine, expire_on_commit=False)