from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import SignUpApiView, GetAuthTokenApiView, UserViewSet

app_name = 'users'

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet)

urlpatterns = [
    path('v1/auth/signup/', SignUpApiView.as_view(), name='sign_up'),
    path('v1/auth/token/', GetAuthTokenApiView.as_view(), name='get_token'),
    path('v1/', include(router_v1.urls)),
]
