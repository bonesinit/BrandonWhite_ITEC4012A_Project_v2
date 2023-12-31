from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Character, Inventory_Item, Perk, Weapon, Armor
from .forms import CharacterCreationForm, AddInventoryForm, AddWeaponForm, AddArmorForm, UpdateCNDForm, LevelUpForm, UpdateAmmoForm


def login_page(request):

    return render(request, 'registration/login.html')


@login_required()
def charactersheet(request):

    characters = Character.objects.filter(active=True)
    items = Inventory_Item.objects.filter()
    perks = Perk.objects.filter()
    weapons = Weapon.objects.filter()
    armors = Armor.objects.filter()

    add_inventory_form = AddInventoryForm()
    add_weapon_form = AddWeaponForm()
    add_armor_form = AddArmorForm()
    update_cnd_form = UpdateCNDForm()
    update_ammo_form = UpdateAmmoForm()

    char_perk_names = Character.objects.filter(active=True).values_list("perks__name")

    return render(
        request, 'charactersheet.html',
                  {'characters': characters,
                   'items': items,
                   'perks': perks,
                   'weapons': weapons,
                   'armors': armors,
                   'char_perk_names': char_perk_names,
                   'add_inventory_form': add_inventory_form,
                   'add_weapon_form': add_weapon_form,
                   'add_armor_form': add_armor_form,
                   'update_cnd_form': update_cnd_form,
                   'update_ammo_form': update_ammo_form,
                   }
                  )


@login_required()
def levelup(request):

    characters = Character.objects.filter(active=True)
    perks = Perk.objects.filter()

    level_up_form = LevelUpForm()

    char_perk_names = Character.objects.filter(active=True).values_list("perks__name")

    return render(
        request, 'levelup.html',
                  {'characters': characters,
                   'perks': perks,
                   'char_perk_names': char_perk_names,
                   'level_up_form': level_up_form,
                   }
                  )

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

        if str(character.id) == character_to_switch:
            character.active = True
            character.save()

    return render(request, "index.html")


@login_required
@require_POST
def add_inventory(request):
    add_inventory_form = AddInventoryForm(request.POST)
    if add_inventory_form.is_valid():
        inventory = add_inventory_form.save(commit=False)
        inventory.save()
        return HttpResponse("Success!")

    else:
        add_inventory_form = AddInventoryForm()

    return render(request, "charactersheet.html", {"add_inventory_form": add_inventory_form})


@login_required
@require_POST
def add_weapon(request):
    add_weapon_form = AddWeaponForm(request.POST)
    if add_weapon_form.is_valid():
        weapon = add_weapon_form.save(commit=False)
        weapon.save()
        return HttpResponse("Success!")

    else:
        add_weapon_form = AddWeaponForm()

    return render(request, "charactersheet.html", {"add_weapon_form": add_weapon_form})


@login_required
@require_POST
def add_armor(request):
    add_armor_form = AddArmorForm(request.POST)
    if add_armor_form.is_valid():
        armor = add_armor_form.save(commit=False)
        armor.save()
        return HttpResponse("Success!")

    else:
        add_armor_form = AddWeaponForm()

    return render(request, "charactersheet.html", {"add_armor_form": add_armor_form})


@login_required
@require_POST
def update_cnd(request):

    characters = Character.objects.filter(user=request.user)
    update_cnd_form = UpdateCNDForm(request.POST)

    for character in characters:

        if character.active == True:
            if update_cnd_form.is_valid():
                character.hit_points = request.POST.get("hit_points", "")
                character.rads = request.POST.get("rads", "")
                character.rad_effects = request.POST.get("rad_effects", "")
                character.other_effects = request.POST.get("other_effects", "")
                character.save()
                return HttpResponse("Success!")

            else:
                update_cnd_form = UpdateCNDForm()

    return render(request, "charactersheet.html", {"update_cnd_form": update_cnd_form})


# Update ammo
@login_required
@require_POST
def update_ammo(request):

    weapons = Weapon.objects.all()
    update_ammo_form = UpdateAmmoForm(request.POST)
    weapon_to_update = request.POST.get("Update Ammo", "")

    for weapon in weapons:

        if str(weapon.id) == weapon_to_update:

            if update_ammo_form.is_valid():

                weapon.ammo_count = request.POST.get("ammo_count", "")
                weapon.save()
                return HttpResponse("Success!")

    else:
        update_ammo_form = UpdateAmmoForm()

    return render(request, "charactersheet.html", {"update_ammo_form": update_ammo_form})


@login_required
@require_POST
def level_up_time(request):

    characters = Character.objects.filter(user=request.user)
    level_up_form = LevelUpForm(request.POST)
    character_to_update = request.POST.get("Level Up", "")

    for character in characters:

        if str(character.id) == character_to_update:

            if level_up_form.is_valid():
                character.level = request.POST.get("level", "")

                character.skill_barter = request.POST.get("skill_barter", "")
                character.skill_energy_weapons = request.POST.get("skill_energy_weapons", "")
                character.skill_explosives = request.POST.get("skill_explosives", "")
                character.skill_guns = request.POST.get("skill_guns", "")
                character.skill_lockpick = request.POST.get("skill_lockpick", "")
                character.skill_medicine = request.POST.get("skill_medicine", "")
                character.skill_melee_weapons = request.POST.get("skill_melee_weapons", "")
                character.skill_repair = request.POST.get("skill_repair", "")
                character.skill_science = request.POST.get("skill_science", "")
                character.skill_sneak = request.POST.get("skill_sneak", "")
                character.skill_speech = request.POST.get("skill_speech", "")
                character.skill_survival = request.POST.get("skill_survival", "")
                character.skill_unarmed = request.POST.get("skill_unarmed", "")

                character.hit_points = request.POST.get("hit_points", "")

                # character.perks = request.POST.get("perks", "")

                character.save()
                return HttpResponse("Success!")

    else:
        level_up_form = LevelUpForm()

    return render(request, "levelup.html", {"level_up_form": level_up_form})


# Delete character

# Delete inventory item

# Delete weapon

# Delete armor
