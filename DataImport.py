import pandas as pd

# Parsing the generated_events.txt file into a DataFrame
def parse_events(filename):
    events = []
    event = {}
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line or line == "=====":
                if event:
                    events.append(event)
                    event = {}
                continue
            key, value = line.split("]:", 1)
            key = key[1:].strip()
            event[key] = value.strip()
    if event:
        events.append(event)
    return pd.DataFrame(events)

# Parsing the generated_entities.txt file into a DataFrame
def parse_entities(filename):
    entities = []
    entity = {}
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("---"):
                if entity:
                    entities.append(entity)
                    entity = {}
                continue
            key, value = line.split("=", 1)
            key = key.strip('"')
            value = value.strip('"')
            entity[key] = value
    if entity:
        entities.append(entity)
    return pd.DataFrame(entities)

# Importing the data into DataFrames
events_df = parse_events("Resources/generated_events.txt")
entities_df = parse_entities("Resources/generated_entities.txt")

print(events_df)
print(entities_df)