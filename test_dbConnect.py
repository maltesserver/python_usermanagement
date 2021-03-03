from unittest import TestCase
from connect_db import DbConnect
import ConfigParser

"""Dieser Test tested die Verbindung zur Datenbank"""
config = ConfigParser.ConfigParser(allow_no_value=True)
config.read('config/database.yml')
dbip = config.items('DBHost')
dbport = config.items('DBPort')
dbname = config.items('DBName')
dbuser = config.items('DBUser')
dbpassword = config.items('DBPassword')

user = '$dbuser'
pw = '$dbpassword'
host = '$dbhost'
port = '$dbport'
database = '$dbname'


class TestDbConnect(TestCase):

    def test_connectDb(self):
        db = DbConnect(user, pw, host, port, database)
        db.connectDb()
        db.closeDb()

    def test_select_user_table(self):
        db = DbConnect(user, pw, host, port, database)
        cnx = db.connectDb()
        cursor = cnx.cursor()
        sql = "select * from user"
        cursor.execute(sql)
        rs = cursor.fetchall()
        print("Ergebnis {}".format(rs))

    def test_select_user_talbe_names_with_loop(self):
        db = DbConnect(user, pw, host, port, database)
        cnx = db.connectDb()
        cursor = cnx.cursor()
        sql = "select * from user"
        cursor.execute(sql)
        rs = cursor.fetchall()
        for row in rs:
            print ("Name Tabelle User {}".format(row[1]))


