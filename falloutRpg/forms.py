from django import forms
from django.contrib.auth.models import User
from .models import Character, Inventory_Item, Perk, Weapon, Armor
from django.utils.translation import gettext_lazy as _


# Lives on newcharacter.html
class CharacterCreationForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            "name",
            "description",
            "backstory",
            "karma",
            "stat_strength",
            "stat_perception",
            "stat_endurance",
            "stat_charisma",
            "stat_intelligence",
            "stat_agility",
            "stat_luck",
            "skill_barter",
            "skill_energy_weapons",
            "skill_explosives",
            "skill_guns",
            "skill_lockpick",
            "skill_medicine",
            "skill_melee_weapons",
            "skill_repair",
            "skill_science",
            "skill_sneak",
            "skill_speech",
            "skill_survival",
            "skill_unarmed",
            "action_points",
            "poison_resistance",
            "radiation_resistance",
            "critical_chance",
            "hit_points",
        ]

        labels = {
            "name": _("Name"),
            "description": _("Description"),
            "backstory": _("Backstory"),
            "karma": _("Karma"),
            "stat_strength": _("Strength"),
            "stat_perception": _("Perception"),
            "stat_endurance": _("Endurance"),
            "stat_charisma": _("Charisma"),
            "stat_intelligence": _("Intelligence"),
            "stat_agility": _("Agility"),
            "stat_luck": _("Luck"),
            "skill_barter": _("Barter"),
            "skill_energy_weapons": _("Energy Weapons"),
            "skill_explosives": _("Explosives"),
            "skill_guns": _("Guns"),
            "skill_lockpick": _("Lockpick"),
            "skill_medicine": _("Science"),
            "skill_melee_weapons": _("Melee Weapons"),
            "skill_repair": _("Repair"),
            "skill_science": _("Science"),
            "skill_sneak": _("Sneak"),
            "skill_speech": _("Speech"),
            "skill_survival": _("Survival"),
            "skill_unarmed": _("Unarmed"),
            "action_points": _("Action Points"),
            "poison_resistance": _("Poison Resistance"),
            "radiation_resistance": _("Radiation Resistance"),
            "critical_chance'": _("Critical Chance"),
            "hit_points": _("Hit Points"),
        }
        help_texts = {
            "name": _("Your character's name."),
            "description": _("How your character looks."),
            "backstory": _("Your character's backstory."),
            "karma": _("Your character's alignment."),
            "stat_strength": _("A measure of your raw physical strength."),
            "stat_perception": _("How well you use your five senses, and also pertains to a 'sixth sense'."),
            "stat_endurance": _("Your health and overall physical fitness."),
            "stat_charisma": _("	Your overall attractiveness and likeability."),
            "stat_intelligence": _("Your basic intellect, curiosity in the world and adeptness at critical thinking."),
            "stat_agility": _("A measure of your quickness and dexterity."),
            "stat_luck": _("How often good things happen to you by chance."),
            "skill_barter": _("Initial level = 2 + (Charisma x 2) + (Luck / 2)"),
            "skill_energy_weapons": _("Initial level = 2 + (Perception x 2) + (Luck / 2)"),
            "skill_explosives": _("Initial level = 2 + (Perception x 2) + (Luck / 2)"),
            "skill_guns": _("Initial level = 2 + (Agility x 2) + (Luck / 2)"),
            "skill_lockpick": _("Initial level = 2 + (Perception x 2) + (Luck / 2)"),
            "skill_medicine": _("Initial level = 2 + (Intelligence x 2) + (Luck / 2)"),
            "skill_melee_weapons": _("Initial level = 2 + (Strength x 2) + (Luck / 2)"),
            "skill_repair": _("Initial level = 2 + (Intelligence x 2) + (Luck / 2)"),
            "skill_science": _("Initial level = 2 + (Intelligence x 2) + (Luck / 2)"),
            "skill_sneak": _("Initial level = 2 + (Agility x 2) + (Luck / 2)"),
            "skill_speech": _("Initial level = 2 + (Charisma x 2) + (Luck / 2)"),
            "skill_survival": _("Initial level = 2 + (Endurance x 2) + (Luck / 2)"),
            "skill_unarmed": _("Initial level = 2 + (Endurance x 2) + (Luck / 2)"),
            "action_points": _("Initial level = 65 + (Agility x 3)"),
            "poison_resistance": _("Initial level = (Endurance x 5) - 5"),
            "radiation_resistance": _("Initial level = (Endurance x 2) - 2"),
            "critical_chance'": _("Initial level = Luck"),
            "hit_points": _("Initial level = 95 + (Endurance x 20) + (Level x 5)"),
        }


# Lives on levelup.html
class LevelUpForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            "level",
            "skill_barter",
            "skill_energy_weapons",
            "skill_explosives",
            "skill_guns",
            "skill_lockpick",
            "skill_medicine",
            "skill_melee_weapons",
            "skill_repair",
            "skill_science",
            "skill_sneak",
            "skill_speech",
            "skill_survival",
            "skill_unarmed",
            "hit_points",
            "perks",
        ]

        labels = {
            "level": _("Level"),
            "skill_barter": _("Barter"),
            "skill_energy_weapons": _("Energy Weapons"),
            "skill_explosives": _("Explosives"),
            "skill_guns": _("Guns"),
            "skill_lockpick": _("Lockpick"),
            "skill_medicine": _("Science"),
            "skill_melee_weapons": _("Melee Weapons"),
            "skill_repair": _("Repair"),
            "skill_science": _("Science"),
            "skill_sneak": _("Sneak"),
            "skill_speech": _("Speech"),
            "skill_survival": _("Survival"),
            "skill_unarmed": _("Unarmed"),
            "hit_points": _("Hit Points"),
            "perks": _("Perks"),
        }

        help_texts = {
            "level": _("Your character's overall level."),
            "stat_luck": _("How often good things happen to you by chance."),
            "skill_barter": _("Initial level = 2 + (Charisma x 2) + (Luck / 2)"),
            "skill_energy_weapons": _("Initial level = 2 + (Perception x 2) + (Luck / 2)"),
            "skill_explosives": _("Initial level = 2 + (Perception x 2) + (Luck / 2)"),
            "skill_guns": _("Initial level = 2 + (Agility x 2) + (Luck / 2)"),
            "skill_lockpick": _("Initial level = 2 + (Perception x 2) + (Luck / 2)"),
            "skill_medicine": _("Initial level = 2 + (Intelligence x 2) + (Luck / 2)"),
            "skill_melee_weapons": _("Initial level = 2 + (Strength x 2) + (Luck / 2)"),
            "skill_repair": _("Initial level = 2 + (Intelligence x 2) + (Luck / 2)"),
            "skill_science": _("Initial level = 2 + (Intelligence x 2) + (Luck / 2)"),
            "skill_sneak": _("Initial level = 2 + (Agility x 2) + (Luck / 2)"),
            "skill_speech": _("Initial level = 2 + (Charisma x 2) + (Luck / 2)"),
            "skill_survival": _("Initial level = 2 + (Endurance x 2) + (Luck / 2)"),
            "skill_unarmed": _("Initial level = 2 + (Endurance x 2) + (Luck / 2)"),
            "hit_points": _("Initial level = 95 + (Endurance x 20) + (Level x 5)"),
            "perks": _("Perks"),
        }


# Lives on charactersheet.html
class AddInventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory_Item

        fields = [
            "owner",
            "quantity",
            "name",
            "value",
            "notes",
        ]

        labels = {
            "owner": _("Owner"),
            "Quantity": _("Quantity"),
            "name": _("Name"),
            "value": _("Value"),
            "notes": _("Notes"),
        }

        help_texts = {
            "owner": _("Character that owns this item."),
            "Quantity": _("Quantity of item."),
            "name": _("Name of item."),
            "value": _("Value of item (in caps)."),
            "notes": _("Special purpose or abilities of item."),
        }


# Lives on charactersheet.html
class AddWeaponForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = [
            "owner",
            "name",
            "type",
            "range",
            "damage",
            "is_burst",
            "ap_cost_single",
            "ap_cost_targeted",
            "ap_cost_burst",
            "ammo_count",
            "ammo_type",
            "ammo_per_shot",
            "ammo_per_burst",
            "special_abilities",
        ]

        labels = {
            "owner": _("Owner"),
            "name": _("Name"),
            "type": _("Type"),
            "range": _("Range"),
            "damage": _("Damage"),
            "is_burst": _("Is this a burst weapon?"),
            "ap_cost_single": _("AP cost (Single shot)"),
            "ap_cost_targeted": _("AP cost (Targeted shot)"),
            "ap_cost_burst": _("AP cost (Burst shot)"),
            "ammo_count": _("Ammo count"),
            "ammo_type": _("Ammo type"),
            "ammo_per_shot": _("Ammo per shot"),
            "ammo_per_burst": _("Ammo per burst"),
            "special_abilities": _("Special abilities"),
        }

        help_texts = {
            "owner": _("Character that owns this weapon."),
            "name": _("Name of weapon."),
            "type": _("Type of weapon."),
            "range": _("Range of weapon."),
            "damage": _("Damage per hit."),
            "is_burst": _("Is this weapon capable of burst fire?"),
            "ap_cost_single": _("How much AP it costs to fire one shot or attack."),
            "ap_cost_targeted": _("How much AP it costs to fire one targeted shot or attack."),
            "ap_cost_burst": _("How much AP it costs to fire one burst."),
            "ammo_count": _("How much ammo the character has for this weapon."),
            "ammo_type": _("What type of ammo the weapon uses."),
            "ammo_per_shot": _("How much ammo is expended per shot."),
            "ammo_per_burst": _("How much ammo is expended per burst."),
            "special_abilities": _("Any special abilities the weapon may have."),
        }


# Lives on charactersheet.html
class AddArmorForm(forms.ModelForm):
    class Meta:
        model = Armor
        fields = [
            "owner",
            "name",
            "type",
            "effects",
            "armor_class",
            "damage_reduction",
        ]

        labels = {
            "owner": _("Owner"),
            "name": _("Name"),
            "type": _("Type"),
            "effects": _("Effects"),
            "armor_class": _("Armor Class"),
            "damage_reduction": _("Damage Reduction"),
        }

        help_texts = {
            "owner": _("Character that owns this armor."),
            "name": _("Name of armor."),
            "type": _("Type of armor."),
            "effects": _("Special effects that armor has (including stat increases). Med: Agility -1, Hvy: Agility -2."),
            "armor_class": _("Armor Class"),
            "damage_reduction": _("Damage Reduction"),
        }


# Lives on charactersheet.html
class UpdateCNDForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            "hit_points",
            "rads",
            "rad_effects",
            "other_effects",
        ]

        labels = {
            "hit_points": _("Hit points"),
            "rads": _("Rads"),
            "rad_effects": _("Radiation effects"),
            "other_effects": _("Other effects"),
        }

        help_texts = {
            "hit_points": _("Character's health."),
            "rads": _("Character's radiation level."),
            "rad_effects": _("Debuffs from radiation level."),
            "other_effects": _("Effects from chems, poison, or other external factors."),
        }


# Lives on charactersheet.html
class UpdateAmmoForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = [
            "ammo_count",
        ]

        labels = {
            "ammo_count": _("Ammo count"),
        }

        help_texts = {
            "ammo_count": _("How much ammo the character has left for this weapon."),
        }
