from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Character, Inventory_Item, Perk, Weapon, Armor
from django.http import JsonResponse
from .forms import CharacterCreationForm

def login_page(request):

    return render(request, 'registration/login.html')

@login_required()
def charactersheet(request):

    characters = Character.objects.filter(active=True)
    items = Inventory_Item.objects.filter()
    perks = Perk.objects.filter()
    weapons = Weapon.objects.filter()
    armors = Armor.objects.filter()

    char_perk_names = Character.objects.filter(active=True).values_list("perks__name")

    return render(request, 'charactersheet.html', {'characters': characters, 'items': items, 'perks': perks, 'weapons': weapons, 'armors': armors, 'char_perk_names': char_perk_names})

@login_required()
def newcharacter(request):

    characters = Character.objects.filter(user=request.user)
    form = CharacterCreationForm()

    return render(request, 'newcharacter.html', {'characters': characters, 'form': form})

@login_required()
def index(request):

    characters = Character.objects.filter(user=request.user)

    return render(request, 'index.html', {'characters': characters})


@login_required
@require_POST
def create_character(request):
    form = CharacterCreationForm(request.POST)
    if form.is_valid():
        character = form.save(commit=False)
        character.user = request.user
        character.save()
        return HttpResponse("Success!")

    else:
        form = CharacterCreationForm()

    return render(request, "newcharacter.html", {"form": form})

@login_required
@require_POST
def switch_character(request):

    characters = Character.objects.filter(user=request.user)
    character_to_switch = request.POST.get("switcher", "")

    for character in characters:
        if character.active == True:
            character.active = False
            character.save()

        elif character.name == character_to_switch:
            character.active = True
            character.save()
            return HttpResponse("Success!")

    return render(request, "index.html")

# LevelUpForm

# AddInventoryForm

# AddWeaponForm

# AddArmorForm

# UpdateCNDForm

# UpdateAmmoForm

# switch character

# Delete character

# Delete inventory item

# Delete weapon

# Delete armor