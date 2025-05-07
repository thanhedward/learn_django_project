from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django_filters import rest_framework as filters
from django.db.models import Count
from .models import Movie
from .permissions import IsOwnerOrReadOnly
from .serializers import MovieSerializer
from .pagination import CustomPagination
from .filters import MovieFilter


class ListCreateMovieAPIView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MovieFilter

    def perform_create(self, serializer):
        # Assign the user who created the movie
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def movie_stats(request):
    total_movies = Movie.objects.filter(creator=request.user).count()
    genres = Movie.objects.filter(creator=request.user).values('genre').annotate(count=Count('genre'))
    years = Movie.objects.filter(creator=request.user).values('year').annotate(count=Count('year'))
    
    return Response({
        'total_movies': total_movies,
        'genres': genres,
        'years': years
    })


@login_required
def movies_view(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/movie_list.html', context)


