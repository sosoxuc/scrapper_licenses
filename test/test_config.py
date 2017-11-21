#!/usr/bin/env nose2

import unittest
from src.config import Config


class TestConfig(unittest.TestCase):

    def test_config(self):
        schema = Config.read_schema()
        self.assertEqual(schema[0]['link to data'], 'ftp://dbprftp.state.fl.us/pub/llweb/certcomp.csv')
        self.assertEqual(schema[-1]['link to data'], 'ftp://dbprftp.state.fl.us/pub/llweb/swimpool_exam.csv')


if __name__ == '__main__':
    unittest.main()
