from django_filters import rest_framework as filters
from .models import Project

class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    status = filters.CharFilter(lookup_expr='exact')
    created_at = filters.DateTimeFilter(lookup_expr='date')
    owner__username = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Project
        fields = ['name', 'status', 'created_at', 'owner__username']
