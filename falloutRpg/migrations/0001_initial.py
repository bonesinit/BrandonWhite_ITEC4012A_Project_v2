# Generated by Django 4.2.6 on 2023-10-21 19:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=512)),
                ('backstory', models.CharField(max_length=512)),
                ('karma', models.CharField(choices=[('VG', 'Very Good'), ('GO', 'Good'), ('NE', 'Neutral'), ('EV', 'Evil'), ('VE', 'Very Evil')], default='NE', max_length=2)),
                ('stat_strength', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('stat_perception', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('stat_endurance', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('stat_charisma', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('stat_intelligence', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('stat_agility', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('stat_luck', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('skill_barter', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('skill_energy_weapons', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('skill_explosives', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('skill_guns', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('skill_medicine', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('skill_melee_weapons', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('skill_repair', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('skill_science', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('skill_sneak', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('skill_speech', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('skill_survival', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('skill_unarmed', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('action_points', models.IntegerField(default=1)),
                ('poison_resistance', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(85), django.core.validators.MinValueValidator(0)])),
                ('radiation_resistance', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(85), django.core.validators.MinValueValidator(0)])),
                ('critical_chance', models.IntegerField(default=1)),
                ('hit_points', models.IntegerField(default=0)),
                ('base_armor', models.IntegerField(default=0)),
                ('rads', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('rad_effects', models.CharField(max_length=64)),
                ('other_effects', models.CharField(max_length=256)),
                ('level', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='falloutRpg.character')),
            ],
        ),
        migrations.CreateModel(
            name='Perk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=256)),
                ('level_req', models.IntegerField(default=1)),
                ('special_skill_name', models.CharField(default='none', max_length=32)),
                ('special_skill_req', models.IntegerField(default=0)),
                ('skill_1_name', models.CharField(default='none', max_length=32)),
                ('skill_1_req', models.IntegerField(default=0)),
                ('skill_2_name', models.CharField(default='none', max_length=32)),
                ('skill_2_req', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('type', models.CharField(choices=[('EN', 'Energy'), ('GU', 'Guns'), ('ME', 'Melee'), ('UN', 'Unarmed')], default='EN', max_length=2)),
                ('range', models.CharField(choices=[('CL', 'Close'), ('SH', 'Short'), ('ME', 'Medium'), ('LO', 'Long')], default='CL', max_length=2)),
                ('damage', models.IntegerField(default=0)),
                ('is_burst', models.BooleanField(default=False)),
                ('ap_cost_single', models.IntegerField(default=0)),
                ('ap_cost_targeted', models.IntegerField(default=0)),
                ('ap_cost_burst', models.IntegerField(default=0)),
                ('ammo_count', models.IntegerField(default=0)),
                ('ammo_type', models.CharField(max_length=24)),
                ('ammo_per_shot', models.IntegerField(default=1)),
                ('ammo_per_burst', models.IntegerField(default=3)),
                ('special_abilities', models.CharField(max_length=128)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='falloutRpg.character')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('value', models.IntegerField(default=0)),
                ('notes', models.CharField(max_length=256)),
                ('owner_inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='falloutRpg.inventory')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='character',
            name='perks',
            field=models.ManyToManyField(to='falloutRpg.perk'),
        ),
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('type', models.CharField(choices=[('UN', 'Unarmored'), ('LI', 'Light'), ('ME', 'Medium'), ('HE', 'Heavy')], default='UN', max_length=2)),
                ('effects', models.CharField(max_length=128)),
                ('armor_class', models.IntegerField(default=0)),
                ('damage_reduction', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='falloutRpg.character')),
            ],
        ),
    ]