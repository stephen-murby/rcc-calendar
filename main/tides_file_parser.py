from typing import List
from models import Tides, Tide, TideType
from datetime import datetime

class TidesFileParser:
    @staticmethod
    def parse_tides(lines: List[str]) -> List[Tide]:
        # Each line in the input file is a tide event in the csv format: DATE,HW,HW_HT,LW,LW_HT
        # Remove the header line
        lines = lines[1:]
        # Create an empty list to store the data
        tides = []
        # Iterate over the lines
        for line in lines:
            # Split the line by the comma
            parts = line.split(',')
            date_str = parts[0]
            # If the HW field is not empty, create a HIGH tide object
            if parts[1]:
                time_str = parts[1]
                datetime_str = f"{date_str} {time_str}"
                starting_at = datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")
                height = float(parts[2])
                tide = Tide(TideType.HIGH, starting_at, height)
                tides.append(tide)
            # If the LW field is not empty, create a LOW tide object
            if parts[3]:
                time_str = parts[3]
                datetime_str = f"{date_str} {time_str}"
                time = datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")
                height = float(parts[4])
                tide = Tide(TideType.LOW, time, height)
                tides.append(tide)
        # Return the list
        return tides