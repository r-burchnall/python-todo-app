import json
import string
import uuid


class TodoItem:
    def __init__(self, title: string, description: string, id: string = uuid.uuid4()):
        self.id = id
        self.title = title
        self.description = description

    def __eq__(self, other):
        if self.id == other.id \
                and self.title == other.title \
                and self.description == self.description:
            return True

        return False
