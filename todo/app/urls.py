"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from app.views import home, login, signup, add_todo, delete_todo, change_todo,todo_detail, search, signout


urlpatterns = [
   path('', home, name='home' ), 
   path('login/',login , name='login'), 
   path('signup/', signup), 
   path('add-todo/', add_todo), 
   path('delete-todo/<int:id>', delete_todo), 
   path('change-status/<int:id>/<str:status>', change_todo), 
   path('todo/<int:todo_id>/', todo_detail),
   path('search/', search),
   path('logout/', signout, name='logout'), 
]