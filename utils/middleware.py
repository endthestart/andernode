from django.conf import settings
from django.shortcuts import redirect

import re

class LoginRequiredMiddleware(object):
    def __init__(self):
        self.urls = tuple([re.compile(url) for url in settings.LOGIN_REQUIRED_URLS])

    def process_request(self, request):
        for url in self.urls:
            if url.match(request.path) and request.user.is_anonymous():
                return redirect('auth_login')
