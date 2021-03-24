from six.moves.urllib import parse as urlparse

from django.conf import settings
from django.contrib import auth
from django.core.signing import TimestampSigner

from . import app_settings


def get_automatic_login_token(user):
    token = TimestampSigner(
        salt=get_user_salt(user),
    ).sign(user.pk)

    return "%s=%s" % (app_settings.KEY, token)


def strip_token(url):
    bits = urlparse.urlparse(url)
    original_query = urlparse.parse_qsl(bits.query)

    query = [(k, v) for k, v in original_query if k != app_settings.KEY]

    query = urlparse.urlencode(query)

    return urlparse.urlunparse((bits[0], bits[1], bits[2], bits[3], query, bits[5]),)


def login(request, user):
    user.backend = settings.AUTHENTICATION_BACKENDS[0]
    auth.login(request, user)


def get_user_salt(user):
    parts = []

    for field in app_settings.SALT_FIELDS:
        # Follow "django__join__notation'
        part = user
        for x in field.split("__"):
            part = getattr(part, x)

        parts.append(part)

    return "".join(str(x) for x in parts)
