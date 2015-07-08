#!/usr/bin/python3.4

import fnmatch
import os
from os.path import abspath, join
import sys


def search_files(pattern, root_dir='.'):
    for dirname, subdirs, files in os.walk(root_dir):
        for file_path in files:
            if fnmatch.fnmatch(file_path, pattern):
                yield abspath(join(dirname, file_path))


def get_lines(filename):
    with open(filename, "r") as _file:
        for nu, line in enumerate(_file, start=1):
            yield nu, line


def grep(pattern, query):
    for file_path in search_files(pattern):
        try:
            for nu, line in get_lines(file_path):
                if query in line:
                    print('{}:{} {}'.format(file_path, nu,
                                            line.rstrip()))
        except UnicodeDecodeError:
            pass


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Syntax: pygrep.py PATTERN QUERY")
        exit(1)
    try:
        _, pattern, query = sys.argv
        grep(pattern, query)
    except KeyboardInterrupt:
        print("Interrupted by user")
        exit(0)
