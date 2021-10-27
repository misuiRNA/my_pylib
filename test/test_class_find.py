import os
import unittest

from libs.file.class_find import find_classes
from test.data.test_class_no01 import TestClassNo01, TestClassNo01Other
from test.data.test_class_no02 import TestClassNo02

ROOT_PATH = os.path.abspath(os.path.join(__file__, "../../"))


class TestFileSearch(unittest.TestCase):

    def test_search_class_should_success(self):
        klass_list = find_classes(ROOT_PATH, "test.data")
        expect_klass_list = [TestClassNo01, TestClassNo01Other, TestClassNo02]
        self.assertEqual(expect_klass_list, klass_list)
