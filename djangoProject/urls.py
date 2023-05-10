from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from root.views import UserView, FriendInviteView, FriendViewSet

router = DefaultRouter()
router.register(r'friend/invite', viewset=FriendInviteView, basename='friend-invite')
router.register(r'friend', viewset=FriendViewSet, basename='friends')
router.register(r'', viewset=UserView, basename='friends')

api = [
    path('', include(router.urls), name='friend'),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', include(api)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
