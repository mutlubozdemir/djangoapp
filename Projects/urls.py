from django.contrib import admin
from django.urls import path
from . import views
app_name="Projects"
urlpatterns = [

    path('dashboard/',views.dashboard,name="dashboard"),
    path('addProject/',views.addProject,name="addProject"),
    path('project/<int:id>/',views.detail,name="detail"),
    path('update/<int:id>/',views.updateProject,name="update"),
    path('delete/<int:id>/',views.deleteProject,name="delete"),
    path('comment/<int:id>/',views.addComment,name="comment"),
    path('',views.projects,name="projects")

]
