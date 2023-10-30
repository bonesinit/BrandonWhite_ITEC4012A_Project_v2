from django.contrib import admin
from .models import Character, Inventory_Item, Perk, Weapon, Armor

# Register your models here.
admin.site.register(Character)
admin.site.register(Inventory_Item)
admin.site.register(Perk)
admin.site.register(Weapon)
admin.site.register(Armor)