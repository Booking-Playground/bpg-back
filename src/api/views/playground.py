from django.contrib.auth import get_user_model
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view

from api.serializers.playground import (
    CoveringSerializer,
    SportSerializer,
    PlaygroundWriteSerializer,
    PlaygroundReadSerializer,
)
from playground.models import Playground, Covering, Sport

User = get_user_model()


@extend_schema(tags=["Sports"])
@extend_schema_view(
    list=extend_schema(summary="List of Sports"),
    retrieve=extend_schema(summary="Get Sport"),
)
class SportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    pagination_class = None


@extend_schema(tags=["Coverings"])
@extend_schema_view(
    list=extend_schema(summary="List of Coverings playground"),
    retrieve=extend_schema(summary="Get Covering playground"),
)
class CoveringViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Covering.objects.all()
    serializer_class = CoveringSerializer
    pagination_class = None


@extend_schema(tags=["Playgrounds"])
@extend_schema_view(
    list=extend_schema(summary="List of Playgrounds"),
    create=extend_schema(summary="Create Playgrounds"),
    retrieve=extend_schema(summary="Get Playground"),
    partial_update=extend_schema(summary="Update Playground"),
    destroy=extend_schema(summary="Delete Playground"),
)
class PlaygroundViewSet(viewsets.ModelViewSet):
    queryset = Playground.objects.all()
    http_method_names = ("get", "post", "patch", "delete")

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return PlaygroundReadSerializer
        return PlaygroundWriteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
