from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HelloApiView, HelloViewSet, UserProfileViewSet, UserLoginApiView

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, base_name='hello-viewset')
router.register('profile', UserProfileViewSet)

urlpatterns = [
    path('hello-view/', HelloApiView.as_view(), name='hello-view'),
    path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
