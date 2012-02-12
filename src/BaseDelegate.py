#!/usr/bin/env python
""" Provides methods for the Base Delegate Object.

The base delegate object provides methods to organize the measurement of the 
absorption coefficient.  The different enviroments the measurment is preformed
in will inheret the BaseDelegate object and provide the synchronization of the
measurement.
"""

import logging

# Alpha Classes
from AbsorptionCoefficient import AbsorptionCoefficient
from AudioIO import AudioIO
from ConfigDb import ConfigDb
from Measurement import Measurement
from MlsDb import MlsDb
from MeasurementDb import MeasurementDb
from SignalGenerator import SignalGenerator

__author__ = "Lance Jenkin"
__email__ = "lancejenkin@gmail.com"

class BaseDelegate(object):

    def __init__(self):
        """ Constructor for BaseDelegate """
        self.logger = logging.getLogger("Alpha")
        self.logger.debug("Creating BaseDelegate")
        
        # Load Singular Objects
        self.config_db = ConfigDb()

        # Load the Config
        self._loadConfig()
    def _loadConfig(self):
        """ Loads the default configuration from the ConfigDb """
        self.logger.debug("Entering _loadConfig")

        self.config_settings = self.config_db.getSettings("config")
        self.signal_settings = self.config_db.getSettings("signal")
        self.analysis_settings = self.config_db.getSettings("analysis")
        # Merge config settings and signal settings to create measurment
        # settings
        self.measurement_settings = dict(config_settings.items() + 
                                        signal_settings.items())
        
        self._getAudioDevices()
    def _saveConfig(self):
        """ Saves the settings as the new default settings """
        self.logger.debug("Entering _saveConfig")

        self.config_db.saveSettings("config", self.config_settings)
        self.config_db.saveSettings("signal", self.signal_settings)
        self.config_db.saveSettings("analysis", self.analysis_settings)
    
    def _resetDefaults(self):
        """ Resets to the default settings """
        self.logger.debug("Entering _resetDefaults")

        self.config_db._setDefaults()
    
    def newMeasurement(self, measurment_settings=None):
        """ Starts a new measurement with the specified settings.

        Note, could take a non-neglible amount of time, should run in seperate
        thread if used in a GUI enviroment.

        :param measurment_settings:
            A dictionary containing the measurements settings to use for a new
            measurement. If not given, then use default settings
        :type measurment_settings:
            dict
        
        :returns:
            Measurement - The measurment object created, with the captured 
            measurement.
        """
        self.logger.debug("Entering newMeasurement")

        if measurment_settings is None:
            measurment_settings = self.measurment_settings
        
        measurement = Measurement(measurment_settings)

        measurment.startMeasurement()

        return measurement
    
    def saveMeasurement(self, measurement, measurement_filename):
        """ Save the measurement to the specified filename.

        Note, could take a non-neglible amount of time, should run in seperate
        thread if used in a GUI enviroment.

        :param measurement:
            A measurement that has be completed, returned from the 
            newMeasurement function.
        :type measurement:
            Measurement
        :param measurement_filename:
            The filename to save the measurement to.
        :type measurement_filename:
            str 
        """
        self.logger.debug("Entering saveMeasurement")

        measurement_db = MeasurementDb(measurement_filename)

        measurement_attr = measurement.measurement_settings
        input_signals = measurement.input_signals
        generator_signals = measurement.generator_signals

        measurement_db.saveMeasurementAttributes(measurement_attr)

        assert(len(input_signals) == len(generator_signals))
        
        for signal_index in range(len(input_signals)):
            measurement_db.saveSignal(input_signals[signal_index],
                                 generator_signals[signal_index])
    
    def loadMeasurement(self, measurement_filename):
        """ Loads a measurement located by the specified measurement_filename.

        Note, could take a non-neglible amount of time, should run in seperate
        thread if used in a GUI enviroment.

        :param measurement_filename:
            The filename of the saved measurement.
        :type measurement_filename:
            str
        
        :returns:
            AbsorptionCoefficient - An object that has analysed the measurement
            and determined the absorption coefficient of the material under
            measurement.
        """
        self.logger.debug("Entering loadMeasurement")

        measurement_db = MeasurementDb(measurement_filename)

        # Get parameters from the measurement database
        if measurement_db.isAnalyzed():
            analysis_settings = measurement_db.getAnalysisSettings()
        else:
            analysis_settings = self.analysis_settings
        
        measurement_settings = measurement_db.getMeasurementSettings()

        input_signals = measurement_db.input_signals
        generator_signals = measurement_db.generator_signals

        alpha = AbsorptionCoefficient(input_signals, generator_signals,
                                      measurement_settings, analysis_settings)

        return alpha
    
    def _getAudioDevices(self):
        """ Gets the available audio devices on the system """
        self.logger.debug("Entering _getAudioDevices")
        
        audio = AudioIO()
        self.audio_devices = audio.getAudioDevices()
          
if __name__ == "__main__":
    """ A simple example showing the use of the BaseDelegate """
    from tempfile import mkstemp
    import pylab as py
    logger = logging.getLogger("Alpha")
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)

    self.logger.info("Creating BaseDelegate Object")
    delegate = BaseDelegate()
    self.logger.info("Starting Measurement")
    measurement = delegate.newMeasurement()
    self.logger.debug("Creating temporary file")
    measurement_file = mkstemp()[1]
    self.logger.info("Saving measurment")
    delegate.saveMeasurement(measurement, measurement_file)
    alpha = delegate.loadMeasurement(measurement_file)

    py.plot(alpha.alpha)
    py.show()


