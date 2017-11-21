#!/usr/bin/env nose2

import os
import unittest
from src.config import Config
from src.source import Source


class TestSource(unittest.TestCase):

    def test_file_save(self):
        url = 'ftp://dbprftp.state.fl.us/pub/llweb/certcomp.csv'
        file_name = url.split('/')[-1]
        ds.file_save(url, file_name)
        self.assertTrue(os.path.exists(os.path.join(config['download_path'], file_name)))


config = Config.get()
ds = Source(config)

if __name__ == '__main__':
    unittest.main()
