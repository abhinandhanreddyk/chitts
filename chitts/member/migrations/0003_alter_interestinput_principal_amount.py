# Generated by Django 5.0.1 on 2024-02-04 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_interestinput'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interestinput',
            name='principal_amount',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
