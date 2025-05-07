from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Project
from .serializers import ProjectSerializer
from .pagination import CustomPagination
from .filters import ProjectFilter

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProjectFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Project.objects.filter(owner=self.request.user)
        status = self.request.query_params.get('status', None)
        name = self.request.query_params.get('name', None)
        if status:
            queryset = queryset.filter(status=status)
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset.order_by('-created_at')


def project_view(request):
    name = request.GET.get('name')
    status = request.GET.get('status')
    project_list = Project.objects.filter(owner=request.user).order_by('-created_at')
    if status:
        project_list = project_list.filter(status=status)
    if name:
        project_list = project_list.filter(name__icontains=name)
    paginator = Paginator(project_list, 8)
    page = request.GET.get('page')
    projects = paginator.get_page(page)
    return render(request, 'projects/project_list.html', {'projects': projects})


@login_required
def project_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status', 'Planning')
        
        project = Project.objects.create(
            name=name,
            description=description,
            status=status,
            owner=request.user
        )
        return redirect('project_view')
        
    return render(request, 'projects/project_create.html')