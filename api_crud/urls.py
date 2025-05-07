from django.contrib import admin
from django.urls import include, path

# urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('projects/', include('projects.urls')),
    path('login/', include('accounts.urls')),
]