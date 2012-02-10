#!/usr/bin/env python
""" Provides an interface to save signals, as well as the settings used to
    create the signal, as well as the settings used to analyze the signal.
"""

import logging
import pickle
import sqlite3
import zlib

__author__ = "Lance Jenkin"
__email__ = "lancejenkin@gmail.com"

class SignalDb(object):
    
    def __init__(self, filename):
        """ Constructor for SignalDb obect.

        :param filename:
            The filename to save the signal to.
        :type filename:
            str
        """
        self.logger = logging.getLogger("Alpha")
        self.logger.debug("Creating SignalDb Object")


    @staticmethod
    def _dict_factory(cursor, row):
        """ Dictionary factory used for sqlite3 to return rows as dictionaries,
            with column names as keys.
        """
        
        d = {}
        for idx,col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d