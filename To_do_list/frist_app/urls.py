
from django.urls import path 
from . import views
urlpatterns = [
      path('', views.home),
      path('add_task/', views.AddTask, name="addtask"),
      path('show_task/', views.ShowTask, name="showtask"),
      path('delete_task/<int:id>', views.DeteteTask, name="deletetask"),
      path('edit_task/<int:id>',views.EditTask, name="edittask"),
      path('complete_task/<int:id>', views.CompleteTask, name="completetask")
]