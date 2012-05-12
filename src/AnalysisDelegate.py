#!/usr/bin/env python
""" Provides the controller for the Analysis Delegate

The Analysis Delegate is used for creating statistical analysis of using the
cepstral technique to measure the absorption coefficient of materials.

All figures used in the write up are generated in the Analysis Delegate
"""

import logging
from pylab import *
from scipy.fftpack import hilbert
import tempfile


from AudioIO import AudioIO
from BaseDelegate import BaseDelegate
from Grapher import Grapher
from MlsDb import MlsDb

__author__ = "Lance Jenkin"
__email__ = "lancejenkin@gmail.com"


class AnalysisDelegate(BaseDelegate):

    def __init__(self):
        BaseDelegate.__init__(self)
        self.logger = logging.getLogger("Alpha")
        self.logger.debug("Creating AnalysisDelegate")

    def responseAnalysis(self):
        """ Method to analyse responses """
        self.logger.debug("Entering responseAnalysis")

        measurement_file = "../test data/120301_asphalt.db"

        alpha = self.loadAbsorptionCoefficient(measurement_file)

        gen_signal = alpha.generator_signals[0]
        mic_signal = alpha.microphone_signals[0]

        plot(alpha.generator_cepstrum)

        show()

    def analysisImpulseResponse(self):
        """ Record the impulse response from the loudspeaker. """
        self.measurement_settings["output device"] = 2
        self.measurement_settings["input device"] = 3

        measurement_filename = "../test data/120309_impulse_test.db"

        measurement = self.newMeasurement(self.measurement_settings)
        self.saveMeasurement(measurement, measurement_filename)
        alpha = self.loadAbsorptionCoefficient(measurement_filename)

        plot(left)
        show()

    def filterTest(self):
        """ Test various filter cut off and orders and the effects on the absorption
        coefficient. """
        self.logger.debug("Entering filterTest")

        lpf_order_tests = [1, 3, 4, 5]
        lpf_cutoff_tests = [3000, 3500, 4000, 4500]

        self.measurement_settings["signal reps"] = 3
        self.measurement_settings["output device"] = 2
        self.measurement_settings["input device"] = 3
        for lpf_order in lpf_order_tests:
                for lpf_cutoff in lpf_cutoff_tests:
                        print "Testing LPF Order %s with cut off of %s" % (lpf_order, lpf_cutoff)
                        self.measurement_settings["lpf order"] = lpf_order
                        self.measurement_settings["lpf cutoff"] = lpf_cutoff

                        measurement = self.newMeasurement(self.measurement_settings)
                        measurement_filename = "../test data/120305_lpf_%s_%s.db" % (lpf_cutoff, lpf_order)
                        self.saveMeasurement(measurement, measurement_filename)
    
    def hpFilterTest(self):
        """ Test various high pass filter cut off and orders and the effects on the absorption
        coefficient. """
        self.logger.debug("Entering hpFilterTest")

        hpf_order_tests = [1, 3, 4, 5]
        hpf_cutoff_tests = [100, 150, 200, 500, 1000]

        self.measurement_settings["signal reps"] = 3
        self.measurement_settings["output device"] = 2
        self.measurement_settings["input device"] = 3
        for hpf_order in hpf_order_tests:
                for hpf_cutoff in hpf_cutoff_tests:
                        print "Testing HPF Order %s with cut off of %s" % (hpf_order, hpf_cutoff)
                        self.measurement_settings["hpf order"] = hpf_order
                        self.measurement_settings["hpf cutoff"] = hpf_cutoff
                        self.measurement_settings["hpf enable"] = 1

                        measurement = self.newMeasurement(self.measurement_settings)
                        measurement_filename = "../test data/120323_hpf_%s_%s.db" % (hpf_order, hpf_cutoff)
                        self.saveMeasurement(measurement, measurement_filename)
    def showFilterTests(self):
        """" plot the absorption coefficient of the various tests done with
        different filter orders """
        self.logger.debug("Entering showFilterTests")

        hpf_order_tests = [1, 3, 4, 5]
        hpf_cutoff_tests = [100, 150, 200, 500, 1000]

        fig = figure()
        for order_index, hpf_order in enumerate(hpf_order_tests):
                for cutoff_index, hpf_cutoff in enumerate(hpf_cutoff_tests):
                        measurement_filename = "../test data/120323_hpf_%s_%s.db" % (hpf_order, hpf_cutoff)
                        alpha = self.loadAbsorptionCoefficient(measurement_filename)
                        grapher = Grapher(alpha.measurement_settings)
                        
                        handler = Object()
                        handler.axes = fig.add_subplot(len(hpf_order_tests), len(hpf_cutoff_tests), order_index * len(hpf_cutoff_tests) + cutoff_index)
                        handler.draw = draw
                        grapher.graphAbsorption(alpha.alpha, handler)
                        plot(alpha.alpha)
                        title("%s Hz order %s" % (hpf_cutoff, hpf_order))

        show()


    def misidentificationAnalysis(self):
        """ Preform analysis on misidentifying the synchronization
        impulse """
        self.logger.debug("Entering misidentificationAnalysis")

        measurement_file = "../test data/120426_asphalt.db"

        alpha = self.loadAbsorptionCoefficient(measurement_file)
        grapher = Grapher(alpha.measurement_settings)

        fig = figure(figsize=(7, 5))

        mic_impulse_loc = int(alpha.measurement_settings["microphone impulse location"])
        gen_impulse_loc = int(alpha.measurement_settings["generator impulse location"])

        (gen_start, gen_end) = (gen_impulse_loc - 20, gen_impulse_loc + 20)
        (mic_start, mic_end) = (mic_impulse_loc - 20, mic_impulse_loc + 100)
        gen_signal = alpha.generator_signals[0][gen_start:gen_end]
        mic_signal = alpha.microphone_signals[0][mic_start:mic_end]
        ax = fig.add_subplot(211)
        ax.plot(gen_signal)
        ax.axvline(x=gen_impulse_loc - gen_start, color="black", linestyle="--", lw=1)
        ax = fig.add_subplot(212)
        ax.plot(mic_signal)
        ax.axvline(x=mic_impulse_loc - mic_start, color="black", linestyle="--", lw=1)
        show()

        fig = figure(figsize=(7, 5))
        ax = fig.add_subplot(111)
        resp = abs(fft(alpha.microphone_signals[0])) ** 2
        ax.plot(alpha.generator_cepstrum)
        ax.plot(alpha.microphone_cepstrum)
        ax.plot(alpha.power_cepstrum)
        show()
        fig = figure(figsize=(7, 5))
        handler = Object()
        handler.axes = fig.add_subplot(111)
        handler.draw = draw
        grapher.graphAbsorption(alpha.alpha, handler)
        show()

        alpha.measurement_settings["microphone impulse location"] = mic_impulse_loc + 0
        alpha.measurement_settings["generator impulse location"] = gen_impulse_loc - 2

        alpha.determineAlpha()
        fig = figure(figsize=(7, 5))
        ax = fig.add_subplot(111)
        ax.plot(alpha.generator_cepstrum)
        ax.plot(alpha.microphone_cepstrum)
        show()
        fig = figure(figsize=(7, 5))
        handler = Object()
        handler.axes = fig.add_subplot(111)
        handler.draw = draw
        grapher.graphAbsorption(alpha.alpha, handler)
        show()
        

    def synchronizeAnalysis(self):
        """ Method to analyse the synchronization of recieved responses. """
        self.logger.debug("Entering synchronizeAnalysis")

        measurement_file = "../test data/120215_asphalt.db"

        alpha = self.loadAbsorptionCoefficient(measurement_file)

        sample_rate = 44100.0

        gen_signal = alpha.generator_signals[0]
        mic_signal = alpha.microphone_signals[0]

        # Show Generator Impulse
        generator_impulse = gen_signal[19375:19450]

        fig = figure()
        ax = fig.add_subplot(111)
        ax.axhline(y=0, linestyle="-", color="black", linewidth=1)
        ax.plot(generator_impulse)
        ax.set_xlabel("Samples")
        ax.set_ylabel("Amplitude")
        ax.text(26, 0.22, "pre-ringing", ha="center", va="bottom", size=10)
        ax.annotate("", xy=(19, 0), xycoords="data", xytext=(26, 0.2),
                    arrowprops=dict(arrowstyle="->"))
        ax.annotate("", xy=(33, 0.08), xycoords="data", xytext=(26, 0.2),
                    arrowprops=dict(arrowstyle="->"))

        peak_y = max(generator_impulse)
        peak_x = where(generator_impulse == peak_y)[0][0]

        ax.annotate("(%d, %.2f)" % (peak_x, peak_y), xy=(peak_x, peak_y),
                    xycoords="data", xytext=(peak_x + 2, peak_y + 0.1),
                    arrowprops=dict(arrowstyle="->"))
        line = Line2D([19, 19], [0, 0.2], color="black", linestyle="--", lw=1)
        ax.add_line(line)
        line = Line2D([33, 33], [0, 0.2], color="black", linestyle="--", lw=1)
        ax.add_line(line)

        ax.set_xlim([0, 70])
        ax.yaxis.set_label_coords(-0.1, 0.5)
        savefig("Analysis/Images/generator_impulse_with_preringing.eps")
        # Show Generator Impulse with a Phase Shift
        cla()
        generator_impulse = hilbert(generator_impulse)
        ax = fig.add_subplot(111)
        ax.axhline(y=0, linestyle="-", color="black", linewidth=1)
        ax.plot(generator_impulse)
        ax.set_xlabel("Samples")
        ax.set_ylabel("Amplitude")

        peak_y = max(generator_impulse)
        peak_x = where(generator_impulse == peak_y)[0][0]

        ax.annotate("(%d, %.2f)" % (peak_x, peak_y), xy=(peak_x, peak_y),
                    xycoords="data", xytext=(peak_x + 2, peak_y + 0.1),
                    arrowprops=dict(arrowstyle="->"))
        ax.set_xlim([0, 70])
        ax.yaxis.set_label_coords(-0.1, 0.5)
        savefig("Analysis/Images/generator_impulse_phase_shifted.eps")

        # Show the Microphone Impulse Response
        mic_impulse = mic_signal[19470:20427]

        cla()
        ax.axhline(y=0, linestyle="-", color="black", linewidth=1)
        ax = fig.add_subplot(111)
        ax.plot(mic_impulse)

        ax.text(50, 0.01, "onset", ha="center", size=10)
        ax.annotate("", xy=(73, 0),
                    xycoords="data", xytext=(50, 0.01),
                    arrowprops=dict(arrowstyle="->"))
        ax.text(70, -0.019, "19 samples", ha="right", va="bottom", size=10)
        ax.annotate("", xy=(92, -0.02), xycoords="data", xytext=(115, -0.02),
                    arrowprops=dict(arrowstyle="->"))
        ax.annotate("", xy=(73, -0.02), xycoords="data", xytext=(50, -0.02),
                    arrowprops=dict(arrowstyle="->"))

        line = Line2D([73, 73], [0, -0.035], color="black", linestyle="--",
                        lw=1)
        ax.add_line(line)
        line = Line2D([92, 92], [0, -0.035], color="black", linestyle="--",
                        lw=1)
        ax.add_line(line)

        ax.set_xlim([0, 300])
        ax.set_xlabel("Samples")
        ax.set_ylabel("Amplitude")
        ax.yaxis.set_label_coords(-0.1, 0.5)
        ax.yaxis.set_ticks(arange(-0.04, 0.04, 0.02))
        savefig("Analysis/Images/microphone_impulse.eps")

        # Plot the Difference Microphone Response
        mic_impulse = abs((mic_impulse[1:] - mic_impulse[:-1]))
        d_mic = mic_signal[1:] - mic_signal[:-1]
        mic_noise = d_mic[abs(d_mic) > 0][:1000]
        max_noise = max(abs(mic_noise))
        std_noise = std(abs(mic_noise))

        mic_threshold = max_noise + 2.5 * std_noise
        onset = where(mic_impulse > mic_threshold)[0][0] - 1
        print onset
        cla()
        ax.axhline(y=0, linestyle="-", color="black", linewidth=1)
        ax.axhline(y=mic_threshold, linestyle="--", color="black", lw=1)
        ax.axvline(x=onset, linestyle="-.", color="grey", lw=1)
        ax = fig.add_subplot(111)
        ax.plot(mic_impulse)
        ax.set_xlim([0, 300])
        ax.text(30, 0.001, "onset at 73", ha="center", size=10)
        ax.annotate("", xy=(73, mic_impulse[onset]),
                    xycoords="data", xytext=(30, 0.001),
                    arrowprops=dict(arrowstyle="->"))
        ax.text(30, mic_threshold + 0.0001, "threshold", ha="center", size=10)
        xlabel("Samples")
        ylabel("Amplitude")
        ax.yaxis.set_label_coords(-0.1, 0.5)
        ax.yaxis.set_ticks(arange(0, 0.008, 0.002))
        savefig("Analysis/Images/onset_detection.eps")

        # Extreme Value Distribution
        from scipy.stats import norm
        from scipy.special import erf, erfc, erfcinv
        cla()
        icdf = lambda x: sqrt(2) * erf(2 * x - 1)

        n = 10
        alpha = icdf(1 - 1 / (n * exp(1)))
        beta = icdf(1 - 1 / n)

        x = arange(-10, 30, 0.1)
        evd = (1 / beta) * exp(-(x - alpha) / beta) * exp(-exp(-(x - alpha) / beta))
        plot(x, evd)
        xlabel("Maximum Value")
        ylabel("Probability")
        savefig("Analysis/Images/extreme_value_distribution.eps")
        # Mean Extreme Value
        cla()

        gamma = 0.57721566490153286060651209008240243104215933593992
        M = lambda n: sqrt(2) * ((-1 + gamma) * (erfcinv(2 - 2 / float(n))) - gamma * erfcinv(2 - 2 / (n * exp(1))))
        n = range(2, 1000)
        mean_max = [M(_) for _ in n]
        plot(n, mean_max)
        xlabel("Samples")
        ylabel("Expected Maximum Value")
        savefig("Analysis/Images/expected_maximum_value.eps")

        cla()
        eps = finfo(float).eps
        N = 1000
        multiplier = arange(0, 5, 0.1)
        samples = ((1 - norm.cdf(M(N) + multiplier)) ** -1) / 44100.0

        semilogy(multiplier, samples)

        samples_1 = ((1 - norm.cdf(M(N) + 1)) ** -1) / 44100.0
        samples_25 = ((1 - norm.cdf(M(N) + 2.5)) ** -1) / 44100.0

        line = Line2D([1, 1], [eps, samples_1], color="black", linestyle="-.", lw=1)
        ax.add_line(line)
        line = Line2D([0, 1], [samples_1, samples_1], color="black", linestyle="-.",
                        lw=1)
        ax.add_line(line)
        ax.text(0.5, samples_1 + 1, "39 seconds", ha="center", va="bottom", size=10)

        line = Line2D([2.5, 2.5], [eps, samples_25], color="black", linestyle="-.", lw=1)
        ax.add_line(line)
        line = Line2D([0, 2.5], [samples_25, samples_25], color="black", linestyle="-.",
                        lw=1)
        ax.add_line(line)
        ax.text(1.25, samples_25 + 5000, "62 hours", ha="center", va="bottom", size=10)

        xlabel("Multiplier")
        ylabel("Seconds")
        savefig("Analysis/Images/maximum_value_probability_multiplier.eps")

    def lowpassSweptSineGeneration(self):
        """ Function to illustrate the steps taken to generate a low pass swept sine.

        Instread of using the Signal Generator, preform the inverse filtering manually
        so that the steps may be illustrated.
        """
        from scipy.signal import butter, lfilter, filtfilt

        self.logger.debug("Entering lowpassSweptSineGeneration")

        T = 125 * 10 ** -3  # 100 ms
        sample_rate = 14e3
        f_1 = 6400
        fft_size = 2 ** 10

        # Generate time vector
        t = arange(0, T, 1 / sample_rate)
        print len(t)
        # Generate the signal from 0 to Nyquist frequency
        a = pi * f_1 / T

        s = sin(a * t ** 2)

        plot(1000 * t, s)
        xlabel("time (ms)")
        ylabel(r"$s(t)$")
        show()
        # Determine the spectrum
        S = fft(s, fft_size)
        # Inverse of the magnitude spectrum
        iaS = abs(S) ** -1
        liaS = log(iaS)
        liaS -= min(liaS)

        plot(fftfreq(fft_size, 1 / sample_rate)[:fft_size / 2], liaS[:fft_size / 2])
        xlabel("Frequency (Hz)")
        ylabel(r"ln$| S(\omega) | ^ {-1}$")
        show()
        # c, similiar to the cepstrum, is the inverse of the logarithmic inverse
        # magnitude spectrum
        c = ifft(log(iaS))

        # Window c to produce m
        m = r_[c[0], 2 * c[1:len(S) / 2 - 1], c[len(S) / 2], zeros(len(S) / 2)]

        # Determine the spectrum of the windowed 'cepstrum'
        M = fft(m, fft_size)

        # Determine the minimum phase inverse filter
        iSmp = exp(M)

        # Determine the minimum phase spectrum
        Smp = S * iSmp

        # Determin the minimum phase signal
        smp = ifft(Smp)

        # smp will have fft_size samples, which could be very long
        # reduce to length of the signal specified
        smp = smp[:len(t)]

         # Low pass filter the signal to the upper frequency
        [b, a] = butter(8, f_1 / (sample_rate / 2), btype="low")
        smp = filtfilt(b, a, smp)

        # Normalize so that the maximum value is 1
        smp /= max(abs(smp))

        signal = smp

    def windowAnalysis(self):
        """ Function to preform some analysis on various windows used
        to lift the impulse response from the cepstrum.

        """
        self.logger.debug("Entering windowAnalysis")
        N = 2 ** 10
        L = 2 ** 6

        rect = ones(L)
        hann = hanning(L)
        hamm = hamming(L)

        tmp_hann = hanning(20)
        mine = r_[tmp_hann[:10], ones(L - 20), tmp_hann[-10:]]
        RECT = fft(rect, N)
        HANN = fft(hann, N)
        HAMM = fft(hamm, N)
        MINE = fft(mine, N)

        plot(fftfreq(N), 20 * log10(abs(RECT)), label="rect")
        plot(fftfreq(N), 20 * log10(abs(HANN)), label="hanning")
        plot(fftfreq(N), 20 * log10(abs(HAMM)), label="hamming")
        plot(fftfreq(N), 20 * log10(abs(MINE)), label="flat-top")

        legend()
        show()

    def sweptSineTesting(self):
        """ Test some techniques to use with swept sine signals """
        self.logger.debug("Entering sweptSineTesting")

    def resonatorExample(self):
        """ Method to draw the example of the resonator's absorption coefficient
         and the significance of the paramaters.
         """
        self.logger.debug("Entering resonatorExample")

        B = 500.0
        f_0 = 1000.0
        a = 0.8
        H_gen = lambda f: sqrt(a / (1 + ((f - f_0) ** 2) / (B / 2) ** 2))
        f = arange(1, 10000)

        semilogx(f, 1 - (H_gen(f)) ** 2)
        ylim([0, 1])
        show()
class Object(object):
    pass

if __name__ == "__main__":
    logger = logging.getLogger("Alpha")
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)

    analysis = AnalysisDelegate()
    analysis.misidentificationAnalysis()
    #analysis.synchronizeAnalysis()
