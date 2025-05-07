from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, project_view, project_create

router = DefaultRouter()
router.register('', ProjectViewSet)

urlpatterns = [
    path('/', include(router.urls)),
    path('view_projects/', project_view, name='project_view'),
    path('create/', project_create, name='project_create'),
]