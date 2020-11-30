from django.conf.urls import url, include
from django.urls import path
from SpaceServer import views
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
     path('', include(router.urls)),
     path('auth/', views.wow.as_view()),
     path('records/', views.RecordListView.as_view()),
     path('records/<int:rid>/', views.RecordDetailView.as_view()),
     url(r'^rest-auth/', include('rest_auth.urls')), # Login, Logout 관련 기능
     url(r'^rest-auth/registration/', include('rest_auth.registration.urls')) # SignUp 관련 기능
]
