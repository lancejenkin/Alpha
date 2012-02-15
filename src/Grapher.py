#!/usr/bin/env python
""" Provides an interface to create various graphs. """

import logging

from pylab import *

__author__ = "Lance Jenkin"
__email__ = "lancejenkin@gmail.com"


class Grapher(object):

    def __init__(self, measurement_settings):
        """ Constructor for the Grapher Object. 

        :param measurement_settings:
            The settings used for the measurement.
        :type measurement_settings:
            dict
        """
        self.logger = logging.getLogger("Alpha")
        self.logger.debug("Creating Grapher Object")

        self.measurement_settings = measurement_settings
    
    def graphAbsorption(self, alpha, plot_handler):
        """ Graph the Absorption Coefficient of the material under measurement.

        :param alpha:
            The absorption coefficent for the material tested.
        :type alpha:
            array
        :param plot_handler:
            The plot handler to plot the data on.
        :type plot_handler:
            matplotlib object
        """
        self.logger.debug("Entering graphAbsorption")

        # Get Parameters
        fft_size = int(self.measurement_settings["fft size"])
        sample_rate = float(self.measurement_settings["sample rate"])
        if "decimation factor" in self.measurement_settings:
            decimate = float(self.measurement_settings["decimation factor"])
            sample_rate = sample_rate / decimate

        if len(alpha) > 0:
            freq = fftfreq(len(alpha), 1 / sample_rate)
            plot_handler.axes.semilogx(freq, alpha)
        else:
            freq = fftfreq(fft_size, 1 / sample_rate)
            data = zeros(fft_size)
            plot_handler.axes.semilogx(freq, data, lw=0)

        plot_handler.axes.set_xlim([100, 2100])
        plot_handler.axes.set_xticks([100, 125, 160, 200, 250, 315, 400, 
                                     500, 630, 800, 1000, 1250, 1600, 2000])
        plot_handler.axes.set_xticklabels([100, 125, 160, 200, 250, 315, 400, 
                                     500, 630, 800, 1000, 1250, 1600, 2000])
        plot_handler.axes.set_ylim([0, 1])
        plot_handler.axes.set_yticks(arange(0,1.1,0.1))
        plot_handler.axes.grid(color="grey", linestyle="--")
        plot_handler.draw()
    