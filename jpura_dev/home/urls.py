from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('project/<int:pk>/', project, name = 'single-project'),
    path('project/create/', createProject, name = 'create-project'),
    path('project/update/<int:pk>/', updateProject, name = 'update-project'),
    path('project/delete/<int:pk>/', deleteProject, name = 'delete-project'),

]