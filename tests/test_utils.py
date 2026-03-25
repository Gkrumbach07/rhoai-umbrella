import unittest


class TestUtils(unittest.TestCase):
    def test_string_concatenation(self):
        """Test string concatenation"""
        result = "hello" + " " + "world"
        self.assertEqual(result, "hello world")

    def test_list_length(self):
        """Test list length calculation"""
        test_list = [1, 2, 3, 4, 5]
        self.assertEqual(len(test_list), 5)

    def test_dictionary_access(self):
        """Test dictionary key access"""
        test_dict = {"key": "value"}
        self.assertEqual(test_dict["key"], "value")


if __name__ == '__main__':
    unittest.main()
