import os
import json
import logging
from data_parser import DataParser

class DataParser:
    def __init__(self, config_file):
        self.config_file = config_file
        self.logger = logging.getLogger(__name__)

    def load_config(self):
        with open(self.config_file, 'r') as f:
            return json.load(f)

    def parse_data(self):
        config = self.load_config()
        parser = DataParser(config)
        return parser.parse()

    def save_config(self, config):
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=4)

def main():
    parser = DataParser('data-parser.config')
    data = parser.parse_data()
    parser.save_config(data)

if __name__ == '__main__':
    main()