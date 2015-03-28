#!/usr/bin/env python

import os
import sys
import unittest

source_dir = os.path.join(os.path.dirname(__file__), 'source')
sys.path.insert(0, source_dir)

from tests.different_topics_test_case import DifferentTopicsTestCase

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(DifferentTopicsTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
