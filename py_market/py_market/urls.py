from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from core.views import index, contact


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path('items/', include('item.urls')),
    path("contact/", contact, name="contact"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
