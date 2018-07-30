# -*- coding: utf-8 -*-
import re
import unittest

from django.contrib.auth.models import User
from django.core.exceptions import ImproperlyConfigured
from django.test import RequestFactory, override_settings
try:
    from django.urls import resolve
except ImportError:
    # Backwards compatibility with Django<1.10
    from django.core.urlresolvers import resolve
from pytest import raises, mark

from admin_reorder.middleware import ModelAdminReorder
from tests.app1.models import App1Model1, App1Model2
from tests.app2.models import App2Model1, App2Model2


@mark.django_db()
class ModelAdminReorderTest(unittest.TestCase):
    """Tests for the ModelAdminReorder middleware class."""
    def setUp(self):
        self.superuser = User.objects.create(is_staff=True, is_superuser=True)

    def _make_request(self, path):
        """Generates a mocked request by a staff user for a given path."""
        request = RequestFactory().get(path)
        request.user = self.superuser
        return request

    @staticmethod
    def _get_response_for_path(request, path):
        """Executes the view at path and returns the response."""
        return resolve(path).func(request)

    def _render_admin_index(self):
        path = '/admin/'
        request = self._make_request(path)
        response = self._get_response_for_path(request, path)

        return request, response

    def test_require_configuration(self):
        """
        Throw an ImproperlyConfigured error if the ADMIN_REORDER config is missing when rendering the admin.
        """
        request, response = self._render_admin_index()

        with raises(ImproperlyConfigured) as exc_info:
            ModelAdminReorder().process_template_response(request, response)

        assert str(exc_info.value) == 'ADMIN_REORDER config is not defined.'

    def _assert_model_prescence_in_response(self, models_to_expect, response):
        """
        Given an unrendered admin index response, check that every model in the given list is mentioned there.
        """
        decoded_content = response.content.decode('utf8')

        for model_to_expect in models_to_expect:
            lower_case_model_name = model_to_expect.__name__.lower()
            assert re.search(
                '<a href="/admin/\w+/{}/" class="changelink">'.format(lower_case_model_name),
                decoded_content,
            ), lower_case_model_name + ' not present'

    def _assert_model_absence_in_response(self, models_to_be_absent, response):
        """
        Given an admin index response, check that every model in the given list is missing there.
        """
        decoded_content = response.content.decode('utf8')

        for model_to_be_absent in models_to_be_absent:
            lower_case_model_name = model_to_be_absent.__name__.lower()
            assert not re.search(
                '<a href="/admin/\w+/{}/" class="changelink">'.format(lower_case_model_name),
                decoded_content,
            ), lower_case_model_name + ' not absent'

    def _render_with_configuration_and_check_model_presence(self, config, models_to_expect, models_to_be_absent=None):
        """
        Renders the admin index with `config` as the ADMIN_REORDER setting, checks that certain models are
        mentioned on the page, and checks that certain models are absent from the page.
        """
        with override_settings(ADMIN_REORDER=config):
            request, response = self._render_admin_index()
            ModelAdminReorder().process_template_response(request, response)
            response.render()

        # Check that the right models are present/absent
        self._assert_model_prescence_in_response(models_to_expect, response)
        if models_to_be_absent:
            self._assert_model_absence_in_response(models_to_be_absent, response)

    def test_only_valid_apps(self):
        """When the config only contains valid app names, the models should be present."""
        self._render_with_configuration_and_check_model_presence(
            config=(
                'app1',
                'app2',
            ),
            models_to_expect=[App1Model1, App1Model2, App2Model1, App2Model2],
        )

    def test_custom_grouping(self):
        """When the config only uses custom grouping, the index should render."""
        self._render_with_configuration_and_check_model_presence(
            config=(
                {
                    'app': 'app1',
                    'models': (
                        'app1.App1Model1',
                        'app2.App2Model2',
                    )
                },
            ),
            models_to_expect=[App1Model1, App2Model2],
            models_to_be_absent=[App1Model2, App2Model1],
        )
