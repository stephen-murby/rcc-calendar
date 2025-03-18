import datetime
from datetime import date
from typing import Callable, List
from unittest import TestCase
from unittest.mock import MagicMock

from main.parsers.event_month_file import EventMonthFile
from main.models import RCCDay, Event, EventType


class TestEventMonthFile(TestCase):
    file_path = "test/resources/events.csv"
    event_file: EventMonthFile = EventMonthFile(path=file_path)
    fourth_start_time = datetime.datetime(year=2025, month=3, day=4, hour=19, minute=30)
    ninth_start_time = datetime.datetime(year=2025, month=3, day=9, hour=9, minute=0)
    one_line_csv = [
        "DATE,RCC MEETINGS AND EVENTS,EVENT TYPE,START TIME",
        "04/03/2025,Main Committee Meeting,CLUB_ADMINISTRATION,19:30"
    ]
    multi_line_csv = [
        "DATE,RCC MEETINGS AND EVENTS,EVENT TYPE,START TIME",
        "04/03/2025,Main Committee Meeting,CLUB_ADMINISTRATION,19:30",
        "09/03/2025,RYA Power Boat Level 2 (Fairhaven),TRAINING,09:00"
    ]


    def test_parse_calls_handler_with_file_path(self):
        self.event_file.read_lines = MagicMock(return_value=self.one_line_csv)
        self.event_file.parse()
        self.event_file.read_lines.assert_called_once()

    def test_parse_when_handler_returns_list_of_one_maps_to_events(self):
        self.event_file.read_lines = MagicMock(return_value=self.one_line_csv)

        result = self.event_file.parse()

        self.assertEqual(result, [
                RCCDay(
                    day='Tuesday',
                    date=self.fourth_start_time.date(),
                    tides=[],
                    events=[
                        Event(start_time=self.fourth_start_time, title='Main Committee Meeting', type=EventType.CLUB_ADMINISTRATION, duration_hours=2.0)
                    ]
                )
            ]
        )

    def test_parse_when_handler_returns_list_of_many_maps_to_events(self):
        self.event_file.read_lines = MagicMock(return_value=self.multi_line_csv)

        result = self.event_file.parse()

        self.assertEqual(result, [
                RCCDay(
                    day='Tuesday',
                    date=self.fourth_start_time.date(),
                    tides=[],
                    events=[
                        Event(start_time=self.fourth_start_time, title='Main Committee Meeting', type=EventType.CLUB_ADMINISTRATION, duration_hours=2.0)
                    ]
                ),
                RCCDay(
                    day='Sunday',
                    date=self.ninth_start_time.date(),
                    tides=[],
                    events=[
                        Event(start_time=self.ninth_start_time, title='RYA Power Boat Level 2 (Fairhaven)', type=EventType.TRAINING, duration_hours=4.0)
                    ]
                )
            ]
        )