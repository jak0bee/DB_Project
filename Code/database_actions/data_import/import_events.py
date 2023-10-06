import json
import re

from utils.special_event import special_event


def import_events(file_name):
    """
    Imports the data from the file
    Args:
        file_name (str): path to the file "generated_events.txt" with the events separeted by ====
    Returns:
        List[special_event]: A list of special_event objects populated based on the file content.
    Example Usage:
    >>> len(import_events("../../../Resources/sample_events"))
    5
    >>> import_events("../../../Resources/sample_events")[0].event_type
    'player_with_guild'
    """
    events = [special_event()]
    type_properties = ["event_type", "timestamp", "entity1", "entity2", "value", "additional_entity_type",
                       "additional_entity"]
    with open(file_name, "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            line = line.split()
            event_property = re.sub(r'[\[\]:]', '',  line[0])  # cleans the first value from [] and :
            # ==== means a new event, "i<len(lines) - 1" is there because the file ends with ==== and it created an empty event at the end
            if line[0] == "=====" and i < len(lines) - 1:
                events.append(special_event())
                continue
            elif event_property in type_properties:  # check if the value in [] is valid
                line = line[1:]
                line = ''.join(line)  # here the line is what needs to be inserted in the event_property of the last event
                if is_json(line.replace("'", '"')):
                    line = json.loads(line.replace('\'', '"'))
                setattr(events[-1], event_property, line)  # insert line into the event_property (of this line), for the last event
    return events

def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError as e:
        return False
    return True

# For testing
# tmp = import_events("../../../Resources/generated_events.txt")
# for event in tmp:
#     event.print()
#     print(type(event.entity1))