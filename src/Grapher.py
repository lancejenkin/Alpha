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

    def graphImpulseResponse(self, impulse, plot_handler):
        """ Graph the impulse response of a system.  Creates a generic time
        domain plot, with the time given in milliseconds.

        :param impulse:
            The impulse response of the system.
        :type impulse:
            array
        :param plot_handler:
            The plot handler used to plot the data.
        :type plot_handler:
            matplotlib object
        """
        self.logger.debug("Entering graphImpulseResponse")

        # get parameters
        sample_rate = float(self.measurement_settings["sample rate"])

        t = arange(0, len(impulse) / sample_rate, 1 / sample_rate)

        # plot time in milliseconds
        plot_handler.axes.plot(t * 1000, impulse)
        plot_handler.axes.grid(color="grey", linestyle="--")
        plot_handler.draw()

    def graphFrequencyResponse(self, frequency, plot_handler):
        """ Graph the frequency response of the system,
        plots the frequency response, normalized to 0 dB, between frequencies
        20 to 10000 Hz.

        :param frequency:
            The frequency response of the system.
        :type frequency:
            array
        :param plot_handler:
            The plot handler used to plot the data.
        :type plot_handler:
            matplotlib object
        """
        self.logger.debug("Entering graphFrequencyResponse")

        # get paramaters
        sample_rate = float(self.measurement_settings["sample rate"])
        fft_size = int(self.measurement_settings["fft size"])

        # Plot frequency response
        freq = fftfreq(fft_size, 1 / sample_rate)

        if len(frequency) > 0:
            normalized_frequency = 20 * log10(frequency) - max(20 * log10(frequency))
            plot_handler.axes.semilogx(freq, normalized_frequency)
        else:
            data = zeros(fft_size)
            plot_handler.axes.semilogx(freq, data, lw=0)

        plot_handler.axes.set_xticks([16, 20, 25, 31.5, 40, 50, 63, 80, 100, 125,
            160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150,
            4000, 5000, 6300, 8000, 1000, 12500])
        plot_handler.axes.set_xticklabels([16, 20, 25, 31.5, 40, 50, 63, 80, 100, 125,
            160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150,
            4000, 5000, 6300, 8000, 1000, 12500])
        plot_handler.axes.set_xlim([20, 5000])
        plot_handler.axes.set_ylim([-50, 0])
        plot_handler.axes.grid(color="grey", linestyle="--")
        plot_handler.axes.set_xlabel("Frequency (Hz)")
        plot_handler.draw()


    def graphAbsorption(self, alpha, plot_handler):
        """ Graph the Absorption Coefficient of the material under measurement.

        :param alpha:
            The absorption coefficient for the material tested.
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
        plot_handler.axes.set_yticks(arange(0, 1.1, 0.1))
        plot_handler.axes.grid(color="grey", linestyle="--")
        plot_handler.axes.set_xlabel("Frequency (Hz)")
        plot_handler.axes.set_ylabel(r"Absorption Coefficient")
        plot_handler.draw()
