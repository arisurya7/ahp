# Generated by Django 3.2.8 on 2022-02-25 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weighting', '0002_responden_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responden',
            name='birth_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
