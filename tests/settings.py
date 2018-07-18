DEBUG = True
USE_TZ = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}
ROOT_URLCONF = 'admin_reorder.urls'
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'tests.app1',
    'tests.app2',
    'admin_reorder',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
            ]
        }
    }
]
SITE_ID = 1
SECRET_KEY = 'yolo'
ROOT_URLCONF = 'tests.urls'
