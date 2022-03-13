from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from main_app.views import *
from static_app.views import *

router = DefaultRouter()
router.register('ombor', OmborViewSet),
router.register('product', ProductViewSet),
router.register('client', ClientViewSet),
router.register('stats', StaticViewSet),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-token/', TokenObtainPairView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view()),
    path('', include(router.urls)),
]
