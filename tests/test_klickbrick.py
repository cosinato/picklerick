# test_picklerick

import os
import unittest
from picklerick import __version__

targetProgram = 'picklerick.py'


class TestPicklerickery(unittest.TestCase):

    def test_version(self):
        assert __version__ == '0.1.0'

    def test_program_exists(self):
        assert os.path.isfile(targetProgram)
