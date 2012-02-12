#!/usr/bin/env python
""" Provides methods for the Rapid Delegate Object.

The rapid delegate is used for the rapid measurement of a material.  It loads
the default settings to do the measurement, as well as to analyse the response.
"""

import logging

from BaseDelegate import BaseDelegate
from Views.RapidController import RapidController

__author__ = "Lance Jenkin"
__email__ = "lancejenkin@gmail.com"

class RapidDelegate(BaseDelegate):

    def __init__(self):
        """ Constructor for RapidDelegate """
        super(BaseDelegate, self).__init__()
        self.logger = logging.getLogger("Alpha")
        self.logger.debug("Creating RapidDelegate")
        
        self.window = RapidController(self.measurement_settings, 
                                    self.audio_devices)
                                    