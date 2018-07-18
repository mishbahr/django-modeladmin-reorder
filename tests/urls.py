from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse


def placeholder_view(request):
    return HttpResponse('')


urlpatterns = [
    # Don't use path() yet for backwards compatibility in the test suite
    url('^$', placeholder_view),
    url('^admin/', admin.site.urls),
]
