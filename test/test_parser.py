#!/usr/bin/env nose2

import unittest
from src.config import Config
from src.parser import Parser
import os


class TestParser(unittest.TestCase):

    def test_parser(self):
        config = Config.get()
        schema = Config.read_schema()

        for item in schema:

            file_name = item['link to data'].split('/')[-1]
            file_path = os.path.join(config['download_path'], file_name)

            if file_path.endswith('.xls'):
                file_path = file_path.replace('.xls', '.csv')
            item['file_path'] = file_path

        result = Parser(config, schema).parse()
        print(result)


if __name__ == '__main__':
    unittest.main()