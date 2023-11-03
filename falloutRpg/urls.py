from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newcharacter.html', views.newcharacter, name="newcharacter"),
    path('charactersheet.html', views.charactersheet, name="charactersheet"),
    path('levelup.html', views.levelup, name="levelup"),
    path('create_character/', views.create_character, name='create_character'),
    path('switch_character/', views.switch_character, name='switch_character'),
    path('add_inventory/', views.add_inventory, name='add_inventory'),
    path('add_weapon/', views.add_weapon, name='add_weapon'),
    path('add_armor/', views.add_armor, name='add_armor'),
    path('update_cnd/', views.update_cnd, name='update_cnd'),
    path('update_ammo/', views.update_ammo, name='update_ammo'),
    path('level_up_time/', views.level_up_time, name='level_up_time'),
]