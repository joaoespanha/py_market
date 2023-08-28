from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include


# é is
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("items/", include("item.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("conversations/", include("conversations.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
