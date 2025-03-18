import datetime
from unittest import TestCase

from icalendar.cal import Calendar, Component

from main.writers.ical_writer import ICalWriter
from main.models import RCCMonth, RCCDay, Event, EventType


class test_ical_writer(TestCase):

    def setUp(self):
        self.writer = ICalWriter()
        self.calendar = RCCMonth("January", [
            RCCDay(datetime.date.fromisoformat("2023-01-01").weekday(), datetime.date.fromisoformat("2023-01-01"), [], [
                Event(start_time=datetime.datetime.fromisoformat("2023-01-01T10:00:00"), title="Event 1", type=EventType.SOCIAL),
                Event(start_time=datetime.datetime.fromisoformat("2023-01-01T12:00:00"), title="Event 2", type=EventType.RACING),
        ]),
            RCCDay(datetime.date.fromisoformat("2023-01-02").weekday(), datetime.date.fromisoformat("2023-01-01"), [], [
                Event(start_time=datetime.datetime.fromisoformat("2023-01-02T12:00:00"), title="Event 3", type=EventType.CLUB_ADMINISTRATION),
            ])
        ])

    def test_write_calendar_to_ics(self):
        # Read the ical output from the writer
        ical = self.writer.write_events_calender_to_ics(self.calendar, "january")
        cal :[Component] = Calendar.from_ical(ical)

        # Check that the calendar has the correct number of events
        self.assertEqual(len(cal.walk()), 3)

