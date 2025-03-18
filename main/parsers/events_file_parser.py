from typing import List
from main.models import Event, EventType, RCCDay
from datetime import datetime
import csv

class EventsFileParser:
    @staticmethod
    def parse_events(lines: List[str]) -> List[Event]:
        # Each line in the input file is an event in the csv format: DATE,RCC_MEETINGS_AND_EVENTS,EVENT_TYPE,START_TIME
        # Remove the header line if lines are not empty
        if lines:
            lines = lines[1:]
        # Create an empty list to store the data
        data = []
        # Iterate over the lines
        for line in lines:
            # Split the line by the comma using csv reader
            parts = next(csv.reader([line]))
            # Create a datetime object for the date and time
            # If all the required fields are not present, skip the line
            if parts[0] == "" or parts[1] == "" or parts[2] == "" or parts[3] == "":
                continue

            date_str = parts[0]
            event_name = parts[1]
            type = parts[2]
            time_str = parts[3]

            datetime_str = f"{date_str} {time_str}"
            starting_at = datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")
            # Create an Event object
            event = Event(start_time=starting_at, title=event_name, type=EventType.of(type))
            data.append(event)
        # Return the list
        return data

    @staticmethod
    def group_events_by_day(events: List[Event]) -> List[RCCDay]:
        # Create a dictionary to store the events grouped by day
        events_by_day = {}
        # Iterate over the events
        for event in events:
            # Get the date of the event
            date = event.start_time.date()
            # If the date is not in the dictionary, add it
            if date not in events_by_day:
                events_by_day[date] = []
            # Add the event to the list of events for that day
            events_by_day[date].append(event)
        # Return the list of RCCDay objects
        days :[RCCDay]= []
        for date, events in events_by_day.items():
            days.append( RCCDay(day=date.strftime('%A'), date=date, tides=[], events=events))
        return days