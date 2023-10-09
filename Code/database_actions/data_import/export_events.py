import json
import re

from database_actions.data_import.import_events import import_events
from utils.special_event import special_event

def export_events():
    """
    Exports events to the database
    """
    file_name = "../../../Resources/generated_events.txt"
    events = import_events(file_name)
    for event in events:
        event.print()


export_events()