from datetime import datetime, date
from typing import Callable, List

from main.models import RCCDay, Event
from main.parsers.event_line_parser import EventLineParser
from main.parsers.file import File


class EventMonthFile(File):

    def __init__(self, path: str):
        super().__init__(path)
        self.month = None
        self.event_csv_line_parser = EventLineParser()

    def parse(self) -> List[RCCDay]:
        events_csv_lines: List[str] = self.read_lines()
        days: [RCCDay] = []

        if events_csv_lines:
            events :List[Event] = []
            # Each line in the input file is an event in the csv format: DATE,RCC_MEETINGS_AND_EVENTS,EVENT_TYPE,START_TIME
            # Remove the header line if lines are not empty
            for line in events_csv_lines[1:]:
                e = self.event_csv_line_parser.parse_line(line)
                if e:
                    events.append(e)

            events_by_day = self.group_events_by_day(events)
            self.month = events[0].start_time.month

            # Return the list of RCCDay objects
            for k, events in events_by_day.items():
                days.append(
                    RCCDay(
                        day=k.strftime('%A'),
                        date=k,
                        tides=[],
                        events=events
                    )
                )

        return days

    def group_events_by_day(self, events :List[Event]) -> dict[date, List[Event]]:
        if events is None:
            return {}
        # Create a dictionary to store the events grouped by day
        events_by_day = {}
        # Iterate over the events
        for event in events:
            # Get the date of the event
            start_date = event.start_time.date()
            # If the date is not in the dictionary, add it
            if start_date not in events_by_day:
                events_by_day[start_date] = []
            # Add the event to the list of events for that day
            events_by_day[start_date].append(event)

        return events_by_day