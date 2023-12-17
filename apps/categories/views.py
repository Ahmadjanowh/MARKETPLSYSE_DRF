from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.categories.serializers import CategorySerializer
from apps.categories.models import Category

# Create your views here.
class CategoryAPIView(GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin):
     queryset = Category.objects.all()
     serializer_class = CategorySerializer
    

