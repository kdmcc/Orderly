# Generated by Django 3.0.6 on 2020-05-19 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chorescheduling', '0004_remove_household_linked_shedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choreinfo',
            name='completed',
        ),
        migrations.AddField(
            model_name='chore',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]