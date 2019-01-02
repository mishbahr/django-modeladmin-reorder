#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-modeladmin-reorder
------------

Tests for `django-modeladmin-reorder` get_admin_index function from middleware
module.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group
from django.test import RequestFactory, TestCase
from django.test.utils import override_settings
from django.urls import path

from admin_reorder import middleware
import admin_reorder


class CustomAdminSite(admin.AdminSite):
    pass


custom_admin = CustomAdminSite(name='CustomAdmin')
custom_admin.register(User, UserAdmin)
custom_admin.register(Group, GroupAdmin)
admin_reorder.custom_admin = custom_admin
urlpatterns = [path('', custom_admin.urls), ]


@override_settings(
    ROOT_URLCONF=__name__,
    ADMIN_REORDER_SITE='admin_reorder.custom_admin')
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
            custom_admin.index(request).context_data,
            admin_index.context_data
        )
