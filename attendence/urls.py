from django.urls import path
from .views import *

urlpatterns = [
    path("groups/", GroupListAPIView.as_view(), name='groups_list'),
    path("groups/<int:pk>/", GroupRUDAPIView.as_view(), name='groups_rud'),
    path("students/", StudentListAPIView.as_view(), name='students_list'),
    path("students/<int:pk>/", StudentRUDAPIView.as_view(), name='students_rud'),
    path("attendence/", AttendenceListAPIView.as_view(), name='attendence_list'),
    path("attendence/late/", LateStudentsAPIView.as_view(), name='late_list'),
    path("attendence/at_time/", AttimeStudentsAPIView.as_view(), name='at_time_list'),
    path("attendence/not_came/", NotStudentsAPIView.as_view(), name='not_came_list'),
    path("attendence/<int:pk>/", AttendenceRUDAPIView.as_view(), name='attendence_rud'),
    path("apsents/", ApsentListAPIView.as_view(), name='apsent_list'),
]
