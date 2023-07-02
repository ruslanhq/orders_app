from .base import *

INSTALLED_APPS += [
    'apps.store',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'store.db'),
    }
}
