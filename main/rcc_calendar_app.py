from main.rcc_calendar import RccCalendar
from main.ribble_cruising_club_ical_calender import RibbleCruisingClubICalCalender


class RCCCalendarApp:
    def __init__(self):
        self.calendar = RibbleCruisingClubICalCalender() \
            .with_tides_file('../data/march_tides.csv') \
            .with_tides_file('../data/april_tides.csv') \
            .with_tides_file('../data/may_tides.csv') \
            .with_tides_file('../data/june_tides.csv') \
            .with_tides_file('../data/july_tides.csv') \
            .with_tides_file('../data/august_tides.csv') \
            .with_tides_file('../data/september_tides.csv') \
            .with_tides_file('../data/october_tides.csv') \
            .with_tides_file('../data/november_tides.csv') \
            .with_tides_file('../data/december_tides.csv') \
            .with_tides_file('../data/january_tides.csv') \
            .with_tides_file('../data/february_tides.csv') \
            \
            .with_events_file('../data/march_events.csv') \
            .with_events_file('../data/april_events.csv') \
            .with_events_file('../data/may_events.csv') \
            .with_events_file('../data/june_events.csv') \
            .with_events_file('../data/july_events.csv') \
            .with_events_file('../data/august_events.csv') \
            .with_events_file('../data/september_events.csv') \
            .with_events_file('../data/october_events.csv') \
            .with_events_file('../data/november_events.csv') \
            .with_events_file('../data/december_events.csv') \
            .with_events_file('../data/january_events.csv') \
            .with_events_file('../data/february_events.csv')

    def run(self):
        self.calendar.events_ics_file(file_name='rcc_events_2025')
        self.calendar.tides_ics_file(file_name='rcc_tides_2025')



if __name__ == '__main__':
    calendar = RCCCalendarApp()
    calendar.run()