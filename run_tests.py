#!/usr/bin/env python

import os
import sys
import unittest

from tests.different_topics_test_case import DifferentTopicsTestCase
from tests.different_text_test_case import DifferentTextTestCase


source_dir = os.path.join(os.path.dirname(__file__), 'source')
sys.path.insert(0, source_dir)

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(DifferentTopicsTestCase),
        # unittest.makeSuite(DifferentTextTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
