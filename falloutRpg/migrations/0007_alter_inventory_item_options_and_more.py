# Generated by Django 4.2.6 on 2023-10-30 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('falloutRpg', '0006_character_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory_item',
            options={},
        ),
        migrations.AlterField(
            model_name='inventory_item',
            name='owner_inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='falloutRpg.character'),
        ),
        migrations.DeleteModel(
            name='Inventory',
        ),
    ]
