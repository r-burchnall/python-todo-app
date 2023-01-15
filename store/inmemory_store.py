import string

from .not_found_error import NotFoundError
from .store import Store, TodoItem


class InMemoryStore(Store):
    def __init__(self):
        self.items = {}

    def Add(self, item: TodoItem) -> (TodoItem | None, bool):
        self.items[item.id] = item
        return self.Get(item.id)

    def Update(self, item: TodoItem) -> TodoItem:
        if item.id not in self.items.keys():
            raise NotFoundError("item was not found in store")

        self.items[item.id] = item
        return self.items[item.id]

    def Get(self, id: string) -> (TodoItem | None, bool):
        if id not in self.items.keys():
            return None, False

        return self.items[id], True

    def Remove(self, id: string) -> bool:
        if id not in self.items.keys():
            return False

        del self.items[id]
        return True
