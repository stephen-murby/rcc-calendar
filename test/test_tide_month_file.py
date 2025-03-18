from datetime import datetime
from unittest import TestCase
from unittest.mock import MagicMock

from main.models import RCCDay
from main.models import Tide, TideType
from main.parsers.tide_month_file import TideMonthFile


#
# class TestTideMonthFile(TestCase):
#     file_path = "test/resources/tides.csv"
#     mock_handler :Callable[[str], List[str]] = None
#     tide_file :TideMonthFile = TideMonthFile(path=file_path, file_handler=mock_handler)
#
#     def test_parse_calls_handler_with_file_path(self):
#         self.tide_file.file_handler = MagicMock()
#         self.tide_file.parse()
#         self.tide_file.file_handler.assert_called_once_with(self.file_path)
#
#     def test_parse_when_handler_returns_list_maps_to_event(self):
#         self.tide_file.file_handler = MagicMock(return_value=["csv-data"])
#         result = self.tide_file.parse()
#
#
#         self.assertEqual(result, [RCCDay()])

class TestTideMonthFile(TestCase):
    file_path = "test/resources/tides.csv"
    tide_file: TideMonthFile = TideMonthFile(path=file_path)
    one_line_csv = [
        "DATE,HW,HW_HT,LW,LW_HT",
        "01/03/2025,06:30,5.2,18:45,0.8"
    ]
    one_line_expected_tides = [
        Tide(type=TideType.HIGH, time=datetime(
            year=2025, month=3, day=1, hour=6, minute=30), height=5.2),
        Tide(type=TideType.LOW, time=datetime(
            year=2025, month=3, day=1, hour=18, minute=45), height=0.8)
    ]
    one_line_day = [
        RCCDay(
            day='Saturday',
            date=datetime(year=2025, month=3, day=1).date(),
            tides=one_line_expected_tides,
            events=[]
        )
    ]

    def test_parse_tides_with_both(self):
        self.tide_file.read_lines = MagicMock(return_value=self.one_line_csv)
        parsed_tides = self.tide_file.parse()

        self.tide_file.read_lines.assert_called_once()
        self.assertCountEqual(self.one_line_day, parsed_tides)
        self.assertEqual(parsed_tides, self.one_line_day)

    #
    # def test_parse_with_only_high(self):
    #     lines = [
    #         "DATE,HW,HW_HT,LW,LW_HT",
    #         "01/03/2025,06:30,5.2,,",
    #     ]
    #
    #     expected_tides = [
    #         Tide(TideType.HIGH, datetime(2025, 3, 1, 6, 30), 5.2)
    #     ]
    #
    #     parsed_tides = TidesFileParser.parse_tides(lines)
    #
    #     self.assertEqual(parsed_tides, expected_tides)
    #
    #
    # def test_parse_with_only_low(self):
    #     lines = [
    #         "DATE,HW,HW_HT,LW,LW_HT",
    #         "01/03/2025,,,18:45,0.8",
    #     ]
    #
    #     expected_tides = [
    #         Tide(TideType.LOW, datetime(2025, 3, 1, 18, 45), 0.8)
    #     ]
    #
    #     parsed_tides = TidesFileParser.parse_tides(lines)
    #
    #     self.assertEqual(parsed_tides, expected_tides)
    #
    #
    # def test_parse_with_two_dates(self):
    #     lines = [
    #         "DATE,HW,HW_HT,LW,LW_HT",
    #         "01/03/2025,06:30,5.2,18:45,0.8",
    #         "02/03/2025,07:15,5.1,19:30,0.9"
    #     ]
    #
    #     expected_tides = [
    #         Tide(type=TideType.HIGH, time=datetime(
    #             year=2025, month=3, day=1, hour=6, minute=30), height=5.2),
    #         Tide(type=TideType.LOW, time=datetime(
    #             year=2025, month=3, day=1, hour=18, minute=45), height=0.8),
    #         Tide(type=TideType.HIGH, time=datetime(
    #             year=2025, month=3, day=2, hour=7, minute=15), height=5.1),
    #         Tide(type=TideType.LOW, time=datetime(
    #             year=2025, month=3, day=2, hour=19, minute=30), height=0.9)
    #     ]
    #
    #     parsed_tides = TidesFileParser.parse_tides(lines)
    #
    #     self.assertEqual(parsed_tides, expected_tides)
