from django.urls import path

from hallOfFameStudent.views import DashboardStudentView, GroupStudentView, LoginStudentView

app_name = 'student'
urlpatterns = [
    path('', DashboardStudentView.as_view(), name='dashboard'),
    path('subject/<int:course_id>', GroupStudentView.as_view(), name='subject'),
    path('login',LoginStudentView.as_view(),name='login')
]