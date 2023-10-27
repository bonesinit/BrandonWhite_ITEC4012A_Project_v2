from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newcharacter.html', views.newcharacter, name="newcharacter"),
    path('charactersheet.html', views.charactersheet, name="charactersheet"),
    # path('create_task/', views.create_task, name='create_task')
]