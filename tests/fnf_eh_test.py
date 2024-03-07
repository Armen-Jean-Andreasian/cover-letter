from utils.file_readers.exception_handler import exception_handler
import unittest


class Test(unittest.TestCase):
    def test_file_not_found_error_handling(self):
        def failed_file_opening():
            with open(".docs.txt") as file:
                pass

        with self.assertRaises(FileNotFoundError) as context:
            exception_handler(fnf_error=failed_file_opening())

        self.assertIn("docs.txt", str(context.exception))


if __name__ == '__main__':
    unittest.main()