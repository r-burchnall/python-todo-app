import string
from abc import ABC, abstractmethod

from .todo_item import TodoItem


class Store(ABC):
    @abstractmethod
    def Add(self, item: TodoItem) -> bool:
        pass

    @abstractmethod
    def Update(self, item: TodoItem) -> TodoItem:
        pass

    @abstractmethod
    def Get(self, id: string) -> TodoItem:
        pass

    @abstractmethod
    def Remove(self, id: string) -> bool:
        pass