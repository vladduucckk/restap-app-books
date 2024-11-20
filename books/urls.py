from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet
from rest_framework_simplejwt import views as jwt_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.SimpleRouter()
router.register(r'book', BookViewSet)

# Настройки для Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Book API",
        default_version='v1',
        description="API для управління книгами з фільтром, доступом через JWT, та різними рівнями доступу",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="vladislavmojseev@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
