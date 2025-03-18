import unittest
from datetime import datetime

from main.parsers.event_line_parser import EventLineParser
from main.models import Event, EventType


class TestEventLineParser(unittest.TestCase):

    def setUp(self):
        self.parser = EventLineParser()

    def test_parse_empty_line(self):
        line = ""
        with self.assertRaises(ValueError):
            self.parser.parse_line(line)

    def test_parse_malformed_line(self):
        line = "2023-01-01,EventName"
        with self.assertRaises(ValueError):
            self.parser.parse_line(line)

    def test_parse_correct_line(self):
        line = "2023-01-01,EventName,EventType,12:00:00"
        event = self.parser.parse_line(line)
        self.assertIsInstance(event, Event)
        self.assertEqual(event.start_time, datetime.strptime("2023-01-01 12:00:00", "%Y-%m-%d %H:%M:%S"))
        self.assertEqual(event.title, "EventName")
        self.assertEqual(event.type, EventType.CLUB_ADMINISTRATION)
        self.assertEqual(event.duration_hours, 1.0)

    def test_parse_line_with_extra_fields(self):
        line = "2023-01-01,EventName,EventType,12:00:00,ExtraField"
        with self.assertRaises(ValueError):
            self.parser.parse_line(line)

    def test_parse_line_with_missing_fields(self):
        line = "2023-01-01,EventName,12:00:00"
        with self.assertRaises(ValueError):
            self.parser.parse_line(line)
