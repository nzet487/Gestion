# Generated by Django 5.2 on 2025-04-06 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='prixUnitaire',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
