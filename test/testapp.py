import pytest
import unittest


def testfile():
    # //check that the file inputs extension equals pdf
        file = "file.pdf"
        extension = file[len(file) -3:len(file)]
        assert extension == "pdf"


def testfilesize():
    length = 280
    assert length < 300
    # //file length
