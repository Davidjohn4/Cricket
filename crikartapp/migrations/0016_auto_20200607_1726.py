# Generated by Django 3.0.3 on 2020-06-07 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crikartapp', '0015_delete_registaration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_register',
            name='team_logo',
            field=models.ImageField(upload_to='media/images'),
        ),
    ]