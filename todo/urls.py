from django.urls import path ,include

from . import views

urlpatterns = [
   

    path('todos/', views.get_todos_view , name ='get-todos_url' ),

    path('create/' , views.create_todo_view , name='create-todo_url'),

    path('get-todo/<int:pk>' ,views.get_todo_view , name='get-todo_url'),

    path('update-todo/<int:pk>', views.update_todo_view , name='update-todo_url'),

    path('delete-todo/<int:pk>', views.delete_todo_view , name='delete-todo_url') ,


    path("auth/", include("django.contrib.auth.urls")),
    path('auth/register/', views.register_user_view , name='register_url') ,



]