# -*- coding: utf-8 -*-
"""
    Provides a custom unit test base class which will log to sentry.

    :copyright: (c) 2010 by Tim Sutton
    :license: GPLv3, see LICENSE for more details.
"""
import unittest
import logging
from app import osm_app as app
from flask_testing import LiveServerTestCase
from reporter import setup_logger

LOGGER = logging.getLogger('osm-reporter')


class LoggedTestCase(unittest.TestCase):
    """A test class for backend tests that logs to sentry on failure."""
    def failureException(self, msg):
        """Overloaded failure exception that will log to sentry.

        :param msg: String containing a message for the log entry.
        :type msg: str

        :returns: delegates to TestCase and returns the exception generated
            by it.
        :rtype: Exception

        See unittest.TestCase to see what gets raised.
        """
        LOGGER.exception(msg)
        return super(LoggedTestCase, self).failureException(msg)
