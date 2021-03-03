#!/usr/bin/env python
# encoding: utf-8

import mysql.connector
from mysql.connector import errorcode

from logger import Logger

class DbConnect:

    def __init__(self, user, password, host, port, db):
        self.logger = Logger(self.__class__.__name__).get()
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db = db

    def connectDb(self):
        try:
            self.cnx = mysql.connector.connect(user=self.user,
                                      password=self.password,
                                      host=self.host, port=self.port, db=self.db)
            self.logger.info("Connection to db established")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.logger.error("Something is wrong with your user name or password...Error: %s" %err)
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.logger.error("Database does not exist...Error: %s" %err)
            else:
                self.logger.error("Undefined DB-connection problem...Error: %s" %err)
        return self.cnx


    def closeDb(self):
        self.cnx.close()
        self.logger.info("Connection do db closed")

    def get_cursor(self):
        cursor = self.cnx.cursor()