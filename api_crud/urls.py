from django.contrib import admin
from django.urls import include, path

# urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/movies/', include('movies.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('api/v1/projects/', include('projects.urls')),
]