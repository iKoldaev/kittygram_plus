from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import constants
from .models import Cat, Owner
from .serializers import CatSerializer, CatListSerializer, OwnerSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    @action(detail=False, url_path='recent-white-cats')
    def recent_white_cats(self, request):
        cats = Cat.objects.filter(color='White')[:constants.CAT_COUNT]
        serializer = self.get_serializer(cats, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        # Если запрошенное действие (action)
        # получение списка объектов ('list')
        if self.action == 'list':
            # ...то применяем CatListSerializer
            return CatListSerializer
        # А если запрошенное действие — не 'list',
        # применяем CatSerializer
        return CatSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class UpdateDeleteViewSet(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class CreateRetrieveViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    pass


class LightCatViewSet(CreateRetrieveViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
