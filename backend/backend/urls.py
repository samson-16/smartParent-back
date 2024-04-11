from django.contrib import admin
from django.urls import path , include
from rest_framework_simplejwt.views import TokenRefreshView
from core_app.views import CreateUserView, TokenObtainPairView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
...

schema_view = get_schema_view(
   openapi.Info(
      title="Smart-Parent API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path ('api/user/register/', CreateUserView.as_view(), name="register"  ),
    path ('api/token/', TokenObtainPairView.as_view(), name="get_token"  ),
    path ('api/token/refresh/', TokenRefreshView.as_view(), name="refresh_token"  ),
    path ('api-auth/', include("rest_framework.urls")),
    path ('api/', include("core_app.urls")),
    path('api/', include("academics.urls")),
    path('api/', include("teacher.urls")),
   

     path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),   name='schema-swagger-ui'),
     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),   name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT ) 
