#Marcell Dorkó (6326607)  and Jakub Suszwedyk (6310933)
import time

from import_events import import_events
from database_actions.database_manipulation import DatabaseManipulation


def export_events():
    """
    Exports events to the database
    """
    start_time = time.time()
    file_name = "../../../Resources/generated_events.txt"
    events = import_events(file_name)
    dbm = DatabaseManipulation()
    le = len(events)
    columns = ["event_type", "timestamp", "entity1_id", "entity1_type", "entity2_id", "entity2_type", "value",
               "additional_entity_id", "additional_entity_type"]
    for i, event in enumerate(events):
        print("currently at: ", i, ", from ", le)
        try:
            entity1 = dbm.check(event.entity1_type, event.entity1['id'])
            if not entity1:
                print("entity one does not exist: ", event.entity1_type, event.entity1)
            entity2 = True
            if entity1:
                if event.entity2_type == 'dialogue':
                    if event.entity2 is None or dbm.check(event.entity2_type, event.entity2['id']):
                        print("Dialogue not inserted ")
                        continue
                    dbm.insert(table_name='Dialogue', columns=["id", "content", "choice_option", "emotion"], values=[
                        str(event.entity2.get("id", "null")),
                        str(event.entity2.get("content", "null")),
                        str(event.entity2.get("choice_options", "null")),
                        str(event.entity2.get("emotion", "null"))])
                else:
                    entity2 = dbm.check(event.entity2_type, event.entity2['id'])
            if entity1 and entity2:
                print("Inserting an event")
                dbm.insert(table_name="Event", values=event.values(), columns=columns)
                print("inserted")
        except TypeError:
            continue
    end_time = time.time()
    print(f"Events exported in {end_time - start_time:.2f} seconds.")


export_events()
