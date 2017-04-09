from django.core.urlresolvers import reverse
from django.shortcuts import redirect

def needs_login(request):
    return request.path not in [reverse('login')]

class NeedToLoginMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if needs_login(request):
            if not request.user.is_authenticated():
                return redirect(reverse('login'))
        return self.get_response(request)
