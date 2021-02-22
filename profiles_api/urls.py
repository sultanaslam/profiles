from django.urls import include, path
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('viewset', views.HelloViewSet, basename='viewset')

urlpatterns = [
    path('hello/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
