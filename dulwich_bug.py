#!/usr/bin/python

"""
A simple test script that calls GitImportProcessor on sys.stdin.
"""
import sys

from dulwich.repo import Repo
from dulwich.fastexport import GitImportProcessor

from tempfile import mkdtemp


if __name__ == "__main__":
    nr = Repo(mkdtemp())
    fi = GitImportProcessor(nr)
    fi.import_stream(sys.stdin)
    exit(0)
    