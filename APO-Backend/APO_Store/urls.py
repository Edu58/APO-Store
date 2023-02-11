"""APO_Store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenRefreshView
from Users.serializers import MyTokenObtainPairView

schema_view = get_schema_view(
    openapi.Info(
        title="APO Store API",
        default_version="v1",
        description="This API is created and maintained by APO Store developers. It provides a way for other "
                    "developers to extend certain APO Store functionality to other software's e.g. mobile, web",
        terms_of_service="",
        contact=openapi.Contact(email="edumuriithi58@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
                  path('admin/', admin.site.urls),

                  # DEBUG toolbar
                  path('__debug__/', include('debug_toolbar.urls')),

                  # JWT Authentication
                  path('api/v1/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

                  # drf-yasg documentation paths
                  re_path(r'^api/v1/(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
                          name='schema-json'),
                  re_path(r'^api/v1/docs/swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
                          name='schema-swagger-ui'),
                  re_path(r'^api/v1/docs/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

                  # Apps urls
                  path("api/v1/accounts/", include("Users.urls")),
                  path("api/v1/catalogue/", include("Catalogue.urls")),
                  path("api/v1/orders/", include("Orders.urls")),
                  path("api/v1/checkout/", include("Checkout.urls")),
                  path("api/v1/query/", include("Query.urls")),
                  path("api/v1/review/", include("Review.urls"))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
