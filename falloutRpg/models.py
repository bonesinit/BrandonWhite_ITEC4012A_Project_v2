from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Perk(models.Model):
    # This model contains all of the data relating to the various perks in the game.
    # Perks are available based on whether or not characters satisfy various requirements.
    # Perks that are selected on level-up are added to the character sheet.

    # ---------------------------------------------------------------------------------------------
    #       DEFINING CHOICES
    # ---------------------------------------------------------------------------------------------

    # SPECIAL

    STRENGTH = "ST"
    PERCEPTION = "PE"
    ENDURANCE = "EN"
    CHARISMA = "CH"
    INTELLIGENCE = "IN"
    AGILITY = "AG"
    LUCK = "LU"

    SPECIAL_CHOICES = [
        ("ST", "Strength"),
        ("PE", "Perception"),
        ("EN", "Endurance"),
        ("CH", "Charisma"),
        ("IN", "Intelligence"),
        ("AG", "Agility"),
        ("LU", "Luck"),
    ]

    # Skills

    BARTER = "BA"
    ENERGY_WEAPONS = "EN"
    EXPLOSIVES = "EX"
    GUNS = "GU"
    MEDICINE = "ME"
    MELEE_WEAPONS = "ML"
    REPAIR = "RE"
    SCIENCE = "SC"
    SNEAK = "SN"
    SPEECH = "SP"
    SURVIVAL = "SU"
    UNARMED = "UN"

    SKILL_CHOICES = [
        ("BA", "Barter"),
        ("EN", "Energy Weapons"),
        ("EX", "Explosives"),
        ("GU", "Guns"),
        ("ME", "Medicine"),
        ("ML", "Melee Weapons"),
        ("RE", "Repair"),
        ("SC", "Science"),
        ("SN", "Sneak"),
        ("SP", "Speech"),
        ("SU", "Survival"),
        ("UN", "Unarmed"),
    ]

    # ---------------------------------------------------------------------------------------------

    # Name of the perk.
    name = models.CharField(max_length=32)

    # Description of what effect the perk has.
    description = models.CharField(max_length=256)

    # Character level requirement from 1-50.
    level_req = models.IntegerField(default=1)

    # Name of SPECIAL skill requirement (optional)
    special_skill_name = models.CharField(
        max_length=2,
        choices=SPECIAL_CHOICES,
        default=STRENGTH,
    )

    # Special skill requirement from 1-10.
    special_skill_req = models.IntegerField(default=0)

    # Name of first skill requirement (optional)
    skill_1_name = models.CharField(
        max_length=2,
        choices=SKILL_CHOICES,
        default=BARTER,
    )
    # Required value from 1-100
    skill_1_req = models.IntegerField(default=0)

    # Name of first second requirement (optional)
    skill_2_name = models.CharField(
        max_length=2,
        choices=SKILL_CHOICES,
        default=BARTER,
    )
    # Required value from 1-100
    skill_2_req = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Character(models.Model):
    # This model contains the data of each character that a user has.
    # A user can have multiple characters.

    # ---------------------------------------------------------------------------------------------
    #       DEFINING CHOICES
    # ---------------------------------------------------------------------------------------------

    # Karma
    VERY_GOOD = "VG"
    GOOD = "GO"
    NEUTRAL = "NE"
    EVIL = "EV"
    VERY_EVIL = "VE"

    KARMA_CHOICES = [
        ("VG", "Very Good"),
        ("GO", "Good"),
        ("NE", "Neutral"),
        ("EV", "Evil"),
        ("VE", "Very Evil"),
    ]

    # ---------------------------------------------------------------------------------------------
    #       GENERAL INFORMATION
    # ---------------------------------------------------------------------------------------------
    # This is information that defines the character's history, appearance, and alignment.

    # Name of character.
    name = models.CharField(max_length=64)

    # Physical description of character.
    description = models.CharField(max_length=512)

    # Backstory of character.
    backstory = models.CharField(max_length=512)

    # Character karma alignment.
    karma = models.CharField(
        max_length=2,
        choices=KARMA_CHOICES,
        default=NEUTRAL,
    )

    # ---------------------------------------------------------------------------------------------
    #       SPECIAL STATS
    # ---------------------------------------------------------------------------------------------
    # These are the core primary statistics that affect secondary statistics and skills.
    # Strength, Perception, Endurance, Charisma, Intelligence, Agility, Luck

    stat_strength = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    stat_perception = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    stat_endurance = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    stat_charisma = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    stat_intelligence = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    stat_agility = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    stat_luck = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])

    # ---------------------------------------------------------------------------------------------
    #       SKILLS
    # ---------------------------------------------------------------------------------------------
    # These are the skills used for skill checks and combat.
    # Barter, Energy Weapons, Explosive, Guns, Medicine, Melee Weapons, Repair,
    # Science, Sneak, Speech, Survival, Unarmed

    skill_barter = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    skill_energy_weapons = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    skill_explosives = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    skill_guns = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    skill_medicine = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    skill_melee_weapons = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    skill_repair = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    skill_science = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    skill_sneak = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    skill_speech = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    skill_survival = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    skill_unarmed = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])

    # ---------------------------------------------------------------------------------------------
    #       SECONDARY STATISTICS
    # ---------------------------------------------------------------------------------------------
    # These are statistics derived from the player's SPECIAL (primary) statistics.
    # Action Points, Poison Resistance, Radiation Resistance, Critical Chance (%)

    action_points = models.IntegerField(default=1)

    poison_resistance = models.IntegerField(default=0, validators=[MaxValueValidator(85), MinValueValidator(0)])

    radiation_resistance = models.IntegerField(default=0, validators=[MaxValueValidator(85), MinValueValidator(0)])

    critical_chance = models.IntegerField(default=1)

    # ---------------------------------------------------------------------------------------------
    #       PERKS
    # ---------------------------------------------------------------------------------------------
    # These are bonus abilities that a player earned on level up. Each character has a list of perks.

    perks = models.ManyToManyField(Perk)

    # ---------------------------------------------------------------------------------------------
    #       CONDITION
    # ---------------------------------------------------------------------------------------------
    # The character's physical health, base armor class, and rads.

    hit_points = models.IntegerField(default=0)
    base_armor = models.IntegerField(default=0)
    rads = models.IntegerField(default=0, validators=[MaxValueValidator(1000), MinValueValidator(0)])

    # ---------------------------------------------------------------------------------------------
    #       EFFECTS
    # ---------------------------------------------------------------------------------------------
    # Radiation, combat effects, chem effects

    rad_effects = models.CharField(max_length=64)
    other_effects = models.CharField(max_length=256)

    # ---------------------------------------------------------------------------------------------
    #       LEVELING
    # ---------------------------------------------------------------------------------------------
    # Info relating to level up for character.

    level = models.IntegerField(default=1)

    # ---------------------------------------------------------------------------------------------
    #       WEAPON
    # ---------------------------------------------------------------------------------------------
    # Each character has a list of weapons that is separate from their inventory.

    # ---------------------------------------------------------------------------------------------
    #       ARMOR
    # ---------------------------------------------------------------------------------------------
    # Each character has a list of weapons that is separate from their inventory.

    # ---------------------------------------------------------------------------------------------
    #       INVENTORY
    # ---------------------------------------------------------------------------------------------

    def __str__(self):
        return self.name

class Weapon(models.Model):
    # A character can have many weapons.

    # ---------------------------------------------------------------------------------------------
    #       DEFINING CHOICES
    # ---------------------------------------------------------------------------------------------

    # Range of weapon
    CLOSE = "CL"
    SHORT = "SH"
    MEDIUM = "ME"
    LONG = "LO"

    RANGE_CHOICES = [
        ("CL", "Close"),
        ("SH", "Short"),
        ("ME", "Medium"),
        ("LO", "Long"),
    ]

    # Type of weapon
    ENERGY = "EN"
    GUNS = "GU"
    MELEE = "ME"
    UNARMED = "UN"

    TYPE_CHOICES = [
        ("EN", "Energy"),
        ("GU", "Guns"),
        ("ME", "Melee"),
        ("UN", "Unarmed"),
    ]

    # ---------------------------------------------------------------------------------------------

    # Who this weapon is associated with.
    owner = models.ForeignKey(Character, on_delete=models.CASCADE)

    # Name of weapon.
    name = models.CharField(max_length=64)

    # Type of weapon
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=ENERGY,
    )

    # Range of weapon (close is melee range)
    range = models.CharField(
        max_length=2,
        choices=RANGE_CHOICES,
        default=CLOSE,
    )

    # Damage per shot
    damage = models.IntegerField(default=0)

    # Burst fire capable?
    is_burst = models.BooleanField(default=False)

    # Action point costs for single shot, targeted shot, or burst
    ap_cost_single = models.IntegerField(default=0)
    ap_cost_targeted = models.IntegerField(default=0)
    ap_cost_burst = models.IntegerField(default=0)

    # Ammo
    ammo_count = models.IntegerField(default=0)
    ammo_type = models.CharField(max_length=24)
    ammo_per_shot = models.IntegerField(default=1)
    ammo_per_burst = models.IntegerField(default=3)

    # Special abilities
    special_abilities = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Armor(models.Model):
    # A character can have many pieces of armor.

    # ---------------------------------------------------------------------------------------------
    #       DEFINING CHOICES
    # ---------------------------------------------------------------------------------------------

    # Type of weapon
    UNARMORED = "UN"
    LIGHT = "LI"
    MEDIUM = "ME"
    HEAVY = "HE"

    TYPE_CHOICES = [
        ("UN", "Unarmored"),
        ("LI", "Light"),
        ("ME", "Medium"),
        ("HE", "Heavy"),
    ]

    # ---------------------------------------------------------------------------------------------

    # Who this armor is associated with
    owner = models.ForeignKey(Character, on_delete=models.CASCADE)

    # Name of armor
    name = models.CharField(max_length=64)

    # Type of armor. Med reduces agility by 1, heavy reduces agility by 2
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=UNARMORED,
    )

    # Effects on stats, special abilities
    effects = models.CharField(max_length=128)

    # Armor class
    armor_class = models.IntegerField(default=0)

    # Damage reduction
    damage_reduction = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    owner = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.name

class Inventory_Item(models.Model):
    owner_inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    value = models.IntegerField(default=0)
    notes = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]