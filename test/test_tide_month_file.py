from datetime import datetime
from unittest import TestCase
from unittest.mock import MagicMock

from main.models import RCCDay
from main.models import Tide, TideType
from main.parsers.tide_month_file import TideMonthFile

class TestTideMonthFile(TestCase):
    file_path = "test/resources/tides.csv"
    tide_file: TideMonthFile = TideMonthFile(path=file_path)
    one_line_csv = [
        "DATE,HW,HW_HT,LW,LW_HT",
        "01/03/2025,0630,5.2,1845,0.8"
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