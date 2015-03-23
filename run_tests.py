#!/usr/bin/env python2.7

import os
import socket
import sys
import unittest
from contextlib import contextmanager

source_dir = os.path.join(os.path.dirname(__file__), 'source')
sys.path.insert(0, source_dir)

from MainTestCase import MainTestCase

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(MainTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
