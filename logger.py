#!/usr/bin/env python
# encoding: utf-8

import os
import logging
import settings

"""
Diese Klasse dient als Grundlage fuer den Logger.
Die Logs werden im Verzeichnis "Logs" gespeichert.
Die Instanzierung erfolgt wie folgend am Beispiel von dump.py beschrieben:
class Dump:
    def __init__(self, user, password, host, database):
        self.logger = Logger(self.__class__.__name__).get()  # Zugriff auf die "private" Variablen jeder Klasse
        ....
    self.logger.error("There was an error saving dump")      # Exemplarisches Logging mit dem Level "error".
                                                             # Weitere Level u.a.: info, debug, warning
"""
class Logger(object):

    def __init__(self, name):
        name = name.replace('.log','')
        logger = logging.getLogger('log_%s' % name)
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            file_name = os.path.join(settings.LOGGING_DIR, '%s.log' % name)
            handlerFile = logging.FileHandler(file_name)
            handlerConsole = logging.StreamHandler()
            self.addHandler(handlerFile, logger, 'DEBUG')
            self.addHandler(handlerConsole, logger, 'DEBUG')
        self._logger = logger

    def addHandler(self, handler, logger, level):
        formatter = logging.Formatter('%(asctime)s %(levelname)s:%(name)s %(message)s')
        handler.setFormatter(formatter)
        handler.setLevel(logging.getLevelName(level))
        logger.addHandler(handler)

    def get(self):
        return self._logger