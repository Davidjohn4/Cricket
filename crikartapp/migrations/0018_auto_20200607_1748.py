# Generated by Django 3.0.3 on 2020-06-07 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crikartapp', '0017_auto_20200607_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_register',
            name='team_logo',
            field=models.ImageField(upload_to='media/image'),
        ),
    ]
