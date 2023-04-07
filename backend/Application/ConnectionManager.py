from Application.Constants import *

import psycopg2


class ConnectionManagerMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ConnectionManager(metaclass=ConnectionManagerMeta):

    def __init__(self):
        self.conn = psycopg2.connect(database="postgres",
                                host=DB_ADDRESS,
                                user="postgres",
                                password=DB_PWD,
                                port=DB_PORT)
    
    def __del__(self):
        self.conn.close()

    def __enter__(self):
        return self
 
    def __exit__(self, *args):
        self.commit()

    def get_cursor(self):
        return self.conn.cursor()
    
    def commit(self):
        return self.conn.commit()