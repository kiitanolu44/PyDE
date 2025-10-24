import os
import sys
import unittest
from phase3.phase3_sprint3 import process, buggy, divide, divide_safe
from phase3.phase3_sprint1.phase3_sprint1 import cd

class Testing(unittest.TestCase):
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)


    def test_cd(self):
        orig_dir = os.getcwd()
        dir_name = "test_dir"
        os.mkdir(dir_name)

        self.assertNotEqual(dir_name, orig_dir)

        with cd(dir_name):
            self.assertEqual(os.getcwd(), os.path.join(orig_dir, "test_dir"))

        self.assertEqual(os.getcwd(), orig_dir)

        os.rmdir(dir_name)
        

def main() -> None:
    pass


if __name__== "__main__":
    unittest.main()
    sys.exit(main())