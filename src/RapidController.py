#!/usr/bin/env python
""" Provides the controller for the RapidView

The RapidAlpha view provides a means to preform a quick absorption measurement
of a material.  The only settings that can be changed in the rapid view, is the
selecting of input and output devices.
"""

import logging

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from RapidView.RapidAlphaWindow import Ui_RapidAlphaWindow
from Grapher import Grapher

__author__ = "Lance Jenkin"
__email__ = "lancejenkin@gmail.com"


class RapidController(QMainWindow, Ui_RapidAlphaWindow):
    # pyqtSignals
    startMeasurement = pyqtSignal()
    saveGraph = pyqtSignal("QString")
    exportData = pyqtSignal("QString")
    loadMeasurement = pyqtSignal("QString")
    saveMeasurement = pyqtSignal("QString")
    exit = pyqtSignal()

    def __init__(self, measurement_settings, audio_devices):
        """ Constructor for RapidController, sets up the view, signals and shows
            the window.

            :param measurement_settings:
                A dictionary containing the settings to used for the measurement.
            :type measurement_settings:
                dict
            :param audio_devices:
                A list of all the input / output devices available in the
                system.
            :type:
                array of AudioDevice
        """
        self.logger = logging.getLogger("Alpha")
        self.logger.debug("Creating RapidController")

        QMainWindow.__init__(self)

        self.measurement_settings = measurement_settings
        self.audio_devices = audio_devices
        self.grapher = Grapher(self.measurement_settings)

        self.setupUi(self)
        self._setupWidgets()
        self._setupSignals()

        self.showMaximized()

    def update(self):
        """ Updates the graph showing the absorption coefficient of the material
        measured.
        """
        self.logger.debug("Entering update")

        self.grapher.graphAbsorption(self.alpha.alpha, self.AlphaPlot)

    def _setupWidgets(self):
        """ Setup the widgets to show the user.

            For the rapid view, the input / output devices are populated, and
            the graph is formatted.
        """
        self.logger.debug("Entering _setupWidgets")

        # Populate the input / output devices
        for audio_device in self.audio_devices:
            name = audio_device.name
            index = audio_device.index
            if audio_device.input_channels > 0:
                self.InputDeviceList.addItem(name, index)
            if audio_device.output_channels > 0:
                self.OutputDeviceList.addItem(name, index)

        # Set the selected input and output device
        default_input_device = self.measurement_settings["input device"]
        default_output_device = self.measurement_settings["output device"]

        # Default to the first entries
        self.InputDeviceList.setCurrentIndex(0)
        self.OutputDeviceList.setCurrentIndex(0)

        # Update if available
        index = self.InputDeviceList.findData(default_input_device)
        self.InputDeviceList.setCurrentIndex(index)

        index = self.OutputDeviceList.findData(default_output_device)
        self.OutputDeviceList.setCurrentIndex(index)

        self.grapher.graphAbsorption([], self.AlphaPlot)

    def _updateMeasurementSettings(self):
        """ Update the Measurement Settings dictionary.

        For the Rapid View, the only settings that change are the input and
        output devices.
        """
        self.logger.debug("Entering _updateMeasurementSettings")

        selected_index = self.InputDeviceList.currentIndex()
        input_device = self.InputDeviceList.itemData(selected_index).toInt()
        self.measurement_settings["input device"] = input_device[0]

        selected_index = self.OutputDeviceList.currentIndex()
        output_device = self.OutputDeviceList.itemData(selected_index).toInt()
        self.measurement_settings["output device"] = output_device[0]

    def _setupSignals(self):
        """ Connects the various button signals to the class signals. """
        self.logger.debug("Entering _setupSignals")

        self.StartMesurement.clicked.connect(self.startMeasurement)
        self.Exit.clicked.connect(self.exit)

        save_func = self._showSaveDialog
        self.SaveGraph.clicked.connect(lambda: save_func("graph"))
        self.ExportData.clicked.connect(lambda: save_func("csv"))
        self.SaveMeasurement.clicked.connect(lambda: save_func("measurement"))

        load_func = self._showOpenDialog
        self.LoadMeasurement.clicked.connect(lambda: load_func("measurement"))

        update_func = self._updateMeasurementSettings
        self.OutputDeviceList.currentIndexChanged.connect(update_func)
        self.InputDeviceList.currentIndexChanged.connect(update_func)

    def _showOpenDialog(self, file_type):
        """ Shows the open dialog to get the filename to load the required data.

        :param file_type:
            The type of data to be saved, could be one of "graph", "csv",
            "measurement"
        :type file_type:
            str
        """
        self.logger.debug("Entering _showOpenDialog")

        if file_type == "measurement":
            caption = "Select Measurement File to Load"
            filter = "AlphaDb (*.db)"
            signal = self.loadMeasurement
        else:
            self.logger.debug("Invalid file_type passed: %s" % (file_type))
            return

        dir = "./"

        filename = QFileDialog.getOpenFileName(self, caption, dir, filter)
        # filename is a tuple (filename, selected filter) when file is selected
        # else a blank string if dialog closed
        print filename
        if filename != "":
            signal.emit(filename)

    def _showSaveDialog(self, file_type):
        """ Shows the save dialog to get the filename to save the required
            data to.

        :param file_type:
            The type of data to be saved, could be one of "graph", "csv",
            "measurement"
        :type file_type:
            str
        """
        self.logger.debug("Entering _showSaveDialog")

        if file_type == "graph":
            caption = "Select file to save the graph"
            filter = "PNG (*.png)"
            signal = self.saveGraph
        elif file_type == "csv":
            caption = "Select file to export data to"
            filter = "CSV (*.csv)"
            signal = self.exportData
        elif file_type == "measurement":
            caption = "Select file to save the measurement to"
            filter = "AlphaDb (*.db)"
            signal = self.saveMeasurement
        else:
            self.logger.debug("Invalid file_type passed: %s" % (file_type))
            return

        dir = "./"

        filename = QFileDialog.getSaveFileName(self, caption, dir, filter)

        if filename != "":
            signal.emit(filename)
