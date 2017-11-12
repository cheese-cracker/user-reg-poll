from django.conf.urls import url
from .views import IndexView, UserRegView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),   url(r'^register/', UserRegView.as_view(), name = 'register')
]
