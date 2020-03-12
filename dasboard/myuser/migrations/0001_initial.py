# Generated by Django 3.0.4 on 2020-03-12 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benutzer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(max_length=64, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=64, verbose_name='Last Name')),
                ('role', models.CharField(blank=True, choices=[('admin', 'Admin'), ('mitarbeiter', 'Mitarbeiter'), ('Assissenzt', 'Assissenzt')], max_length=20, null=True, verbose_name='Role')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Is Admin')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is Staff')),
                ('email_verified', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date joined')),
                ('title', models.CharField(blank=True, choices=[('dr', 'Dr'), ('Prof', 'prof'), ('other', 'Sonstiges')], max_length=10, null=True, verbose_name='Title')),
                ('no_password_set', models.BooleanField(default=False, help_text='Forces to change password on login', verbose_name='No password set')),
            ],
            options={
                'verbose_name': 'Email user',
                'verbose_name_plural': 'Email users',
            },
        ),
    ]