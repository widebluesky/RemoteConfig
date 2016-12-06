#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"File Util Module"
import os
import hashlib
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
def get_file_hash(file1):
    "Get file hash"
    line = file1.readline()
    hash_value = hashlib.md5()
    while line:
        hash_value.update(line)
        line = file1.readline()
    return hash_value.hexdigest()
def is_file_hash_equal(file1, file2):
    "Is file hash equal"
    str1 = get_file_hash(file1)
    str2 = get_file_hash(file2)
    return str1 == str2
    