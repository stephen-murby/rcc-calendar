# Main function

def main():
    # Read in the the file january_events.csv 
    # and store the data in a list of dictionaries
    events = read_events('january_events.csv')
    # Print the first 5 events
    for event in events[:5]:
        print(event)

def read_events(filename):
    # Open the file and read each line that has the format: DATE,RCC_MEETINGS_AND_EVENTS,START_TIME,OTHER_EVENTS
    with open(filename) as f:
        lines = f.readlines()
        # Remove the newline character from each line
        lines = [line.strip() for line in lines]
        # Remove the header line
        lines = lines[1:]
        # Create an empty list to store the data
        data = []
        # Iterate over the lines
        for line in lines:
            # Split the line by the comma
            parts = line.split(',')
            # Store the data in a dictionary
            d = {
                'date': parts[0],
                'rcc_meetings_and_events': parts[1],
                'start_time': parts[2],
                'other_events': parts[3]
            }
            # Append the dictionary to the list
            data.append(d)
        # Return the list
        return data 
    
