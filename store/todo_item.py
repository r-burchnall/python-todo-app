import string
import uuid


class TodoItem:
    def __init__(self, title: string):
        self.id = uuid.uuid4()
        self.title = title
