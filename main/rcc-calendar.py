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

    def with_tides(self, file_path):
        self.tide_files.append(file_path)
        return self

    def with_events(self, file_path):
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
        .with_tides('../data/march_tides.csv') \
        .with_tides('./data/april_tides.csv') \
        .with_tides('./data/may_tides.csv') \
        .with_tides('./data/june_tides.csv') \
        .with_tides('./data/july_tides.csv') \
        .with_tides('./data/august_tides.csv') \
        .with_tides('./data/september_tides.csv') \
        .with_tides('./data/october_tides.csv') \
        .with_tides('./data/november_tides.csv') \
        .with_tides('./data/december_tides.csv') \
        .with_tides('./data/january_tides.csv') \
        .with_tides('./data/february_tides.csv') \
        \
        .with_events('./data/march_events.csv') \
        .with_events('./data/april_events.csv') \
        .with_events('./data/may_events.csv') \
        .with_events('./data/june_events.csv') \
        .with_events('./data/july_events.csv') \
        .with_events('./data/august_events.csv') \
        .with_events('./data/september_events.csv') \
        .with_events('./data/october_events.csv') \
        .with_events('./data/november_events.csv') \
        .with_events('./data/december_events.csv') \
        .with_events('./data/january_events.csv') \
        .with_events('./data/february_events.csv')
    calendar.create()