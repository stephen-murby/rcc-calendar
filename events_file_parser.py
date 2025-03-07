from typing import List
from models import Event
from datetime import datetime

class EventsFileParser:
    @staticmethod
    def parse_events(lines: List[str]) -> List[Event]:
        # Each line in the input file is an event in the csv format: DATE,RCC_MEETINGS_AND_EVENTS,EVENT_TYPE,START_TIME
        # Remove the header line
        lines = lines[1:]
        # Create an empty list to store the data
        data = []
        # Iterate over the lines
        for line in lines:
            # Split the line by the comma
            parts = line.split(',')
            # Create a datetime object for the date and time
            date_str = parts[0]
            time_str = parts[3]
            datetime_str = f"{date_str} {time_str}"
            starting_at = datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")
            # Create an Event object
            event = Event(starting_at, parts[1], parts[2])
            data.append(event)
        # Return the list
        return data