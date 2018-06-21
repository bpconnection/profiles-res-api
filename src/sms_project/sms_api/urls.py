from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

urlpatterns = [
    url(r'^sms_mo/', views.Sms_moApiView.as_view()),
    url(r'^cobros/', views.CobrosApiView.as_view()),
    url(r'^recobros/', views.RecobrosApiView.as_view()),
    url(r'', include(router.urls))
]
