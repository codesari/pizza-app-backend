from django.urls import path
from .views import register,logoutUser,loginUser

urlpatterns = [
    
    path('register/', register,name='register'),
    path('login/', loginUser,name='login'),
    path('logout/', logoutUser,name='logout'),
    
    
] 