import json
import re
import time

from database_actions.data_import.import_events import import_events
from database_actions.database_manipulation import DatabaseManipulation
from utils.special_event import SpecialEvent


def export_events():
    """
    Exports events to the database
    """
    start_time = time.time()
    file_name = "../../../Resources/generated_events.txt"
    events = import_events(file_name)
    dbm = DatabaseManipulation()
    le = len(events)
    for i,event in enumerate(events):
        print("currently at: ", i,", from ", le)
        try:
            entity1 = dbm.check(event.entity1_type, event.entity1['id'])
            entity2 = dbm.check(event.entity2_type, event.entity2['id'])

        except TypeError:
            continue
    end_time = time.time()
    print(f"Events exported in {end_time - start_time:.2f} seconds.")


export_events()
