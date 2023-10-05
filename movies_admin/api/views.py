from rest_framework import viewsets

from api.paginators import MoviePagination
from api.serializers import MovieSerializer
from movies.models import Filmwork


class MovieReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = MoviePagination
    serializer_class = MovieSerializer
    queryset = Filmwork.objects.all().prefetch_related('genres', 'persons')
