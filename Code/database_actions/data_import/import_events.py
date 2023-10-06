def importevents(file_name):
    """
    Imports the data from the file
    Args:
        file_name (str): The name of the entity to be printed
    """
    file = open(file_name, "r")
    events = []
    for line in file.readlines():
        print(line.split())
    file.close()


importevents("../../../Resources/generated_events.txt")
