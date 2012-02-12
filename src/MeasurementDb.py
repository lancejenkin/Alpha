#!/usr/bin/env python
""" Provides an interface to save signals, as well as the settings used to
    create the signal, as well as the settings used to analyze the signal.
"""

import logging
import pickle
import sqlite3
import zlib
import os

__author__ = "Lance Jenkin"
__email__ = "lancejenkin@gmail.com"

class MeasurementDb(object):
    
    def __init__(self, filename):
        """ Constructor for MeasurementDb obect.

        :param filename:
            The filename where the measurement will be saved.
        :type filename:
            str
        """
        self.logger = logging.getLogger("Alpha")
        self.logger.debug("Creating MeasurementDb Object")

        if os.path.exists(filename):
            os.remove(filename)

        try:
            self.conn = sqlite3.connect(filename)
        except sqlite3.OperationalError as error:
            self.logger.error("Could not open %s: %s"%(filename, error))
            raise Exception("Database Error: %s"%(error))
        
        self._setupDatabase()
    
    def __del__(self):
        """ Deconstructor, ensures that the changes to the database have be 
            commited.
        """
        self.logger.debug("Entering __del__")

        self.conn.commit()
        
    def _setupDatabase(self):
        """ Setup signal database schema so that signals can be saved. """
        self.logger.debug("Entering _setupDatabase")

        cursor = self.conn.cursor()

        cursor.execute("""CREATE TABLE "attributes" (
                        "key" TEXT PRIMARY KEY,
                        "value" TEXT)""")
        
        cursor.execute("""CREATE TABLE "analysis" (
                        "key" TEXT PRIMARY KEY,
                        "value" TEXT)""")

        cursor.execute("""CREATE TABLE "signal" (
                        "id" INTEGER PRIMARY KEY,
                        "signal" BLOB,
                        "generator" BLOB,
                        "enabled" INTEGER DEFAULT 1)""")
        
        self.conn.commit()
        cursor.close()
    
    def saveMeasurementAttributes(self, attributes):
        """ Save attributes associated with the measurment.

        When saving a new signal, the attributes will contain the measurement 
        settings used when creating the signal.  When analysing a signal it 
        will contain the analysis settings.  It will also contain the location
        of the location of the start of the signal.

        :param attributes:
            A dictionary of attributes associated with the captured signals.
        :type attributes:
            dict
        """
        self.logger.debug("Entering saveMeasurementAttributes")

        cursor = self.conn.cursor()

        for key, value in attributes.items():
            cursor.execute("""REPLACE INTO "attributes" ("key", "value") 
                                VALUES (?, ?)""", (key, value,))
        
        self.conn.commit()

        cursor.close()
    
    def saveAnalysisSettings(self, analysis_settings):
        """ Saved the settings used to analyse the signals.

        :param settings:
            A dictionary of settings used to analyse the signals.
        :type settings:
            dict
        """
        self.logger.debug("Entering saveAnalysisSettings")

        cursor = self.conn.cursor()

        for key, value in attributes.items():
            cursor.execute("""REPLACE INTO "analysis" ("key", "value") 
                                VALUES (?, ?)""", (key, value,))
        
        self.conn.commit()

        cursor.close()
    
    def isAnalysed(self):
        """ Determine if the signals have be analysed by counting the records
            in the analysis table.
        """
        self.logger.debug("Entering isAnalysed")

        cursor = self.conn.cursor()

        cursor.execute("SELECT COUNT(*) as count FROM analysis")

        row = cursor.fetchone()

        if int(row["count"]) > 0:
            return True
        else:
            return False

    def saveSignal(self, input_signal, generator_signal):
        """ Save captured input and generator signals.

        :param input_signal:
            The signal caputred by the microphone.
        :type input_signal:
            array of float
        :param generator_signal:
            The signal cpatured by the sound card, representing what the sound
            card produces.
        :type generator_signal:
            array of float
        """
        self.logger.debug("Entering saveSignal")

        cursor = self.conn.cursor()

        pickled_input = pickle.dumps(input_signal)
        pickled_generator = pickle.dumps(generator_signal)

        compressed_input = buffer(zlib.compress(pickled_input, 9))
        compressed_generator = buffer(zlib.compress(pickled_generator, 9))

        cursor.execute("INSERT INTO signal (input, generator) VALUES (?, ?)",
             (compressed_input, compressed_generator))
        self.conn.commit()
        
        cursor.close()
    
    def getMeasurementSettings(self):
        """ Get measurement settings used to measure the signals.

        :returns:
            dict - A dictionary containing all the measurement_settings
        """
        self.logger.debug("Entering getAttributes")

        cursor = self.conn.cursor()

        cursor.execute("SELECT * FROM attributes")

        results = cursor.fetchall()

        measurement_settings = {}
        for row in results:
            attributes[row["key"]] = row["value"]
        
        cursor.close()

        return measurement_settings
    
    def getAnalysisSettings(self):
        """ Get the analysis settings saved in the database, if any.
        """
        self.logger.debug("Entering getAnalysisSettings")

        cursor = self.conn.cursor()

        cursor.execute("SELECT * FROM analysis")

        results = cursor.fetchall()

        analysis_settings = {}
        for row in results:
            analysis_settings[row["key"]] = row["value"]
        
        cursor.close()

        return analysis_settings

    def getSignals(self):
        """ Return all the signals in the database.

        :returns:
            array - An array of dictionary containg the signals in the database
        """
        self.logger.debug("Entering getSignals")

        cursor = self.conn.cursor()

        cursor.execute("SELECT * FROM signal ORDER BY id ASC")

        results = cursor.fetchall()

        signals = []
        for row in results:
            signal = {"input": row["input"], 
                      "generator": row["generator"]}
            # For compatibility with previous versions, need to ensure the 
            # enabled column is in the table
            if "enabled" in row:
                signal["enabled"] = row["enabled"]
            signals.append(signal)
        
        cursor.close()

        return signals
        
    @staticmethod
    def _dict_factory(cursor, row):
        """ Dictionary factory used for sqlite3 to return rows as dictionaries,
            with column names as keys.
        """
        
        d = {}
        for idx,col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d