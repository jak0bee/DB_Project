import json
import re

from database_actions.data_import.import_events import import_events
from database_actions.database_manipulation import DatabaseManipulation
from utils.special_event import SpecialEvent

def export_events():
    """
    Exports events to the database
    """
    file_name = "../../../Resources/generated_events.txt"
    events = import_events(file_name)
    dbm = DatabaseManipulation()
    for event in events:
        event.print()
        dbm.check(event.entity1_type, event.entity1['id'])



export_events()