
import os
import unittest

from andrew_utils import get_md5sum_file


class TestMd5sum(unittest.TestCase):
    
    def test_zero(self):
        dir = os.path.dirname(os.path.realpath(__file__))
        self.assertEqual(get_md5sum_file(os.path.join(dir,'test.bin')), "b3e8dd762f95e0066de2c9c66c35a24a")