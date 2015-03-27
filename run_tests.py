#!/usr/bin/env python

import os
import sys
import unittest

source_dir = os.path.join(os.path.dirname(__file__), 'source')
sys.path.insert(0, source_dir)

from tests.create_topic_test_case import CreateTopicTestCase

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(CreateTopicTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
