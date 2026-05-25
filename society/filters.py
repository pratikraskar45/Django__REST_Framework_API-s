import django_filters
from .models import Society

class SocietyFilter(django_filters.FilterSet):
    room_type=django_filters.CharFilter(field_name='room_type',lookup_expr='iexact')
    room_owner=django_filters.CharFilter(field_name='room_owner',lookup_expr='icontains')
    # this is for if integer fild in range
    # id=django_filters.RangeFilter(field_name='id')
    
    # for filter for a getting range filter in charfiled
    id_min=django_filters.CharFilter(method='filter_by_id',label='From Room No')
    id_max=django_filters.CharFilter(method='filter_by_id',label='TO Room NO')
    
    
    class Meta:
        model=Society
        fields=['room_type','room_owner','id_min','id_max']   #'id'
    
    
    def filter_by_id(self,queryset,name,value):
        if name=='id_min':
            return queryset.filter(room_no__gte=value)
        elif name=='id_max':
            return queryset.filter(room_no__lte=value)
        return queryset
        
        