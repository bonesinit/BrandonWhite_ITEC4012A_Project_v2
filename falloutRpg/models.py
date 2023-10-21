from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Perk(models.Model):
    # This model contains all of the data relating to the various perks in the game.
    # Perks are available based on whether or not characters satisfy various requirements.
    # Perks that are selected on level-up are added to the character sheet.

    # Name of the perk.
    name = models.CharField(max_length=32)

    # Description of what effect the perk has.
    description = models.CharField(max_length=256)

    # Character level requirement from 1-50.
    level_req = models.IntegerField(default=1)

    # Name of SPECIAL skill requirement (optional)
    special_skill_name = models.CharField(max_length=32, default="none")
    # Special skill requirement from 1-10.
    special_skill_req = models.IntegerField(default=0)

    # Name of first skill requirement (optional)
    skill_1_name = models.CharField(max_length=32, default="none")
    # Required value from 1-100
    skill_1_req = models.IntegerField(default=0)

    # Name of first second requirement (optional)
    skill_2_name = models.CharField(max_length=32, default="none")
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
    description = models.CharField(max_length=256)

    # Backstory of character.
    backstory = models.CharField(max_length=512)

    # Character level.
    level = models.IntegerField(default=1)

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

    # Strength
    stat_strength = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )

    # Perception
    stat_perception = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )

    # Endurance
    stat_endurance = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )

    # Charisma
    stat_charisma = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )

    # Intelligence
    stat_intelligence = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )

    # Agility
    stat_agility = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )

    # Luck
    stat_luck = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )

    # ---------------------------------------------------------------------------------------------
    #       SKILLS
    # ---------------------------------------------------------------------------------------------
    # These are the skills used for skill checks and combat.

    # Barter
    skill_barter = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    # Energy Weapons
    skill_energy_weapons = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    # Explosives
    skill_explosives = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    # Guns
    skill_guns = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    # Medicine
    skill_medicine = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    # Melee Weapons
    skill_melee_weapons = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    # Repair
    skill_repair = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    # Science
    skill_science = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    # Sneak
    skill_sneak = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    # Speech
    skill_speech = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    # Survival
    skill_survival = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    # Unarmed
    skill_unarmed = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    # ---------------------------------------------------------------------------------------------
    #       SECONDARY STATISTICS
    # ---------------------------------------------------------------------------------------------
    # These are statistics derived from the player's SPECIAL (primary) statistics.

    # Action Points
    action_points = models.IntegerField(default=1)

    # Poison Resistance
    poison_resistance = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(85),
            MinValueValidator(0)
        ]
    )

    # Radiation Resistance
    radiation_resistance = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(85),
            MinValueValidator(0)
        ]
    )

    # Critical Chance (%)
    critical_chance = models.IntegerField(default=1)

    # ---------------------------------------------------------------------------------------------
    #       PERKS
    # ---------------------------------------------------------------------------------------------
    # These are bonus abilities that a player earns on level up.

    # List of character's perks.
    perks = models.ManyToManyField(Perk)

    # ---------------------------------------------------------------------------------------------
    #       CONDITION
    # ---------------------------------------------------------------------------------------------
    # The character's physical health.

    # Hit points
    hit_points = models.IntegerField(default=0)

    # Rads
    rads = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(1000),
            MinValueValidator(0)
        ]
    )

    # ---------------------------------------------------------------------------------------------
    #       EFFECTS
    # ---------------------------------------------------------------------------------------------
    # These are effects caused by radiation sickness, intoxication, and damage types (poison, fire, frost, electric).

    # Radiation effects
    rad_effects = models.CharField(max_length=64)

    # Other effects, including chems
    other_effects = models.CharField(max_length=256)

    # Poison damage taken per round
    poison_dam = models.IntegerField(default=0)

    # Fire damage taken per round
    fire_dam = models.IntegerField(default=0)

    # Frost damage taken per round
    frost_dam = models.IntegerField(default=0)

    # Electric damage taken per round
    electric_dam = models.IntegerField(default=0)

    # ---------------------------------------------------------------------------------------------
    #       LEVELING
    # ---------------------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------------------
    #       EQUIPMENT
    # ---------------------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------------------
    #       INVENTORY
    # ---------------------------------------------------------------------------------------------



