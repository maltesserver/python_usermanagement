#!/usr/bin/env python
# encoding: utf-8

import psutil
#import wmi
import os
import smtplib
import socket
from commands import *
from datetime import datetime

# Zeit Definieren

now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
time = now.strftime("%H:%M:%S")
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
date_time_log = now.strftime("%m-%d-%Y-%H-%M-%S")




def info():
    print("")
    print("")
    print("Code von: Felix, Malte und Nagehan")
    print("GitLab Link: https://gitlab.realtox.network/itech-bs14/usermanagement")
    print("")
    print("Ram Usage: " + str(psutil.virtual_memory()[2]) + "%")
    print("")
    print("")
    return
