from typing import List

from main.models import RCCDay, RCCMonth, RCCYear
from main.parsers.event_month_file import EventMonthFile
from main.parsers.tide_month_file import TideMonthFile
from main.writers.ical_writer import ICalWriter


class RibbleCruisingClubICalCalender:
    def __init__(self):
        self.tide_files :List[EventMonthFile] = []
        self.event_files :List[TideMonthFile] = []

    def with_tides_file(self, file_path):
        self.tide_files.append(TideMonthFile(file_path))
        return self

    def with_events_file(self, file_path):
        self.event_files.append(EventMonthFile(file_path))
        return self

    def events_ics_file(self, file_name: str = "rcc_calendar"):

        months=[]
        for file_handler in self.event_files:
            event_month :List[RCCDay] = file_handler.parse()
            if event_month is not None and event_month.__len__() > 0:
                months.append(RCCMonth(name=event_month[0].date.strftime("%B"), days=event_month))
        rcc_year = RCCYear(months=months)

        writer = ICalWriter()
        components = rcc_year.ical_component()
        return writer.write_events(components, file_name)

    def tides_ics_file(self, file_name: str = "rcc_calendar"):
        months=[]
        for file_handler in self.tide_files:
            tide_month :List[RCCDay] = file_handler.parse()
            if tide_month is not None and tide_month.__len__() > 0:
                months.append(RCCMonth(name=tide_month[0].date.strftime("%B"), days=tide_month))
        rcc_year = RCCYear(months=months)

        writer = ICalWriter()
        components = rcc_year.ical_component()
        return writer.write_events(components, file_name)