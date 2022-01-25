import pytest
import unittest

@pytest
def testapp():
    # //check that the file inputs extension equals pdf
        file = "file.pdf"
        extension = file[len(file) -3:len(file)]
        assert extension == "pdf"