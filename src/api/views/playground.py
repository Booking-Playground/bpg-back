from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from api.serializers.booking import (
    WriteBookingSerializer,
    ReadBookingSerializer,
)
from api.serializers.playground import (
    CoveringSerializer,
    SportSerializer,
    PlaygroundWriteSerializer,
    PlaygroundReadSerializer,
)
from booking.models import Booking
from playground.models import Playground, Covering, Sport


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


class BookingPlaygroundViewSet(
    mixins.CreateModelMixin, viewsets.GenericViewSet
):
    serializer_class = WriteBookingSerializer

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookingViewSet(viewsets.ModelViewSet):
    http_method_names = ("get", "post")
    serializer_class = ReadBookingSerializer

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        playground = get_object_or_404(
            Booking, pk=self.kwargs.get("playground_id")
        )
        serializer.save(user=self.request.user, playground=playground)

    @action(
        detail=True,
        methods=("post",),
        url_path="cancel",
        permission_classes=(IsAuthenticated,),
    )
    def cancel(self, request, *args, **kwargs):
        """
        Отмена резервирования пользователем.
        """
        booking = get_object_or_404(Booking, pk=kwargs["pk"])
        self.check_object_permissions(self.request, booking)
        booking.delete()
        return Response(
            {"message": f"Резерв успешно отменен!"},
            status=status.HTTP_204_NO_CONTENT,
        )
