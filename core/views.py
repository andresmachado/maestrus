from django.shortcuts import render, Http404
from core.utils import _encode_data, custom_redirect

# Create your views here.


def index(request, template_name='core/index.html'):
    return render(request, template_name)


def login(request, template_name='core/main.html'):
    requester = request.GET.get('r', None)

    if requester:
        request.session.update({'requester': requester})
        return render(request, template_name)
    raise Http404


def complete_auth(request):
    mhash, data = _encode_data({'email': request.user.email})
    REDIR_URL = "https://treinamento.maestrus.com/ead/auth/"
    return custom_redirect(REDIR_URL, h=mhash, d=data)
