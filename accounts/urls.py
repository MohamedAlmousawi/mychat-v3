from django.urls import path
from .views import *
urlpatterns = [
	path('login/',LoginChatView.as_view(),name='login'),
	path('register',RegisterChatView,name='register'),
	path('logout',LogoutChatView.as_view(),name='logout'),
	path('edit_profile',UpdateAccountView,name='edit_profile'),
	path('profile/<int:id>',AccountView,name='profile'),
]