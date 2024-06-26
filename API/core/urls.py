from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include


schema_view = get_schema_view(
    openapi.Info(
        title="PassKeeper API",
        default_version='v0.1',
        description="Documentación Publica API PassKeeper",
        #terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="info.rocketinnovate@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0),name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('account/', include('apps.users.api.urls')),
    path('payments/', include('apps.payments.api.urls')),
    path('contact/', include('apps.contact.api.urls')),
    path('newsletter/', include('apps.newsletter.api.urls')),
]
