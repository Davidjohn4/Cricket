# Generated by Django 3.0.3 on 2020-06-12 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crikartapp', '0020_auto_20200607_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_register',
            name='date',
            field=models.DateField(default=''),
        ),
    ]