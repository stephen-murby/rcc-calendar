import csv
from datetime import datetime
from typing import List

from main.models import Tide, TideType


class TideLineParser:
    @staticmethod
    def parse_line(line: str) -> List[Tide]:
        # Split the line by the comma
        parts = next(csv.reader([line]))
        tides = []
        date_str = parts[0]
        # If the HW field is not empty, create a HIGH tide object
        if parts[1]:
            time_str = parts[1]
            datetime_str = f"{date_str} {time_str}"
            starting_at = datetime.strptime(f"{parts[0]} {parts[1]}", "%d/%m/%Y %H%M")
            height = float(parts[2])
            tide = Tide(TideType.HIGH, starting_at, height)
            tides.append(tide)
        # If the LW field is not empty, create a LOW tide object
        if parts[3]:
            time_str = parts[3]
            datetime_str = f"{date_str} {time_str}"
            starting_at = datetime.strptime(f"{parts[0]} {parts[3]}", "%d/%m/%Y %H%M")
            height = float(parts[4])
            tide = Tide(TideType.LOW, starting_at, height)
            tides.append(tide)
        # Return the list
        return tides