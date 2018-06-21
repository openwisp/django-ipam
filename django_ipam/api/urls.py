from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^subnet/(?P<subnet_id>[^/]+)/get-first-available-ip/$',
        views.get_first_available_ip,
        name='get_first_available_ip'),
    url(r'^subnet/(?P<subnet_id>[^/]+)/request-ip/$',
        views.RequestIPView.as_view(),
        name='request_ip'),
]
