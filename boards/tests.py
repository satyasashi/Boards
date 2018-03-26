# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.urls import resolve

from .models import Board
from .views import home, board_topics

# Create your tests here.
class HomeTests(TestCase):

	def setUp(self):
		self.board = Board.objects.create(name="Django", description="Django board")
		url = reverse('home')
		self.response = self.client.get(url)

	def test_home_view_status_code(self):
		# when user tries to get a view that exists, status should be 200
		# url = reverse('home')
		# response = self.client.get(url) # This is given in setUp()
		self.assertEquals(self.response.status_code, 200)


	def test_home_url_resolve_home_view(self):
		# when user tries following url, correct view should be called.
		view = resolve('/')
		self.assertEquals(view.func, home)

	def test_home_view_contains_link_to_topics_page(self):
		board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
		self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))


class BoardTopicsTests(TestCase):
	def setUp(self):
		'''As django suite doesn't run tests against current database,
		To run the tests, django creates DB on the fly, applies Migration,
		runs the tests, when done destroys the testing database.'''
		Board.objects.create(name="Django", description="Django board")

	def test_board_topics_view_success_status_code(self):
		# when user tries to get a view that is existing, status should be 200
		url = reverse('board_topics', kwargs={'pk': 1})
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)

	def test_board_topics_view_not_found_status_code(self):
		# when user tries to get non existing view, status should be 404
		url = reverse('board_topics', kwargs={'pk': 99})
		response = self.client.get(url)
		self.assertEquals(response.status_code, 404)

	def test_board_topics_url_resolves_board_topics_view(self):
		# When user enter following url, django should trigger correct function
		view = resolve('/boards/1/')
		self.assertEquals(view.func, board_topics)