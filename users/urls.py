from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('add_student', AddStudentView.as_view(), name='add_student'),
    path('list_student', StudentListView.as_view(), name='list_student'),
    path('list_user', AllUsersView.as_view(), name='list_user'),
]
