=============================
django-modeladmin-reorder
=============================

.. image:: https://badge.fury.io/py/django-modeladmin-reorder.png
    :target: https://badge.fury.io/py/django-modeladmin-reorder

.. image:: https://travis-ci.org/mishbahr/django-modeladmin-reorder.png?branch=master
    :target: https://travis-ci.org/mishbahr/django-modeladmin-reorder

.. image:: https://coveralls.io/repos/mishbahr/django-modeladmin-reorder/badge.png?branch=master
    :target: https://coveralls.io/r/mishbahr/django-modeladmin-reorder?branch=master

Custom ordering for the apps and models in the admin app.
You can rename, reorder, cross link, exclude apps or models

Documentation
-------------

The full documentation is at https://django-modeladmin-reorder.readthedocs.org.

Install
----------

Install django-modeladmin-reorder::

    pip install django-modeladmin-reorder


Configuration
----------

1. Add `admin_reorder` to `INSTALLED_APPS`::

    INSTALLED_APPS = (
        ...
        'admin_reorder',
        ...
    )


2. Add the `ModelAdminReorder` to `MIDDLEWARE_CLASSES`::


    MIDDLEWARE_CLASSES = (
        ...
        'admin_reorder.middleware.AdminReorder',
        ...
    )


3. Add the setting `ADMIN_REORDER` to your settings.py::


    ADMIN_REORDER = (
        # Keep original label and models
        'sites',

        # Rename app
        {'app': 'auth', 'label': 'Authorisation'},

        # Reorder app models
        {'app': 'auth', 'models': ('auth.User', 'auth.Group')},

        # Cross-linked models
        {'app': 'auth', 'models': ('auth.User', 'sites.Site')},

        # models with custom name
        {'app': 'auth', 'models': (
            'auth.User',
            {'model': 'auth.Group', 'label': 'User Group'},
        )},
    )


Features
--------

* TODO