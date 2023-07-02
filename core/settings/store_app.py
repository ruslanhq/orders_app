from .base import *

INSTALLED_APPS += [  # noqa: F405
    "apps.store",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "store.db"),  # noqa: F405
    }
}
