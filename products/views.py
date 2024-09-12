from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as django_filters_rest_framework

class ProductFilter(django_filters_rest_framework.FilterSet):
    name = django_filters_rest_framework.CharFilter(lookup_expr = 'icontains')
    # patient_id = django_filters_rest_framework.NumberFilter(field_name="name")

    class Meta:
        model = Product
        fields = ['name', 'description', 'category']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

