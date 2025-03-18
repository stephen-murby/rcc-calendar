from typing import List

class Utils:

    @staticmethod
    def read_file(file_path) -> List[str]:
        # Open the file in read mode
        file_handler = open(file_path, 'r')
        # Read each line from the file handler
        lines = file_handler.readlines()
        # Remove the newline character from each line
        lines = [line.strip() for line in lines]
        return lines