import pytest
import sys
import os
from ..main import db, Flask




def check_test_enviornment():
    app = Flask(__name__)
    db.init_app(app)
    return app


def test_integer():
    assert check_test_enviornment()
# import instance of SQLAlchemy that is the child of the Flask instance
# test that the instance is connected to the main application
# from flask import url_for
#
# from main import post_route
#


# '''Test files size'''
