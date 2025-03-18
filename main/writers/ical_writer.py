from typing import List

import icalendar

from main.models import RCCMonth


class ICalWriter():

    def write_events(self, components: List[icalendar.Event], file_name: str) -> bytes:
        cal = icalendar.Calendar()
        for component in components:
            cal.add_component(component)

        ical: bytes = cal.to_ical()

        with open(f'{file_name}_events.ics', 'wb') as f:
            f.write(ical)

        return ical



    def write_events_calender_to_ics(self, calendar : RCCMonth, name: str) -> bytes:
        cal = icalendar.Calendar()

        for day in calendar.days:
            # Map the RCCDay object to an icalendar Event object
            for event in day.events:
                ical_event = icalendar.Event()
                ical_event.add('summary', event.title)
                ical_event.add('dtstart', event.start_time)
                cal.add_component(ical_event)

        ical: bytes = cal.to_ical()

        with open(f'{name}_events.ics', 'wb') as f:
            f.write(ical)

        return ical