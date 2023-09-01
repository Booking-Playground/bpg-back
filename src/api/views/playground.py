from rest_framework import viewsets

from src.api.serializers.playground import (
    CoveringSerializer,
    SportSerializer,
    PlaygroundWriteSerializer,
    PlaygroundReadSerializer,
)
from src.playground.models import Playground, Covering, Sport


class SportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    pagination_class = None


class CoveringViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Covering.objects.all()
    serializer_class = CoveringSerializer
    pagination_class = None


class PlaygroundViewSet(viewsets.ModelViewSet):
    queryset = Playground.objects.all()

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return PlaygroundReadSerializer
        return PlaygroundWriteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
