from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('viewset', views.HelloViewSet, basename='viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.ProfileFeedViewSet)

urlpatterns = [
    path('hello/', views.HelloApiView.as_view()),
    path('login/', views.LoginApiView.as_view()),
    path('', include(router.urls)),
]
