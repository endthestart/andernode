from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from custom_auth.models import User

def manage_home(request, template_name='kvm/home.html'):
    return render_to_response(template_name, {}, RequestContext(request))
