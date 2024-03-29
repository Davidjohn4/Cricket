# Generated by Django 3.0.3 on 2020-03-24 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=30)),
                ('mobile_no', models.IntegerField()),
                ('message', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('zip_code', models.IntegerField()),
                ('mobile_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='player_register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=25)),
                ('player_email', models.CharField(max_length=25)),
                ('player_no', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='registaration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('password1', models.IntegerField()),
                ('password2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='sport_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=25)),
                ('category', models.CharField(max_length=25)),
                ('sub_category', models.CharField(max_length=25)),
                ('desc', models.CharField(max_length=50)),
                ('puch_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='media/image')),
            ],
        ),
        migrations.CreateModel(
            name='team_register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=25)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('college_name', models.CharField(max_length=50)),
                ('captain_name', models.CharField(max_length=25)),
                ('coach_name', models.CharField(max_length=25)),
                ('college_address', models.CharField(max_length=50)),
                ('email_id', models.CharField(max_length=25)),
                ('team_logo', models.ImageField(upload_to='media/image')),
                ('group', models.CharField(max_length=10)),
            ],
        ),
    ]
