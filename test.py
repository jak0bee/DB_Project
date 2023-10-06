import csv
import datetime
import json
import random


def load_csv_to_list(file_name, entity_type):
    """
        Load data from a CSV file to a list based on the entity_type.

        Parameters:
        file_name (str): The name of the CSV file to read.
        entity_type (str): The type of the entity, used to determine how to read the data.

        Returns:
        tuple: A tuple containing two lists.
            - The first list contains values from the first column of the CSV.
            - The second list contains values from the second column of the CSV, if applicable.

        Exceptions:
        FileNotFoundError: Raised if the file specified by file_name is not found.
        Exception: Catches all other exceptions and prints an error message.

        Example Usage:
        >>> load_csv_to_list('Resources/mystic_quest-main/mystic_quest-main/data/dialogues.csv', 'dialogue')
        (['dialogue1', 'dialogue2'], [])

        >>> load_csv_to_list('Resources/mystic_quest-main/mystic_quest-main/data/dialogues.csv', 'dialogue')
        (['dialogue1', 'dialogue2'], [])
    """

    loaded_list = []
    loaded_list_second_column = []
    try:
        with open(file_name, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                if entity_type in ['kingdom', 'team_name', 'blueprint', 'dialogue', 'event_name', 'first_name',
                                   'last_name']:
                    # Assuming the CSV has a single column for these types
                    loaded_list.append(row[0])
                elif entity_type in ['npc', 'enemy', 'item_name', 'guild']:
                    # Assuming the CSV has two columns: 'type' and 'description'
                    loaded_list.append(row[0])
                    loaded_list_second_column.append(row[1])
                else:
                    print("Unknown entity type")
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        raise FileNotFoundError()

    return loaded_list, loaded_list_second_column



blueprints, blueprint_types = load_csv_to_list('Resources/mystic_quest-main/mystic_quest-main/data/dialogues.csv', 'dialogue')
print(blueprints)