# Generated by Django 4.1.4 on 2024-01-20 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMS_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='E_Name',
            new_name='Last_Name',
        ),
        migrations.AddField(
            model_name='employee',
            name='First_Name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
