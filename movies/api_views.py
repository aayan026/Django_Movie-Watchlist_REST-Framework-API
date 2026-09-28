from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Movie
from .permissions import IsOwner
from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    İstifadəçinin öz filmləri üçün CRUD API:

    GET    /api/movies/            - siyahı (status və genre ilə filtrlənə bilər)
    POST   /api/movies/            - yeni film yarat
    GET    /api/movies/{id}/       - bir filmin detalı
    PUT    /api/movies/{id}/       - filmi tam yenilə
    PATCH  /api/movies/{id}/       - filmi qismən yenilə
    DELETE /api/movies/{id}/       - filmi sil
    """

    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'genre']

    def get_queryset(self):
        return Movie.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
