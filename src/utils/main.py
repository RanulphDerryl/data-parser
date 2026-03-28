from data_parser import config
from data_parser.parsers import CsvParser, JsonParser

def main():
    """Parse data from input files."""
    parser_type = input("Enter the type of parser (csv/json): ")
    parser = None

    if parser_type.lower() == "csv":
        parser = CsvParser()
    elif parser_type.lower() == "json":
        parser = JsonParser()
    else:
        print("Invalid parser type")
        return

    parser.parse_files(config.input_files)

if __name__ == "__main__":
    main()