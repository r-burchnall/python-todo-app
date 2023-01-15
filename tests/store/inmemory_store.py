import unittest

from store import InMemoryStore

class InMemoryStoreTests(unittest.TestCase):
    store = InMemoryStore()

    def test_something(self):
        self.store.Get()
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
