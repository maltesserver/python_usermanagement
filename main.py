#!/usr/bin/env python
# encoding: utf-8

from commands import *
from DB_GetUsers import *
from DB_AddUser import *

print('[########################]')
print('[#                      #]')
print('[#                      #]')
print('[#      Skript von      #]')
print('[#                      #]')
print('[#        Felix         #]')
print('[#        Malte         #]')
print('[#       Nagehan        #]')
print('[#                      #]')
print('[#                      #]')
print('[########################]')
print('')
print('Internetverbindung: ✓ | ✘')
print('')
print('Datenbankverbindung: ✓ | ✘')
print('')
print('')
while True:

    print('[########################]')
    print('')
    print('Help:')
    print('')
    print('-h   ->  Get the Help Page')
    print('-i   ->  Get the Info Page')
    print('-adduser   ->  Create a User')
    print('-getuser   ->  Get Info about a User')
    print('-deluser   ->  Delete a User')
    print('')
    print('[########################]')

#Commandsabfrage

    commands = input("Command: ")
    print
    if commands == "-h":
        print('')
    elif commands == "-i":
        info()
    elif commands == "-adduser":
        AddUser.CreateForm()
    elif commands == "-getuser":
        GetUsers().ListUsersFromDB()
    elif commands == "-deluser":
        print('')
sleep(1)
