from django.conf import settings

try:
    # Django 1.5+
    from django.contrib.auth import get_user_model
except ImportError:
    # Django <= 1.4
    from django.contrib.auth.models import User
else:
    User = get_user_model()

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


