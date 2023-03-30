from . import views
from django.urls import path

urlpatterns = [
    path('employees/', views.employees_list, name='employees_list'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
]
