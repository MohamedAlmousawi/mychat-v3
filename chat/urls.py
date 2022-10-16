from django.urls import path
from .views import *
urlpatterns = [
	path('',HomeView,name='home'),
	path('create_chat/',CreateChatView,name='create_chat'),
	path('chat/<int:id>',ChatView,name='chat'),
	path('chat/<int:pk>/message/delete/<int:id>',DeleteChatView,name='delete'),
	path('chat/<int:pk>/message/edit/<int:id>',EditChatView,name='edit'),
	]