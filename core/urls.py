from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, AboutViewSet, CertificationViewSet, EducationViewSet, SkillViewSet, ProjectViewSet

router = DefaultRouter()
router.register('profile', ProfileViewSet)
router.register('about', AboutViewSet)
router.register('certifications', CertificationViewSet)
router.register('educations', EducationViewSet)
router.register('skills', SkillViewSet)
router.register('projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
