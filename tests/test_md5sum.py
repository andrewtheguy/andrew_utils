
import os

from andrew_utils import get_md5sum_file

def test_file_md5sum():
    dir = os.path.dirname(os.path.realpath(__file__))
    assert get_md5sum_file(os.path.join(dir,'test.bin')) == "b3e8dd762f95e0066de2c9c66c35a24a"