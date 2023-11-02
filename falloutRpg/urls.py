from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newcharacter.html', views.newcharacter, name="newcharacter"),
    path('charactersheet.html', views.charactersheet, name="charactersheet"),
    path('create_character/', views.create_character, name='create_character'),
    path('switch_character/', views.switch_character, name='switch_character'),
]