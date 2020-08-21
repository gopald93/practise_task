from django.urls import path
from company import  views 

urlpatterns = [
	path('employee_details/', views.employee_details, name='employee_details'),
	path('employee_add/', views.employee_add, name='employee_add'),
	path('<int:id>/employee_edit/', views.employee_edit, name='employee_edit'),
	path('<int:id>/employee_delete/', views.employee_delete, name='employee_delete'),
]
