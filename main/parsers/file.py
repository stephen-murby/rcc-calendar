from typing import List


class File:
    def __init__(self, path):
        self.path = path

    def read_lines(self) -> List[str]:
        with open(self.path) as f:
            return f.readlines()