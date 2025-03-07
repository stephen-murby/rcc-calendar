from rcc_event_day import RccEventDay

class RccCalendar:
    def create(self, *file_handlers):
        all_events = []
        for file_handler in file_handlers:
            # Read in the file and store the data in a list of RccEventDay objects
            lines = read_file(file_handler)
            events = parse_events(lines)
            all_events.extend(events)

        # Filter for RccEventDay objects that have a start time and rcc_meetings_and_events
        all_events = [event for event in all_events if event.start_time and event.rcc_meetings_and_events]
        
        # Print the first 5 events
        for event in all_events[:5]:
            print(event)

def read_file(file_handler):
    # Read each line from the file handler
    lines = file_handler.readlines()
    # Remove the newline character from each line
    lines = [line.strip() for line in lines]
    return lines

def parse_events(lines):
    # Remove the header line
    lines = lines[1:]
    # Create an empty list to store the data
    data = []
    # Iterate over the lines
    for line in lines:
        # Split the line by the comma
        parts = line.split(',')
        # Create an RccEventDay object
        event = RccEventDay(parts[0], parts[1], parts[2], parts[3])
        # Append the object to the list
        data.append(event)
    # Return the list
    return data

if __name__ == '__main__':
    with open('./data/march_events.csv') as march, open('./data/april_events.csv') as april:
        calendar = RccCalendar()
        calendar.create(march, april)