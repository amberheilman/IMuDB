"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.template import RequestContext

class test_artist_detail(TestCase):

    def user_is_authenticated(self):
        self.assertTrue(request.user.is_authenticated())

    def method_is_POST(self):
	self.assertTrue(request.method == POST)
	

