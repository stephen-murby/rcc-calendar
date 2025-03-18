import icalendar

from models import Event, Tide, RCCYear
from typing import List
from main.parsers.tides_file_parser import TidesFileParser
from main.parsers.events_file_parser import EventsFileParser


class RccCalendar:

    def __init__(self):
        self.tide_files = []
        self.event_files = []
        self.year = RCCYear(months=[])

    def write_events_to_ics(self, file_name: str):
        ics_calendar = icalendar.Calendar()



    def write_tides_to_ics(self, file_name: str):
        pass

    def create(self):
        all_events: List[Event] = []
        all_tides: List[Tide] = []

        for file_handler in self.event_files:
            # Read in the file and store the data in a list of RccEventDay objects
            event_lines = read_file(file_handler)
            print(f'{len(event_lines)} lines read in from {file_handler}')
            events = EventsFileParser.parse_events(event_lines)
            print(f'{len(events)} events parsed from {file_handler}')
            all_events.extend(events)
            
        for file_handler in self.tide_files:
            # Read in the file and store the data in a list of RccEventDay objects
            tide_lines = read_file(file_handler)
            print(f'{len(tide_lines)} lines read in from {file_handler}')
            tides = TidesFileParser.parse_tides(tide_lines)
            print(f'{len(tides)} tides parsed from {file_handler}')
            all_tides.extend(tides)

        # Filter for events that have a start time and a title
        all_events = [event for event in all_events if event.start_time and event.title]


        # Print the first 5 events
        for e in all_events[:5]:
            print(e)

        # Print the first 5 tides
        for t in all_tides[:5]:
            print(t)

    def with_tides(self, file_path):
        self.tide_files.append(file_path)
        return self

    def with_events(self, file_path):
        self.event_files.append(file_path)
        return self

