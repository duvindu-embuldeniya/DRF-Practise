from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name = 'home'),

    path('register/', register, name = 'register'),
    path('login/', login, name = 'login'),
    path('logout/', logout, name = 'logout'),

    path('projects', projects, name = 'projects'),
    path('project/<int:pk>/', singleProject, name = 'single-project'),
    path('project/create/', createProject, name = 'create-project'),
    path('project/update/<int:pk>/', updateProject, name = 'update-project'),
    path('project/delete/<int:pk>/', deleteProject, name = 'delete-project'),

    path('profile/<str:username>/', singleProfile, name = 'single-profile'),
    path('profile/<str:username>/update/', updateProfile, name = 'update-profile'),
]