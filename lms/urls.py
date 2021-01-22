from django.urls import path
from lms import views

urlpatterns = [
    path('leaves/', views.LeaveList.as_view()),
    path('leave/<int:pk>/', views.LeaveDetail.as_view()),
    path('user/', views.UserCreate.as_view()),
]
