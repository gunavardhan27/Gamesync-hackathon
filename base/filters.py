import django_filters 
from .models import *
from django_filters import DateFilter,CharFilter
class GameFilter(django_filters.FilterSet):
    #level = 
    Type_of_Gameplay = CharFilter(field_name='Type_of_gameplay',lookup_expr='icontains')
    Level = django_filters.RangeFilter(field_name='Level')
    class Meta:
        model = BattleRoyale
        exclude = ['image','name','player_id','Level','Type_of_gameplay']
