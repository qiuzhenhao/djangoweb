from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('index/', views.index, name='index'),
    path("add/", views.add, name='add'),
    path('add/action', views.add_action, name='add_action'),
    path('article/<int:article_id>', views.article, name='article'),
    path('edit/<int:article_id>', views.edit, name='edit')

]
