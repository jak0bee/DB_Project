def print_colorful_table(file_name):
    """
    Imports the data from the file
    Args:
        file_name (str): The name of the entity to be printed
    """
    file = open(file_name, "r")
    events = []
    for event in file.readlines():
        print(event)
    file.close()


print_colorful_table("Resources/generated_events.txt")
