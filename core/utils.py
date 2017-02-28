"""File with auxiliary functions."""
from django.http import HttpResponseRedirect
import hashlib
import pickle
import zlib
import urllib
import base64

_my_secret = "my_super_secret"


def _encode_data(data):
    """
    Codify a Dictionary data into base64 string.

    :param data: python dict
    :return: encoding hash, encoded data
    Usage
    hash, data = _encode_data({'email': 'myplain@email.com'})
    """
    text = zlib.compress(pickle.dumps(data, 0))
    text = base64.b64encode(text)
    raw = _my_secret + text.decode()
    m = hashlib.md5(raw.encode()).hexdigest()[:12]
    return m, text


def custom_redirect(url, *args, **kwargs):
    """
    Redirect to url with GET arguments.

    :param url: plain text url
    :return: HttpResponse with passed url with GET args
    Usage
    redir_url = custom_redirect('http://localhost/', **kwargs)
    """
    params = urllib.parse.urlencode(kwargs)
    return HttpResponseRedirect(url + "?{0}".format(params))
