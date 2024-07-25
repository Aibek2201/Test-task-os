import os
from tempfile import TemporaryDirectory as td

from main import categorize_files_by_type as cf


def test_files_by_type():
    with td() as temp_dir:
        print(temp_dir)
        file1 = os.path.join(temp_dir, 'first.txt')
        file2 = os.path.join(temp_dir, 'second.jpg')
        dir_1 = os.path.join(temp_dir, 'dir1')
        os.makedirs(dir_1)
        file3 = os.path.join(dir_1, 'third.txt')

        open(file1, 'w').close()
        open(file2, 'w').close()
        open(file3, 'w').close()

        result = cf(temp_dir)

        assert '.txt' in result
        assert '.jpg' in result
        assert len(result['.txt']) == 2
        assert file1 in result['.txt']
        assert file3 in result['.txt']
        assert file2 in result['.jpg']


def test_no_files():
    with td() as temp_dir:
        result = cf(temp_dir)
        assert result == {}
