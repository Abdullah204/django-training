from django_filters import rest_framework as filters
from albums.models import Album
class AlbumFilter(filters.FilterSet):
    cost__gte = filters.NumberFilter(field_name='cost', lookup_expr='gte')
    cost__lte = filters.NumberFilter(field_name='cost', lookup_expr='lte')
    name__iexact = filters.NumberFilter(field_name='name', lookup_expr='iexact')

    class Meta:
        model = Album
        fields = '__all__'