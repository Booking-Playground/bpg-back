from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from api.serializers.booking import SettingsBookingSerializer
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
