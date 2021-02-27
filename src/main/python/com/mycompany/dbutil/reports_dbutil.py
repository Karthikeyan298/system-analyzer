'''
Created on 03-Nov-2017

@author: karthikeyan
'''
import os
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError


class DBUtil(object):

    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '3307')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'root')
    DB_NAME = os.getenv('DB_NAME', 'system_analyzer')

    def create_database(self):
        engine = create_engine(
            'mysql://' + self.DB_USER + ':'
            + self.DB_PASSWORD
            + '@' + self.DB_HOST
            + ':' + self.DB_PORT
            )
        conn = engine.connect()
        conn.execute("commit")
        try:
            conn.execute("create database " + self.DB_NAME)
            conn.close()
        except ProgrammingError:
            return

    def create_engine(self):
        return create_engine('mysql://' + self.DB_USER + ':' + self.DB_PASSWORD + '@' + self.DB_HOST + ':'
                             + self.DB_PORT + '/system_analyzer', echo=False)
