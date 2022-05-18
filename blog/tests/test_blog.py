# project/test_basic.py
 
import os
import unittest

from flask import app, db, request

TEST_DB = 'test.db'

class BasicTests(unittest.TestCase):

############################
#### setup and teardown ####
############################

# executed prior to each test
# def setUp(self):
# app.config['TESTING'] = True
# app.config['WTF_CSRF_ENABLED'] = False
# app.config['DEBUG'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
# os.path.join(app.config['BASEDIR'], TEST_DB)
# self.app = app.test_client()
# db.drop_all()
# db.create_all()