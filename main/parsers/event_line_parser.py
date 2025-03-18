import csv
from datetime import datetime

from main.models import Event, EventType


class EventLineParser:

    @staticmethod
    def parse_line(line: str) -> Event:
        parts = next(csv.reader([line]))
        # Create a datetime object for the date and time
        # If all the required fields are not present, skip the line
        if parts[0] != "" and parts[1] != "" and parts[2] != "" and parts[3] != "":
            # Create an Event object
            starting_at = datetime.strptime(f"{parts[0]} {parts[3]}", "%d/%m/%Y %H:%M")
            event_type = EventType.of(parts[2])
            event_type_based_duration = EventType.default_duration(event_type)
            return Event(start_time=starting_at, title=parts[1], type=EventType.of(parts[2]), duration_hours=event_type_based_duration)
