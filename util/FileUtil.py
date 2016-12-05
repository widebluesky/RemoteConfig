#!/usr/bin/env python
"File Util Module"
import os
class FileUtil(object):
    "File Util Class"
    def __init__(self):
        return
def is_file_exists(path):
    "Is file exists"
    return os.path.exists(path)
def make_dir(path):
    "Make dir"
    return os.mkdir(path)
def make_dirs(path):
    "Make dirs"
    return os.makedirs(path)
    