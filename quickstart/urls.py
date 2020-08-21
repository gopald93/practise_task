from django.urls import path
from quickstart import  views 

urlpatterns = [
	path('index/', views.index, name='index'),
	path('book_data_add/', views.book_data_add, name='book_data_add'),
	path('<int:id>/book_data_edit/', views.book_data_edit, name="book_data_edit"),
	path('<int:id>/book_data_delete/', views.book_data_delete, name="book_data_delete"),
]
