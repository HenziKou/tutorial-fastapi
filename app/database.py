from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# Imports for Python Postgres library for db connection
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time


# Format of the connection string need to pass into SQLAlchemy
# SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@<ip-address/hostname>:<port_number>/<database_name>"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

# Excuslive to SQLite, you must pass in 'connect_args={"check_same_thread": False}'
# after the first param in create_engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# ----- Connecting to Database -----
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ----- Connecting to Database -----


# Python Postgres library to connect to database
# Not required because we are using SQLAlchemy to connect
# ----- Connecting to Database -----
# while True:
#     try:
#         conn = psycopg2.connect(host=f'{settings.database_hostname}',
#                                 database=f'{settings.database_name}',
#                                 user=f'{settings.database_username}',
#                                 password=f'{settings.database_password}',
#                                 cursor_factory=RealDictCursor
#                                )
#         cursor = conn.cursor()
#         print("Database connection was successful!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)
# ----- Connecting to Database -----
