from os import makedirs
from os.path import exists
from shutil import rmtree
import errno


class IOUtil:

    def __init__(self):
        pass

    @classmethod
    def create_directory(cls, path):
        if not exists(path):
            try:
                makedirs(path)
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise

    @classmethod
    def delete_directory(cls, path):
        if exists(path):
            try:
                rmtree(path)
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
