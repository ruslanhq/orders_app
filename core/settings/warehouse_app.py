from .base import *

INSTALLED_APPS += [  # noqa: F405
    "apps.warehouse",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "warehouse.db"),  # noqa: F405
    }
}
