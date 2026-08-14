from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("students/", views.student_list, name="student-list"),
    path("create/", views.student_create, name="student-create"),
    path("<int:student_id>/edit/", views.student_update, name="student-update"),
    path("<int:student_id>/delete/", views.student_delete, name="student-delete"),
    path("register/", views.register, name="register"),
]