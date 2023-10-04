from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
]
from . import views

urlpatterns = [
    path('departments/create/', views.create_department, name='create_department'),
    path('departments/<int:department_id>/update/', views.update_department, name='update_department'),
    path('departments/<int:department_id>/delete/', views.delete_department, name='delete_department'),
    path('employees/create/', views.create_employee, name='create_employee'),
    path('employees/<int:employee_id>/update/', views.update_employee, name='update_employee'),
    path('employees/<int:employee_id>/delete/', views.delete_employee, name='delete_employee'),
]
