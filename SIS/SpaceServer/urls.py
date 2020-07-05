from django.conf.urls import url, include
from django.urls import path
from SpaceServer import views
from rest_framework import routers
from .views import UserViewSet, RecordViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('records', RecordViewSet)
urlpatterns = [
     path('', include(router.urls)),
]