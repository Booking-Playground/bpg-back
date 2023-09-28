from django.shortcuts import get_object_or_404
from rest_framework import generics, status, mixins, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from api.permissions import IsOwner
from api.serializers.booking import (
    ReadBookingSerializer,
    SettingsBookingSerializer,
    WriteBookingSerializer,
)
from booking.models import Booking
from core.choices_classes import BookingStatusOptions
from playground.models import Playground


@extend_schema(tags=["Playgrounds"])
class SettingBookingView(APIView):
    @extend_schema(summary="Get Settings booking playground")
    def get(self, request, playground_id):
        settings = get_object_or_404(
            Playground,
            id=playground_id,
        ).settings_playground
        serializer = SettingsBookingSerializer(settings)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(summary="Update Settings booking playground")
    def patch(self, request, playground_id):
        settings = get_object_or_404(
            Playground,
            id=playground_id,
        ).settings_playground
        serializer = SettingsBookingSerializer(
            settings,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class CreateBookingView(generics.ListCreateAPIView):
    """
    Создание брони пользователем
    Метод: [POST].
    Эндпоинт: playgrounds/<playground_id>/bookings/ .
    """

    serializer_class = WriteBookingSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        playground = get_object_or_404(
            Playground,
            id=self.kwargs["playground_id"],
        )
        self.check_object_permissions(self.request, playground)
        return Booking.objects.filter(playground=playground)

    def perform_create(self, serializer):
        playground = get_object_or_404(
            Playground,
            id=self.kwargs["playground_id"],
        )
        if not playground.settings_playground.confirmation_required:
            serializer.save(
                user=self.request.user,
                playground=playground,
                status=BookingStatusOptions.CONFIRMED,
            )
        else:
            serializer.save(
                user=self.request.user,
                playground=playground,
            )


class ListRetrieveBookingViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    Получение информации:
    о всех бронированиях, конкретного пользователя,
    об {id} бронировании, конкретного пользователя.
    Метод: [GET].
    Эндпоинты: bookings/, bookings/<booking_id>/.
    """

    serializer_class = ReadBookingSerializer

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class CancelBookingAPIView(mixins.CreateModelMixin, GenericAPIView):
    """
    Отмена автором бронирования.
    Метод: [POST].
    Эндпоинт: bookings/<booking_id>/cancel/ .
    """

    serializer_class = WriteBookingSerializer

    def post(self, request, booking_id):
        booking = get_object_or_404(
            Booking,
            user=request.user,
            id=booking_id,
        )
        self.check_object_permissions(self.request, booking)
        booking.status = BookingStatusOptions.CANCELLED
        booking.save()
        return Response(
            {"message": f"Резерв успешно отменен!"},
            status=status.HTTP_204_NO_CONTENT,
        )


class ApproveBookingAPIView(mixins.CreateModelMixin, GenericAPIView):
    """
    Подтверждение брони владельцем площадки
    Метод: [POST].
    Эндпоинт: bookings/<booking_id>/approve/ .
    """

    serializer_class = WriteBookingSerializer
    permission_classes = (IsOwner,)

    def post(self, request, booking_id):
        booking = get_object_or_404(
            Booking,
            id=booking_id,
        )
        playground = get_object_or_404(
            Playground,
            id=booking.playground.pk,
        )
        self.check_object_permissions(self.request, playground)
        booking.status = BookingStatusOptions.CONFIRMED
        booking.save()
        return Response(
            {"message": f"Резерв успешно подтверждён!"},
            status=status.HTTP_201_CREATED,
        )
