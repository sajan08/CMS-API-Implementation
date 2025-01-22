from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterUserView, LoginUserView, ContentViewSet

router = DefaultRouter()
router.register(r'content', ContentViewSet, basename='content')

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('', include(router.urls)),
]
