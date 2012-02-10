#!/usr/bin/env python
""" Provides a means to preform a measurement.  Uses Signal Generate to
    generate a signal, and the Audio Interface to play the signal and record
    the reponse.
"""
import logging

from AudioIO import AudioIO
from SignalGenerator import SignalGenerator

__author__ = "Lance Jenkin"
__email__ = "lancejenkin@gmail.com"


class Measurement(object):

    def __init__(self, measurement_settings):
        """ Constructor for Measurement object.

        :param measurement_settings:
            A dictionary with the measurements settings to create use to create
            the signal.
        :type measurement_settings:
            dict
        """
        self.logger = logging.getLogger("Alpha")
        self.logger.debug("Creating Measurement Object")

        self.measurement_settings = measurement_settings

        self._setupAudio()

    def startMeasurement(self):
        """ Start the actual measurement.

            Start a measurement, by getting the signal from the signal
            generator, passing the signal to the sound card and recieving the
            response. It then preforms the initial analysis on the signals, to
            split up the long response into the seperate signals, and locate
            the start of the signal.
        """
        self.logger.debug("Entering startMeasurement")

        signal_gen = SignalGenerator(self.measurement_settings)

        signal = signal_gen.signal

        (left_channel, right_channel) = self.audio.playbackAndRecord(signal)

        self.input_response = left_channel
        self.generator_response = right_channel

    def _initialAnalysis(self):
        """ Preform the initial analysis on the received response.

        Split the received response into the seperate signals.  It then locates
        the start of the signals by locating the impulse.
        """
        self.logger.debug("Entering _initialAnalysis")

        # Get required parameters
        signal_reps = int(self.measurement_settings["signal reps"])

        self.input_signals = reshape(self.input_response, (signal_reps, -1))
        self.generator_signals = reshape(self.generator_response,
                                        (signal_reps, -1))

        # Since all signals should be located in the same place, only need to
        # locate the impulse in the first signal.
        input_signal = input_signals[0]
        generator_signal = generator_signals[0]

        input_impulse_loc = self.locateSignalImpulse(input_signal)
        generator_impulse_loc = self.locateGeneratorImpulse(generator_signal)

        self.measurement_settings["input impulse location"] = (
            input_impulse_loc)
        self.measurement_settings["generator impulse location"] = (
            generator_impulse_loc)

    def locateSignalImpulse(self, signal):
        """ Locates the synchronization impulse in the microphone response.

        Finding the synchronization impulse in the microphone is complicated
        by; the relatively low SNR as compared to the generator response and
        the distorting effects on the impulse that the loudspeaker, fibre glass
        plug and sound propagating in a tube has on the impulse.  Instead of
        using a simple threshold, instead the first N samples of the signal are
        assumed not to have any signal in them and consit of only noise. The
        maximum value is then taken as the peak noise level, and the impulse
        is determined to be in the sample that is T times the peak noise level.
        """
        self.logger.debug("Entering locateSignalImpulse")

        noise_samples = self.measurement_settings["noise samples"]
        impulse_constant = self.measurement_settings["impulse constant"]

        # Differentiate the signal
        d_signal = r_[0, (signal[1:] - signal[:-1])]

        # Determine noise level
        peak_noise_lvl = max(abs(d_signal[:noise_samples]))

        for sample_index, sample in enumerate(d_signal):
            if abs(sample) > noise_level * IMPULSE_THRESHOLD_CONSTANT:
                self.logger.debug("Impulse found at %s" % (sample_index))
                return sample_index

        self.logger.debug("Impulse not found")
        return -1

    def locateGeneratorImpulse(self, signal):
        """ Locates the synchronization impulse in the generator response.

        Due to the high SNR of the generator signal, a simple threshold
        algorithm suffices to find the synchronization impulse in the generator
        signal. It should be noted, preringing occurs due to the out of phase
        response of the bandlimiting filters in the AD and DA parts of the
        soundcard.  The ringing has a frequency of Fs / 2, and can be removed
        by phase shifting the signal using the Hilbert transform.  This will
        help in locating the impulse.

        :param signal:
            The generator signal captured.
        :type signal:
            array of float

        :returns:
            int - The start index of the impulse
        """

        self.logger.debug("Entering locate_generator_impulse")

        threshold = self.measurement_settings["impulse threshold"]
        # Get the envolope of the signal, removing the pre-ringing
        signal = abs(hilbert(signal))

        # Differentiate the signal
        d_signal = r_[0, (signal[1:] - signal[:-1])]

        for sample_index, sample in enumerate(d_signal):
            if sample > threshold:
                self.logger.debug("Impulse found at %s" % (sample_index))
                return sample_index

        self.logger.debug("Impulse not found!")
        return -1

    def _setupAudio(self):
        """ Setup the audio device """
        self.logger.debug("Entering _setupAudio")

        sample_rate = self.measurement_settings["sample rate"]

        self.audio = AudioIO(sample_rate)

        input_device = self.measurement_settings["input device"]
        output_device = self.measurement_settings["output device"]
        self.audio.setInputDevice(input_device)
        self.audio.setOutputDevice(output_device)
