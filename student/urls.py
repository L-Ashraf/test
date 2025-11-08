from django.urls import include, path
from rest_framework import routers
from student import views
router = routers.DefaultRouter()
router.register(r"students", views.StudentViewSet)
urlpatterns = [
    path("student-data/", include(router.urls)),
    path("create-student/", views.create_student.as_view(), name="create-student"),
]