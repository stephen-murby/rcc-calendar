import unittest
from main.events_file_parser import EventsFileParser
from main.models import Event, EventType
from datetime import datetime

class TestEventsFileParser(unittest.TestCase):
    def test_parse_events_multiple_lines(self):
        lines = [
            "DATE,RCC_MEETINGS_AND_EVENTS,EVENT_TYPE,START_TIME",
            "01/03/2025,Main Committee Meeting,CLUB_ADMINISTRATION,19:30",
            "08/03/2025,Commodore's Sherry Party,SOCIAL,19:30",
            "09/03/2025,RYA Power Boat Level 2 (Fairhaven),TRAINING,09:00"
        ]
        
        expected_events = [
            Event(datetime(2025, 3, 1, 19, 30), "Main Committee Meeting", EventType.CLUB_ADMINISTRATION),
            Event(datetime(2025, 3, 8, 19, 30), "Commodore's Sherry Party", EventType.SOCIAL),
            Event(datetime(2025, 3, 9, 9, 0), "RYA Power Boat Level 2 (Fairhaven)", EventType.TRAINING)
        ]
        
        parsed_events = EventsFileParser.parse_events(lines)
        
        self.assertEqual(parsed_events, expected_events)

    def test_one_club_administration(self):
        lines = [
            "DATE,RCC_MEETINGS_AND_EVENTS,EVENT_TYPE,START_TIME",
            "01/03/2025,Main Committee Meeting,CLUB_ADMINISTRATION,19:30"
        ]

        expected_events = [
            Event(start_time=datetime(2025, 3, 1, 19, 30), title="Main Committee Meeting", type=EventType.CLUB_ADMINISTRATION)
        ]

        parsed_events = EventsFileParser.parse_events(lines)

        self.assertEqual(parsed_events, expected_events)

    def test_one_social(self):
        lines = [
            "DATE,RCC_MEETINGS_AND_EVENTS,EVENT_TYPE,START_TIME",
            "01/03/2025,Main Committee Meeting,SOCIAL,19:30"
        ]

        expected_events = [
            Event(start_time=datetime(2025, 3, 1, 19, 30), title="Main Committee Meeting", type=EventType.SOCIAL)
        ]

        parsed_events = EventsFileParser.parse_events(lines)

        self.assertEqual(parsed_events, expected_events)

    def test_one_training(self):
        lines = [
            "DATE,RCC_MEETINGS_AND_EVENTS,EVENT_TYPE,START_TIME",
            "01/03/2025,Main Committee Meeting,TRAINING,19:30"
        ]

        expected_events = [
            Event(start_time=datetime(2025, 3, 1, 19, 30), title="Main Committee Meeting", type=EventType.TRAINING)
        ]

        parsed_events = EventsFileParser.parse_events(lines)

        self.assertEqual(parsed_events, expected_events)

    def test_one_racing(self):
        lines = [
            "DATE,RCC_MEETINGS_AND_EVENTS,EVENT_TYPE,START_TIME",
            "01/03/2025,Main Committee Meeting,RACING,19:30"
        ]

        expected_events = [
            Event(start_time=datetime(2025, 3, 1, 19, 30), title="Main Committee Meeting", type=EventType.RACING)
        ]

        parsed_events = EventsFileParser.parse_events(lines)

        self.assertEqual(parsed_events, expected_events)

    def test_one_cruising(self):
        lines = [
            "DATE,RCC_MEETINGS_AND_EVENTS,EVENT_TYPE,START_TIME",
            "01/03/2025,Main Committee Meeting,CRUISING,19:30"
        ]

        expected_events = [
            Event(start_time=datetime(2025, 3, 1, 19, 30), title="Main Committee Meeting", type=EventType.CRUISING)
        ]

        parsed_events = EventsFileParser.parse_events(lines)

        self.assertEqual(parsed_events, expected_events)


    def test_one_working_party(self):
        lines = [
            "DATE,RCC_MEETINGS_AND_EVENTS,EVENT_TYPE,START_TIME",
            "01/03/2025,Main Committee Meeting,WORKING_PARTY,19:30"
        ]

        expected_events = [
            Event(start_time=datetime(2025, 3, 1, 19, 30), title="Main Committee Meeting", type=EventType.WORKING_PARTY)
        ]

        parsed_events = EventsFileParser.parse_events(lines)

        self.assertEqual(parsed_events, expected_events)

if __name__ == '__main__':
    unittest.main()