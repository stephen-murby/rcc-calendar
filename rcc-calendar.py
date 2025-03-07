from rcc_event_day import RccEventDay
from models import Tides, Event, Tide
from typing import List
from datetime import datetime
from tides_file_parser import TidesFileParser
from events_file_parser import EventsFileParser


class RccCalendar:
    def __init__(self):
        self.tide_files = []
        self.event_files = []

    def create(self):
        all_events = []
        all_tides = []
        
        for file_handler in self.event_files:
            # Read in the file and store the data in a list of RccEventDay objects
            event_lines = read_file(file_handler)
            events = EventsFileParser.parse_events(event_lines)
            all_events.extend(events)
            
        for file_handler in self.all_tides:
            # Read in the file and store the data in a list of RccEventDay objects
            tide_lines = read_file(file_handler)
            tides = TidesFileParser.parse_tides(tide_lines)
            all_tides.extend(tides)

        # Filter for RccEventDay objects that have a start time and rcc_meetings_and_events
        all_events = [event for event in all_events if event.start_time and event.rcc_meetings_and_events]

        # Print the first 5 events
        for event in all_events[:5]:
            print(event)

    def withTides(self, file_path):
        self.tide_files.append(file_path)
        return self

    def withEvents(self, file_path):
        self.event_files.append(file_path)
        return self

def read_file(file_path) -> List[str]:
    # Open the file in read mode
    file_handler = open(file_path, 'r')
    # Read each line from the file handler
    lines = file_handler.readlines()
    # Remove the newline character from each line
    lines = [line.strip() for line in lines]
    return lines


if __name__ == '__main__':
    calendar = RccCalendar() \
        .withTides('./data/march_tides.csv') \
        .withTides('./data/april_tides.csv') \
        .withTides('./data/may_tides.csv') \
        .withTides('./data/june_tides.csv') \
        .withTides('./data/july_tides.csv') \
        .withTides('./data/august_tides.csv') \
        .withTides('./data/september_tides.csv') \
        .withTides('./data/october_tides.csv') \
        .withTides('./data/november_tides.csv') \
        .withTides('./data/december_tides.csv') \
        .withTides('./data/january_tides.csv') \
        .withTides('./data/february_tides.csv') \
        \
        .withEvents('./data/march_events.csv') \
        .withEvents('./data/april_events.csv') \
        .withEvents('./data/may_events.csv') \
        .withEvents('./data/june_events.csv') \
        .withEvents('./data/july_events.csv') \
        .withEvents('./data/august_events.csv') \
        .withEvents('./data/september_events.csv') \
        .withEvents('./data/october_events.csv') \
        .withEvents('./data/november_events.csv') \
        .withEvents('./data/december_events.csv') \
        .withEvents('./data/january_events.csv') \
        .withEvents('./data/february_events.csv')
    calendar.create()