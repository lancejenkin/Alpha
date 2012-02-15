#!/usr/bin/env python
""" Analyzes the recorded response and determines the absorption coefficient.
    
    Using Cepstral techniques to determine the absorption by taking the power 
    cepstrum of the microphone and generator signals.  The generator cepstrum
    can then be subtracted from the microphone cepstrum.  The impulse response
    of the material can then be directly 'lifted' of the power cepstrum.
"""

import logging
from scipy.signal import butter, lfilter
from numpy import *
from pylab import *
from MlsDb import MlsDb

__author__ = "Lance Jenkin"
__email__ = "lancejenkin@gmail.com"


class AbsorptionCoefficient(object):

    def __init__(self, microphone_signals, generator_signals, measurement_settings,
        analysis_settings):

        """ Constructor for AbsorptionCoefficient object.
        
        :param microphone_signals:
            An array of signals recorded from the microphone.
        :type microphone_signals:
            array of float
        :param generator_signals:
            An array of signals recorded directly from the generator.
        :type generator_signals:
            array of float
        :param measurement_settings:
            A dictionary containing the settings used to measure the signals.
            As well as the location of the impulse in the microphone signal and
            the generator signal.
        :type measurement_settings:
            dict
        :param analysis_settings:
            A dictionary containing the settings used to analyse the signals.
        :type analysis_settings:
            dict
        """
        self.logger = logging.getLogger("Alpha")
        self.logger.debug("Creating AbsorptionCoefficient Object")

        self.microphone_signals = microphone_signals
        self.generator_signals = generator_signals
        self.measurement_settings = measurement_settings
        self.analysis_settings = analysis_settings

        self.mls_db = MlsDb()
        
        self.determineAlpha()

    def determineAlpha(self):
        """ Determine the absorption coeffiecient of the material under test.
        
        The absorption coeffiecient is determined directly by lifting the 
        impulse response from the power cepstrum.  The power cepstrum is the 
        generator's power cepstrum subtracted from microphone's power cepstrum.
        The microphone and generator power cepstra are determined from the 
        averaged recorded microphone and generator response.  These averaged
        signals are filtered with an antialiasing filter, and decimated.  
        """
        self.logger.debug("Entering determineAlpha")

        # Extract the signals from the recorded responses, and average
        self._extractSignals()

        # If MLS signal, then utilize the circular convolution propery
        signal_type = self.measurement_settings["signal type"]

        if signal_type == "maximum length sequence":
            number_taps = int(self.measurement_settings["mls taps"])
            print len(self.average_microphone_response)
            self.microphone_response = self.mls_db.getSystemResponse(
                                        self.average_microphone_response, number_taps)
            
            self.generator_response = self.mls_db.getSystemResponse(
                                        self.average_generator_response, number_taps)
        else:
            self.microphone_response = self.average_microphone_response
            self.generator_response = self.average_generator_response
        
        # LPF the signals and decimate
        self._downsampleSignals()
        # Determine the Cepstrum
        self._determineCepstrum()

        # Lift the impulse response
        self._liftImpulseResponse()

        # Determine the absorption coefficient
        fft_size = int(self.measurement_settings["fft size"])
        self.alpha = 1 - abs(fft(self.impulse_response, fft_size)) ** 2
    
    def _extractSignals(self):
        """ Extract the microphone and generator signals from the raw signals.

        The microphone and generator signal are preceeded by an impulse.  The
        location of the impulse is given in the signal settings.  The delay 
        from the impulse to the start of the signal is also specified in the
        signal settings.  The microphone and generator can therefore be extracted 
        from the start of the signal.
        """
        self.logger.debug("Entering _extractSignals")

        sample_rate = float(self.measurement_settings["sample rate"])
        signal_type = str(self.measurement_settings["signal type"])
        impulse_location = int(self.measurement_settings["microphone impulse location"])
        impulse_signal_delay = float(self.measurement_settings["impulse delay"])

        impulse_signal_samples = impulse_signal_delay * sample_rate
        
        signal_start = impulse_location + impulse_signal_samples

        self.microphone_responses = []
        for signal in self.microphone_signals:
            self.microphone_responses.append(signal[signal_start:])
        self.average_microphone_response = average(self.microphone_responses, axis=0)

        impulse_location = int(self.measurement_settings["generator impulse location"])
        signal_start = impulse_location + impulse_signal_samples

        self.generator_responses = []
        for signal in self.generator_signals:
            self.generator_responses.append(array(signal[signal_start:]))
        self.average_generator_response = average(self.generator_responses,
                                                    axis=0)
        
        if signal_type == "maximum length sequence":
            mls_reps = int(self.measurement_settings["mls reps"])
            mls_taps = int(self.measurement_settings["mls taps"])
            assert(mls_reps > 0)

            mls_length = 2 ** mls_taps - 1
            mls_sig = self.average_microphone_response[mls_length:(
                                                mls_length * (mls_reps + 1))]
            mic_mls_array = reshape(mls_sig, (mls_reps, -1))
            self.average_microphone_response = average(mic_mls_array, axis=0)
            mls_sig = self.average_generator_response[mls_length:(
                                                mls_length * (mls_reps + 1))]
            mic_mls_array = reshape(mls_sig, (mls_reps, -1))
            self.average_generator_response = average(mic_mls_array, axis=0)

        
    def _downsampleSignals(self):
        """ Low pass filter microphone response and generator response, then down 
            sample by an Integer factor.

            The response signals is either the rawsignal, or if the MLS signal 
            was used to excite the system, the system response determined by
            the convolution property of MLS signals.
        """
        self.logger.debug("Entering _downsampleSignals")

        # Get required variables
        sample_rate = float(self.measurement_settings["sample rate"])
        decimation_factor = float(self.analysis_settings["decimation factor"])
        filter_cutoff = int(self.analysis_settings["antialiasing filter order"])

        # Low pass filter the response to prevent aliasing
        [b, a] = butter(filter_cutoff, 0.8 / decimation_factor, btype="low")

        self.microphone_response = lfilter(b, a, self.microphone_response)
        self.generator_response = lfilter(b, a, self.generator_response)


        # Down sample the responses
        self.microphone_response = self.microphone_response[::decimation_factor]
        self.generator_response = self.generator_response[::decimation_factor]

    def _liftImpulseResponse(self):
        """ Lift the impulse response off the power cepstrum.

        Using the specified window settings, create a window to lift the 
        impulse response off the power cepstrum.
        """
        self.logger.debug("Entering _liftImpulseResponse")

        # Get required variables
        window_type = str(self.analysis_settings["window type"])
        window_start = float(self.analysis_settings["window start"])
        window_end = float(self.analysis_settings["window end"])
        taper_length = float(self.analysis_settings["taper length"])
        sample_rate = float(self.measurement_settings["sample rate"])
        decimation_factor = int(self.analysis_settings["decimation factor"])

        effective_sample_rate = sample_rate / decimation_factor
        window_length = window_end - window_start
        window_samples = window_length * effective_sample_rate
        taper_samples = taper_length * effective_sample_rate

        # Create the window
        tapers = hanning(2 * taper_samples)
        if window_type == "one sided":
            self.window = r_[ones(window_samples - taper_samples), 
                        tapers[taper_samples:]]
        elif window_type == "two sided":
            self.window = r_[tapers[:taper_samples], 
                        ones (window_samples - (2 * taper_samples)),
                        tapers[taper_samples:]]
        
        # Lift impulse response
        start = window_start * effective_sample_rate
        end = start + len(self.window)

        self.impulse_response = self.power_cepstrum[start:end]
        self.impulse_response *= self.window


    def _determineCepstrum(self):
        """ Determines the power cepstra of the averaged microphone and 
            generator signals.
        
            The power cepstra is defined as:
                c(t) = ifft(log(abs(fft(x(t)) ** 2))
            
            "The inverse Fourier Transform of the logarithmic squared magnitude
            of the Fourier Transform of a signal"
        """
        self.logger.debug("Entering _determineCepstrum")
        fft_size = int(self.measurement_settings["fft size"])

        self.microphone_cepstrum = ifft(log(abs(fft(self.microphone_response, fft_size)) ** 2))
        self.generator_cepstrum = ifft(log(abs(fft(self.generator_response, fft_size)) ** 2))

        self.power_cepstrum = self.microphone_cepstrum - self.generator_cepstrum