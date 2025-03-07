import unittest
from events_file_parser import EventsFileParser
from models import Event
from datetime import datetime

class TestEventsFileParser(unittest.TestCase):
    def test_parse_events(self):
        lines = [
            "DATE,RCC_MEETINGS_AND_EVENTS,EVENT_TYPE,START_TIME",
            "01/03/2025,Main Committee Meeting,CLUB_ADMINISTRATION,19:30",
            "08/03/2025,Commodore's Sherry Party,SOCIAL,19:30",
            "09/03/2025,RYA Power Boat Level 2 (Fairhaven),TRAINING,09:00"
        ]
        
        expected_events = [
            Event(datetime(2025, 3, 1, 19, 30), "Main Committee Meeting", "CLUB_ADMINISTRATION"),
            Event(datetime(2025, 3, 8, 19, 30), "Commodore's Sherry Party", "SOCIAL"),
            Event(datetime(2025, 3, 9, 9, 0), "RYA Power Boat Level 2 (Fairhaven)", "TRAINING")
        ]
        
        parsed_events = EventsFileParser.parse_events(lines)
        
        self.assertEqual(parsed_events, expected_events)

if __name__ == '__main__':
    unittest.main()