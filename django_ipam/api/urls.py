from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^subnet/(?P<subnet_id>[^/]+)/request-ip/$',
        views.request_ip,
        name='request_ip'),
]
