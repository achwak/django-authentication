from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from myapp.views import *
urlpatterns = [
    url(r'^currentClient/', CurrentClient.as_view()),
    url(r'^updateProfile/(?P<pk>[0-9]+)$', UpdateProfile.as_view()),
    url(r'^changepswd/$', ChangePasswordView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
