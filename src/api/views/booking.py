from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions import IsOwner
from api.serializers.booking import (
    SettingsBookingSerializer,
    WriteBookingSerializer,
)
from booking.models import Booking
from playground.models import Playground


class SettingBookingView(APIView):
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
        serializer.save(user=self.request.user, playground=playground)
