import string

from store import Store, TodoItem


class InMemoryStore(Store):
    def __init__(self):
        print('something')
        self.items = {}

    def Add(self, item: TodoItem) -> TodoItem:
        self.items[item.id] = item
        return self.Get(item.id)

    def Update(self, item: TodoItem) -> TodoItem:
        self.items[item.id] = item
        return self.items[item.id]

    def Get(self, id: string) -> TodoItem:
        return self.items[id]

    def Remove(self, id: string) -> bool:
        del self.items[id]
