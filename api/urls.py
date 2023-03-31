from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('attendance_class_info', AttendanceClassInfoView.as_view()),
]
