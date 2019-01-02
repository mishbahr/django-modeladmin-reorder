#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-modeladmin-reorder
------------

Tests for `django-modeladmin-reorder` get_admin_index function from middleware
module.
"""

from django.contrib import admin
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.test.utils import override_settings
from django.urls import path

from admin_reorder import middleware


urlpatterns = [path('', admin.site.urls), ]


@override_settings(ROOT_URLCONF=__name__)
class Testadmin_reorder(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            'admin', 'foo@foo.com', 'admin')

    def test_get_admin_index_for_default_admin_site(self):
        request = self.factory.get('/')
        request.user = self.user
        admin_index = middleware.get_admin_index(request)
        self.assertEqual(
            admin.site.index(request).context_data,
            admin_index.context_data
        )
