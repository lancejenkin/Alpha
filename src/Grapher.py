#!/usr/bin/env python
""" Provides an interface to create various graphs. """

import logging

from pylab import *
from matplotlib.ticker import MultipleLocator

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
        normalized_impulse = impulse / max(impulse)
        plot_handler.axes.plot(t * 1000, normalized_impulse)
        y_minorLocator = MultipleLocator(0.1)
        x_minorLocator = MultipleLocator(1)
        plot_handler.axes.yaxis.set_minor_locator(y_minorLocator)
        plot_handler.axes.xaxis.set_minor_locator(x_minorLocator)
        plot_handler.axes.yaxis.grid(True, which='minor', color="grey", linestyle="--")
        plot_handler.axes.xaxis.grid(True, which='minor', color="grey", linestyle="--")

        plot_handler.axes.yaxis.grid(True, which='major', color="grey", linestyle="-")
        plot_handler.axes.xaxis.grid(True, which='major', color="grey", linestyle="-")
        plot_handler.axes.set_ylim(top=1.1)
        plot_handler.axes.set_xlabel("Time (ms)")
        plot_handler.axes.set_ylabel("Amplitude")
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
            # make the level at 1000 Hz = 0
            #bin1000 = int(1000 * fft_size / (sample_rate))
            #normalized_frequency = 20 * log10(frequency) - 20 * log10(frequency[bin1000])
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
        plot_handler.axes.set_yticks(arange(-50, 1, 5))
        plot_handler.axes.set_yticklabels(arange(-50, 1, 5))
        plot_handler.axes.set_xlim([20, 5000])
        plot_handler.axes.set_ylim([-50, 0])
        plot_handler.axes.grid(color="grey", linestyle="--")
        plot_handler.axes.set_xlabel("Frequency (Hz)")
        plot_handler.axes.set_ylabel("$L_P (dB)$")
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
            plot_handler.axes.hold(True)
            freq = fftfreq(len(alpha), 1 / sample_rate)
            plot_handler.axes.semilogx(freq, alpha)
            data = [0.030265443, 0.035447682, 0.047655763, 0.026164963, 0.187046493, 
                0.390593132,0.362845495,0.685562058,0.528042171,0.334144,0.289366757,
                0.354272959,0.473338776,0.256837099, 0.550658133]
            freq = [100, 125, 160, 200, 250, 300, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000]
            plot_handler.axes.semilogx(freq, data, "x")
            plot_handler.axes.hold(False)
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
