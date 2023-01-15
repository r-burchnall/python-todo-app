import unittest

from store.inmemory_store import InMemoryStore
from store.not_found_error import NotFoundError
from store.todo_item import TodoItem


class InMemoryStoreTests(unittest.TestCase):
    store = InMemoryStore()

    def setUp(self) -> None:
        self.store = InMemoryStore()
        items = [
            TodoItem(id="1", title="todo item: 1", description="my first todo item"),
            TodoItem(id="2", title="todo item: 2", description="my second todo item")
        ]
        for item in items:
            self.store.Add(item)

    def test_inmemory_store_get(self):
        test_cases = [
            {
                "name": "should get first element from store",
                "input": "1",
                "expected": (TodoItem(id="1", title="todo item: 1", description="my first todo item"), True)
            },
            {
                "name": "should get second element from store",
                "input": "2",
                "expected": (TodoItem(id="2", title="todo item: 2", description="my second todo item"), True)
            },
            {
                "name": "should return false if not present",
                "input": "3",
                "expected": (None, False)
            }
        ]
        for test_case in test_cases:
            want, success = test_case["expected"]
            got, found = self.store.Get(test_case["input"])
            if success == found:
                self.assertEqual(got, want, test_case["name"])
            else:
                self.fail(test_case["name"] + ": Test expectation for 'found' attribute did not match")

    def test_inmemory_store_add(self):
        test_cases = [
            {
                "name": "create a new entity in store",
                "input": TodoItem("a new item", "with a description"),
            },
        ]
        for test_case in test_cases:
            item, found = self.store.Add(test_case["input"])

            self.assertEqual(item.id, test_case["input"].id,
                             "{0} did not match on id".format(test_case['name']))
            self.assertEqual(item.title, test_case["input"].title,
                             "{0} did not match on title".format(test_case['name']))
            self.assertEqual(item.description, test_case["input"].description,
                             "{0} did not match on description".format(test_case['name']))

    def test_inmemory_store_update(self):
        test_cases = [
            {
                "name": "create a new entity in store",
                "input": {
                    "id": "1",
                    "item": TodoItem("an updated item", "with a description", "1"),
                },
                "expected": TodoItem("an updated item", "with a description", "1")
            },
            {
                "name": "create a different entity in store",
                "input": {
                    "id": "2",
                    "item": TodoItem("an updated item", "with a description", "2"),
                },
                "expected": TodoItem("an updated item", "with a description", "2")
            },
            {
                "name": "throw an error if there is no entity with that id",
                "input": {
                    "id": "3",
                    "item": TodoItem("this shouldn't exist", "")
                },
                "expected": False
            },
        ]
        for test_case in test_cases:
            try:
                item = self.store.Update(test_case["input"]["item"])
                self.assertEqual(item, test_case["expected"],
                                 "{0}: did not match return value from update".format(test_case["name"]))

                item, found = self.store.Get(test_case["input"]["id"])
                self.assertTrue(found)
                self.assertEqual(item, test_case["expected"],
                                 "{0}: did not match return value from get".format(test_case["name"]))
            except Exception:
                self.assertEqual(False, test_case["expected"])

    def test_inmemory_store_remove(self):
        test_cases = [
            {
                "name": "create a new entity in store",
                "input": {
                    "item": TodoItem("an updated item", "with a description", "1"),
                },
                "expected": True
            },
            {
                "name": "throw an error if there is no entity with that id",
                "input": {
                    "item": TodoItem("this shouldn't exist", "")
                },
                "expected": False
            },
        ]
        for test_case in test_cases:
            success = self.store.Remove(test_case["input"]["item"].id)
            self.assertEqual(success, test_case["expected"],
                             "{0}: did not match return value from Remove".format(test_case["name"]))

            if success:
                _, found = self.store.Get(test_case["input"]["item"].id)
                self.assertFalse(found, "entity was not removed from store")


if __name__ == '__main__':
    unittest.main()
