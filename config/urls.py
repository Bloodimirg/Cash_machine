from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from cash_machine.utils import serve_pdf

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("cash_machine.urls")),
    path("media/<str:filename>/", serve_pdf, name="serve_pdf"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
