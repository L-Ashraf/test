from django.urls import include, path
from rest_framework import routers
from quickstart import views
router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)


urlpatterns = [
    path("user-data/", include(router.urls)),
]
