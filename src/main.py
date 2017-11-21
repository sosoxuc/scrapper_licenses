#!/usr/bin/env python3
from src.config import Config
from src.source import Source
from src.parser import Parser

if __name__ == '__main__':
    config = Config.get()
    schema = Config.read_schema()

    schema = Source(config, schema).get_all()
    result = Parser(config, schema).parse()
