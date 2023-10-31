from django import forms
from django.contrib.auth.models import User
from .models import Character, Inventory_Item, Perk, Weapon, Armor
from django.utils.translation import gettext_lazy as _

class CharacterCreationForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            'name',
            'description',
            'backstory',
            'karma',
            'stat_strength',
            'stat_perception',
            'stat_endurance',
            'stat_charisma',
            'stat_intelligence',
            'stat_agility',
            'stat_luck',
            'skill_barter',
            'skill_energy_weapons',
            'skill_explosives',
            'skill_guns',
            'skill_medicine',
            'skill_melee_weapons',
            'skill_repair',
            'skill_science',
            'skill_sneak',
            'skill_speech',
            'skill_survival',
            'skill_unarmed',
            'action_points',
            'poison_resistance',
            'radiation_resistance',
            ''
        ]

        # labels = {
        #     "name": _("Writer"),
        # }
        # help_texts = {
        #     "name": _("Some useful help text."),
        # }
        # error_messages = {
        #     "name": {
        #         "max_length": _("This writer's name is too long."),
        #     },
        # }