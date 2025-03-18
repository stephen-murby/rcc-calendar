import datetime
from typing import Callable, List

from main.models import RCCDay, Tide
from main.parsers.file import File
from main.parsers.tide_line_parser import TideLineParser


class TideMonthFile(File):
    def __init__(self, path: str):
        super().__init__(path)
        self.month = None
        self.tide_csv_line_parser = TideLineParser()

    def parse(self) -> List[RCCDay]:
        tides_csv_lines :List[str] = self.read_lines()
        days: [RCCDay] = []
        if tides_csv_lines:
            tides :List[Tide] = []
            # Each line in the input file is an event in the csv format: DATE,RCC_MEETINGS_AND_EVENTS,EVENT_TYPE,START_TIME
            # Remove the header line if lines are not empty
            for line in tides_csv_lines[1:]:
                tides.append(self.tide_csv_line_parser.parse_line(line))

            tides_by_day = self.group_tides_by_day(tides)

            # Return the list of RCCDay objects
            for k, t in tides_by_day.items():
                if self.month is None:
                    self.month = k.month
                days.append(
                    RCCDay(
                        day=k.strftime('%A'),
                        date=k,
                        tides=t,
                        events=[]
                    )
                )

        return days

    def group_tides_by_day(self, tides :List[List[Tide]]) -> dict[datetime.date, List[Tide]]:
        # Create a dictionary to store the events grouped by day
        tides_by_day = {}
        # Flatten the list of lists
        flat_tides = [
            x
            for xs in tides
            for x in xs
        ]

        # Iterate over the tides
        for t in flat_tides:
            # Get the date of the tide
            start_date = t.time.date()
            # If the date is not in the dictionary, add it
            if start_date not in tides_by_day:
                tides_by_day[start_date] = []
            # Add the tide to the list of tides for that day
            tides_by_day[start_date].append(t)

        return tides_by_day
