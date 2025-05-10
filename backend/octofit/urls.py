from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet, TeamViewSet, BadgeViewSet

router = DefaultRouter()
router.register(r'activities', ActivityViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'badges', BadgeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
