#!/usr/bin/env python
# encoding: utf-8

import yaml
import mysql.connector

from connect_db import DbConnect

with open(r'config/database.yml') as file:
    # Load Yaml File
    config = yaml.load(file, yaml.FullLoader)

    # Get Data from File
    host = config["Database"]["Host"]
    port = config["Database"]["Port"]
    database = config["Database"]["Database"]
    user = config["Database"]["User"]
    pw = config["Database"]["Password"]


class AddUser(object):

    @staticmethod
    def CreateForm():
        print("Wählen die einen Vornamen")
        Vorname = input("Vorname: ")
        print(" ")
        print("[-------]")
        print(" ")
        print("Wählen die einen Nachnamen")
        Nachname = input("Nachname: ")
        print(" ")
        print("[-------]")
        print(" ")
        print("Wählen die einen Systembenutzer (Anmeldename)")
        Systembenutzer = input("Systembenutzer: ")
        print(" ")
        print("[-------]")
        print(" ")
        print("Auf welchen System soll der Benutzer zugreifen können?")
        print("Wählen sie zwischen folgenden Systemen aus:")
        print("admin.Domain.de")
        print("user.Domain.de")
        Systemzugriff = input("Antwort: ")
        print(" ")
        print("[-------]")
        print(" ")
        print("In welcher Gruppe soll der Benutzer sein?")
        print("Wählen sie zwischen folgenden Gruppen aus:")
        print("admin")
        print("user")
        Gruppe = input("Gruppe: ")
        print(" ")
        print("[-------]")
        print(" ")
        print("Welchen Zugriff soll der Benutzer haben?")
        print("Wählen sie aus:")
        print("komplett")
        print("beschränkt")
        Zugriff = input("Zugriff: ")
        print(" ")
        print("[-------]")
        print(" ")
        print("Welche E-mail hat der Benutzer?")
        Mail = input("E-Mail: ")
        print(" ")
        print("[-------]")
        print(" ")

        if Vorname > 3:
            print("Der Vorname lautet " + Vorname)
            if Nachname > 3:
                print("Der Nachname lautet " + Nachname)
                if Systembenutzer > 5:
                    print("Der Systembenutzer lautet " + Systembenutzer)
                    if Systemzugriff > 5:
                        print("Der Nutzer " + Systembenutzer + "wird den folgenden Zugriff haben " + Systemzugriff)
                        if Gruppe > 4:
                            print("Die Gruppe lautet " + Gruppe)
                            if Zugriff > 3:
                                print("Der Benutzer wird die folgenden Rechte haben: " + Zugriff)
                                if Mail > 5:
                                    print("Die E-Mail " + Mail + " wurde eingetragen")
                                    print(" ")
                                    print(" ")
                                    print(" ")
                                    print("Versuche die Daten in die Datenbank einzutragen")

                                    mydb = mysql.connector.connect(host, user,pw,database)
                                    mycursor = mydb.cursor()
                                    sql = "INSERT INTO mitarbeiter('Vorname', 'Nachname', 'Systemnutzer', 'Systemzugriff', 'Gruppen', 'Zugriff', 'Zeitraum', 'SSH_Key', 'Passwort', 'Mail') VALUES (" + Vorname + "," + Nachname + "," + Systembenutzer + "," + Systemzugriff + "," + Gruppe + "," + Zugriff + ",0000-00-00, Ja, Ja," + Mail + ")"
                                    mycursor.execute(sql)

                                    mydb.commit()

                                    print("User Angelegt, User ID:", mycursor.lastrowid)

                                else:
                                    print("Die E-Mail Fehlt")
                            else:
                                print("Die Zugriffsberechtigungen fehlen!")
                        else:
                            print("Es wurde keine Gruppe eingetragen")
                    else:
                        print("Der Systemzugriff ist leer")
                else:
                    print("Der Systembenutzer ist zu Kurz oder ist leer!")
            else:
                print("Der Nachname darf nicht leer sein!")
        else:
            print("Der Vorname darf nicht leer sein!")
        return
