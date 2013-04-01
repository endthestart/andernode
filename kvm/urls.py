from django.conf.urls import patterns, include, url

from kvm import views as kvm_views

urlpatterns = patterns('',
    url(r'$', kvm_views.manage_home, name='manage_home'),
)
