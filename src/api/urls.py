from allauth.account.views import ConfirmEmailView
from dj_rest_auth.views import PasswordResetConfirmView
from django.urls import include, path
from rest_framework import routers
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from api.views.booking import (
    ApproveBookingAPIView,
    CancelBookingAPIView,
    CreateBookingView,
    ListRetrieveBookingViewSet,
    SettingBookingView,
)
from api.views.playground import (
    CoveringViewSet,
    SportViewSet,
    PlaygroundViewSet,
)

v1_router = routers.DefaultRouter()

v1_router.register("sports", SportViewSet, basename="sport")
v1_router.register("coverings", CoveringViewSet, basename="covering")
v1_router.register("playgrounds", PlaygroundViewSet, basename="playground")
v1_router.register("bookings", ListRetrieveBookingViewSet, basename="booking")
# v1_router.register(
#     r'bookings/(?P<playground_slug>\d+)',
#     BookingViewSet, basename='booking',
# )


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
    path(
        "v1/playgrounds/<int:playground_id>/bookings/",
        CreateBookingView.as_view(),
    ),
    path(
        "v1/bookings/<int:booking_id>/cancel/",
        CancelBookingAPIView.as_view(),
    ),
    path(
        "v1/bookings/<int:booking_id>/approve/",
        ApproveBookingAPIView.as_view(),
    ),
    # users and auth
    path(
        "v1/auth/registration/account-confirm-email/<str:key>/",
        ConfirmEmailView.as_view(),
        name="account_confirm_email",
    ),
    path("v1/auth/registration/", include("dj_rest_auth.registration.urls")),
    path(
        "v1/auth/password/reset/confirm/<str:uidb64>/<str:token>",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("v1/auth/", include("dj_rest_auth.urls")),
]
