from datetime import datetime
from main.models import Tide, TideType
from main.parsers.tides_file_parser import TidesFileParser
import unittest

class TestTidesFileParser(unittest.TestCase):

    def test_parse_tides_with_both(self):
        lines = [
            "DATE,HW,HW_HT,LW,LW_HT",
            "01/03/2025,06:30,5.2,18:45,0.8"
        ]

        expected_tides = [
            Tide(type=TideType.HIGH, time=datetime(
                year=2025, month=3, day=1, hour=6, minute=30), height=5.2),
            Tide(type=TideType.LOW, time=datetime(
                year=2025, month=3, day=1, hour=18, minute=45), height=0.8)
        ]

        parsed_tides = TidesFileParser.parse_tides(lines)

        self.assertCountEqual(parsed_tides, expected_tides)
        self.assertEqual(parsed_tides, expected_tides)


    def test_parse_with_only_high(self):
        lines = [
            "DATE,HW,HW_HT,LW,LW_HT",
            "01/03/2025,06:30,5.2,,",
        ]

        expected_tides = [
            Tide(TideType.HIGH, datetime(2025, 3, 1, 6, 30), 5.2)
        ]

        parsed_tides = TidesFileParser.parse_tides(lines)

        self.assertEqual(parsed_tides, expected_tides)


    def test_parse_with_only_low(self):
        lines = [
            "DATE,HW,HW_HT,LW,LW_HT",
            "01/03/2025,,,18:45,0.8",
        ]

        expected_tides = [
            Tide(TideType.LOW, datetime(2025, 3, 1, 18, 45), 0.8)
        ]

        parsed_tides = TidesFileParser.parse_tides(lines)

        self.assertEqual(parsed_tides, expected_tides)


    def test_parse_with_two_dates(self):
        lines = [
            "DATE,HW,HW_HT,LW,LW_HT",
            "01/03/2025,06:30,5.2,18:45,0.8",
            "02/03/2025,07:15,5.1,19:30,0.9"
        ]

        expected_tides = [
            Tide(type=TideType.HIGH, time=datetime(
                year=2025, month=3, day=1, hour=6, minute=30), height=5.2),
            Tide(type=TideType.LOW, time=datetime(
                year=2025, month=3, day=1, hour=18, minute=45), height=0.8),
            Tide(type=TideType.HIGH, time=datetime(
                year=2025, month=3, day=2, hour=7, minute=15), height=5.1),
            Tide(type=TideType.LOW, time=datetime(
                year=2025, month=3, day=2, hour=19, minute=30), height=0.9)
        ]

        parsed_tides = TidesFileParser.parse_tides(lines)

        self.assertEqual(parsed_tides, expected_tides)

if __name__ == "__main__":
    unittest.main()
