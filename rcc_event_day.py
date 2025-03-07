class RccEventDay:
    def __init__(self, date, rcc_meetings_and_events, start_time, other_events):
        self.date = date
        self.rcc_meetings_and_events = rcc_meetings_and_events
        self.start_time = start_time
        self.other_events = other_events

    def __repr__(self):
        return f"RccEventDay(date='{self.date}', rcc_meetings_and_events='{self.rcc_meetings_and_events}', start_time='{self.start_time}', other_events='{self.other_events}')"