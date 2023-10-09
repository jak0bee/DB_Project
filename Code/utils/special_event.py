class special_event:
    def __init__(self, event_type=None, timestamp=None, entity1=None, entity2=None, value=None,
                 additional_entity_type=None, additional_entity=None):
        self.event_type = event_type
        self.timestamp = timestamp
        self.entity1 = entity1
        self.entity2 = entity2
        self.value = value
        self.additional_entity_type = additional_entity_type
        self.additional_entity = additional_entity


    def print(self):
        print("Event Type:", self.event_type)
        print("Timestamp:", self.timestamp)
        print("Entity 1:", self.entity1)
        print("Entity 2:", self.entity2)
        print("Value:", self.value)
        print("Additional Entity Type:", self.additional_entity_type)
        print("Additional Entity:", self.additional_entity)
