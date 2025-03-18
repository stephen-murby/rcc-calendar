from dataclasses import dataclass
from enum import Enum
from typing import List
from datetime import datetime, timedelta

import icalendar


class TideType(Enum):
    LOW = "LOW"
    HIGH = "HIGH"

class EventType(Enum):
    SOCIAL = "SOCIAL"
    WORKING_PARTY = "WORKING_PARTY"
    TRAINING = "TRAINING"
    RACING = "RACING"
    CRUISING = "CRUISING"
    CLUB_ADMINISTRATION = "CLUB_ADMINISTRATION"

    @classmethod
    def of(cls, param):
        # return the event type that matches the param by name
        return cls[param]

    @classmethod
    def default_duration(cls, event_type):
        # return the default duration for the event type
        if event_type == cls.RACING:
            return 4.0
        if event_type == cls.CRUISING:
            return 4.0
        if event_type == cls.TRAINING:
            return 4.0
        if event_type == cls.WORKING_PARTY:
            return 6.0
        if event_type == cls.CLUB_ADMINISTRATION:
            return 2.0
        if event_type == cls.SOCIAL:
            return 4.0
        return 0.0


@dataclass
class Tide:
    type: TideType
    time: datetime
    height: float

    def ical_component(self):
        # Create an icalendar event for this tide
        ical_event = icalendar.Event()
        ical_event.add('summary', self.__str__())
        # Event start time should be 30 minutes before the tide time
        s = self.time - timedelta(minutes=30)
        ical_event.add('dtstart', s)
        # Event finish time should be 30 after before the tide time
        f = self.time + timedelta(minutes=30)
        ical_event.add('dtend', f)
        return ical_event

    def __str__(self):
        if self.type.HIGH:
            # Return a string in the format "High tide [5.6m @ 12:34]"
            return f"High tide [{self.height}m @ {self.time.strftime('%H:%M')}]"
        else:
            # Return a string in the format "Low tide [0.8m @ 18:34]"
            return f"Low tide [{self.height}m @ {self.time.strftime('%H:%M')}]"


@dataclass
class Tides:
    tides: List[Tide]

@dataclass
class Event:
    start_time: datetime
    title: str
    type: EventType
    duration_hours: float

    def ical_component(self):
        ical_event = icalendar.Event()
        ical_event.add('summary', self.title)
        ical_event.add('description', self.__str__())
        ical_event.add('dtstart', self.start_time)
        ical_event.add('dtend', self.start_time + timedelta(hours=self.duration_hours))
        return ical_event

    def __str__(self):
        return f"This is a {self.type.value} event expected to take {self.duration_hours} hours"

@dataclass
class SailingEvent(Event):
    on_the_water_time: datetime

    def ical_component(self):
        ical_event = icalendar.Event()
        ical_event.add('summary', self.title)
        ical_event.add('description', self.__str__())
        ical_event.add('dtstart', self.on_the_water_time - timedelta(hours=1))
        # Sailing possible 2 hours either side of high water, plus 1 hour for clearing up
        ical_event.add('dtend', self.start_time + timedelta(hours=5))
        return ical_event

    def __str__(self):
        return f"On the water at {self.on_the_water_time.strftime('%H:%M')}"

@dataclass
class RCCDay:
    day: str
    date: datetime.date
    tides: List[Tide]
    events: List[Event]

    def __add__(self, other):
        if self.date != other.date:
            raise ValueError("Cannot add days with different dates")

        return RCCDay(
            day=self.day,
            date=self.date,
            tides=self.tides + other.tides,
            events=self.events + other.events
        )

    def ical_component(self):
        icals = []
        for tide in self.tides:
            icals.append(tide.ical_component())
        for event in self.events:
            icals.append(event.ical_component())
        return icals


@dataclass
class RCCMonth:
    name: str
    days: List[RCCDay]

    def ical_component(self):
        icals = []
        for d in self.days:
            icals += d.ical_component()
        return icals

@dataclass
class RCCYear:
    months: List[RCCMonth]

    def ical_component(self):
        icals = []
        for m in self.months:
            icals += m.ical_component()
        return icals