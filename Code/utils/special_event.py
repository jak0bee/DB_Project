import re


class SpecialEvent:
    def __init__(self, event_type=None, timestamp=None, entity1=None, entity2=None, value=None,
                 additional_entity_type=None, additional_entity=None):
        self.event_type = event_type
        self.timestamp = timestamp
        self.entity1 = entity1
        self.entity1_type = ""
        self.entity2 = entity2
        self.entity2_type = ""
        self.value = value
        self.additional_entity_type = additional_entity_type
        self.additional_entity = additional_entity

    def print(self):
        print("Event Type:", self.event_type)
        print("Timestamp:", self.timestamp)
        print("Entity 1:", self.entity1)
        print("Entity 1 type:", self.entity1_type)
        print("Entity 2:", self.entity2)
        print("Entity 2 type:", self.entity2_type)
        print("Value:", self.value)
        print("Additional Entity Type:", self.additional_entity_type)
        print("Additional Entity:", self.additional_entity)

    def __setattr__(self, name, value):
        if name == "event_type" and value is not None:
            match = re.match(r'(.+)_with_(.+)', value)
            if match:
                entity1_type, entity2_type = match.groups()
                # Using super().__setattr__ directly to avoid recursion
                super().__setattr__('entity1_type', entity1_type)
                super().__setattr__('entity2_type', entity2_type)
        super().__setattr__(name, value)
