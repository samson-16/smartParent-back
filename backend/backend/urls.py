from django.contrib import admin
from django.urls import path , include
from rest_framework_simplejwt.views import TokenRefreshView
from core_app.views import CreateUserView, TokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path ('api/user/register/', CreateUserView.as_view(), name="register"  ),
    path ('api/token/', TokenObtainPairView.as_view(), name="get_token"  ),
    path ('api/token/refresh/', TokenRefreshView.as_view(), name="refresh_token"  ),
    path ('api-auth/', include("rest_framework.urls")),
    path ('api/', include("core_app.urls")),
    path('api/', include("academics.urls")),
]
