from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('django_ipam.urls', namespace='ipam')),
    url(r'^admin/', admin.site.urls),
]
