import unittest
import randomnames

class TestNameGenerator(unittest.TestCase):
    def test_generate(self):
        names = randomnames.generate_random_names(10)
        self.assertEqual(10, len(names))

if __name__ == "__main__":
    unittest.main()
