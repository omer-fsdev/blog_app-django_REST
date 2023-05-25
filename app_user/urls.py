from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import logout
from rest_framework import routers
from .views import UserView

router = routers.DefaultRouter()
router.register('users', UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token),
    path('logout/', logout),
]
