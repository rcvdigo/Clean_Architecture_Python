import os


from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DbConnectionHandler():

    def __init__(self):

        load_dotenv()

        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            os.getenv("DB_DRIVER"),
            os.getenv("DB_USERNAME"),
            os.getenv("DB_PASSWORD"),
            os.getenv("DB_HOST"),
            os.getenv("DB_PORT"),
            os.getenv("DB_DATABASE")
        )
        self.__engine = self.create_database_engine()
        self.session = None

    def create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    def get_engine(self):
        return self.__engine

    def __enter__(self):
        sessionmake = sessionmaker(bind=self.__engine)
        self.session = sessionmake()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
