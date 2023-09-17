from django.urls import include, path
from rest_framework import routers
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from api.views.booking import SettingBookingView
from api.views.playground import (
    CoveringViewSet,
    SportViewSet,
    PlaygroundViewSet,
)
from api.views.users import CustomUserViewSet

v1_router = routers.DefaultRouter()

v1_router.register("sports", SportViewSet, basename="sport")
v1_router.register("coverings", CoveringViewSet, basename="covering")
v1_router.register("playgrounds", PlaygroundViewSet, basename="playground")
# v1_router.register(
#     r'bookings/(?P<playground_slug>\d+)',
#     BookingViewSet, basename='booking',
# )
v1_router.register("users", CustomUserViewSet, basename="users")


urlpatterns = [
    path("v1/", include(v1_router.urls)),
    path(
        "v1/playgrounds/<int:playground_id>/settings/",
        SettingBookingView.as_view(),
    ),
    path("v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "v1/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="docs",
    ),
    path("auth/", include("dj_rest_auth.urls")),
]
