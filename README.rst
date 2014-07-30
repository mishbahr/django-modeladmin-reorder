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
        'admin_reorder.middleware.ModelAdminReorder',
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

        # Exclude models
        {'app': 'auth', 'models': ('auth.User', )},

        # Cross-linked models
        {'app': 'auth', 'models': ('auth.User', 'sites.Site')},

        # models with custom name
        {'app': 'auth', 'models': (
            'auth.Group',
            {'model': 'auth.User', 'label': 'Staff'},
        )},
    )


Features
--------

* Reorder apps in admin index — this will allow you to position most used apps in top of the page, instead of listing apps alphabetically. e.g. ``sites`` app before the ``auth`` app

* Rename a app label easily for third party apps without having to modify the source code. e.g. rename ``auth`` app to ``Authorisation``

* Reorder models within a ``app``. e.g. ``auth.User`` model before the ``auth.Group``

* Exclude any of the models from the app list by not including it in the ``models`` config. e.g. Exclude ``auth.Group`` from app list. Please note this only excludes the model from the app list and it doesn't protect it from access via url.

* Cross link models from multiple apps to make your own app module. e.g. Group ``sites.Site`` with the ``auth`` app

* Rename individual model in the app list. e.g. rename ``auth.User`` name from ``User`` to ``Staff``

