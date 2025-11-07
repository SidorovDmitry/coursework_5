from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


def health_check(request):
    return HttpResponse("OK", content_type="text/plain", status=200)

urlpatterns = [
    path("admin/", admin.site.urls),

    # Основные приложения
    path("", include("habits.urls", namespace="habits")),
    path("", include("users.urls", namespace="users")),

    # Документация через drf-spectacular
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

    path("health/", health_check, name="health"),
    # Редирект с корня
    path("", RedirectView.as_view(url="/api/docs/", permanent=False), name="index"),
]
