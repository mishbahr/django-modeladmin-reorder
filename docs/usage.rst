========
Usage
========

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

        # Cross-linked models
        {'app': 'auth', 'models': ('auth.User', 'sites.Site')},

        # models with custom name
        {'app': 'auth', 'models': (
            'auth.Group',
            {'model': 'auth.User', 'label': 'Staff'},
        )},
    )

