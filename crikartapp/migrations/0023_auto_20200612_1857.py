# Generated by Django 3.0.3 on 2020-06-12 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crikartapp', '0022_auto_20200612_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player_register',
            name='date',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='team_register',
            name='team_logo',
            field=models.ImageField(upload_to='upload/image'),
        ),
    ]
