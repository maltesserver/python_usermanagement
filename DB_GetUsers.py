#!/usr/bin/env python
# encoding: utf-8

from unittest import TestCase
from connect_db import DbConnect
import yaml

with open(r'config/database.yml') as file:
    # Load Yaml File
    config = yaml.load(file, yaml.FullLoader)

    # Get Data from File
    host = config["Database"]["Host"]
    port = config["Database"]["Port"]
    database = config["Database"]["Database"]
    user = config["Database"]["User"]
    pw = config["Database"]["Password"]


class GetUsers(object):

    @staticmethod
    def ListUsersFromDB():
        db = DbConnect(user, pw, host, port, database)
        cnx = db.connectDb()
        cursor = cnx.cursor()
        sql = "select * from mitarbeiter"
        cursor.execute(sql)
        rs = cursor.fetchall()
        simple_list = []
        for row in rs:
            simple_list.append({
                "id": row[0],
                "Vorname": row[1],
                "Nachname": row[2],
                "Systemnutzer": row[3],
                "Systemzugriff": row[4],
                "Gruppen": row[5],
                "Zugriff": row[6],
                "Mail": row[10]
            })
        for row in simple_list:
            print("[-----------------------------]")
            print("User ID: " + str(row["id"]))
            print("Name: " + row["Vorname"] + " " + row["Nachname"])
            print("Systemnutzer: " + str(row["Systemnutzer"]))
            print("Systemzugriff: " + row["Systemzugriff"])
            print("Gruppe: " + row["Gruppen"])
            print("Zugriff: " + row["Zugriff"])
            print("E-Mail: " + row["Mail"])
            print("[-----------------------------]")
            print()

        return simple_list

