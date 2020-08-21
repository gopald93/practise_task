from django.urls import path
from modelformapp import  views 

urlpatterns = [
	path('collection_details/', views.collection_details, name='collection_details'),
	# path('get_bot_response/', views.get_bot_response, name='get_bot_response'),
	# path('chat_bot/', views.chat_bot, name='chat_bot'),
	path('collection_add/', views.collection_add, name='collection_add'),
	path('<int:id>/collection_each_details/', views.collection_each_details, name='collection_each_details'),
	path('<int:id>/collection_edit/', views.collection_edit, name='collection_edit'),
	path('<int:id>/collection_delete/', views.collection_delete, name='collection_delete'),
	path('<int:id>/collection_title_edit/', views.collection_title_edit, name="collection_title_edit"),
	path('<int:id>/collection_title_delete/', views.collection_title_delete, name="collection_title_delete"),
	path('<int:id>/collection_title_detail/', views.collection_title_detail, name="collection_title_detail"),
	
]
