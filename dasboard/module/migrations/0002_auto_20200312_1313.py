# Generated by Django 3.0.4 on 2020-03-12 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='module',
            field=models.CharField(max_length=128, verbose_name='Modulname'),
        ),
        migrations.AlterField(
            model_name='module',
            name='module_id',
            field=models.CharField(max_length=64, null=True, unique=True, verbose_name='Module ID'),
        ),
        migrations.AlterField(
            model_name='module',
            name='module_wahl',
            field=models.CharField(blank=True, choices=[('soa', 'SOA'), ('WPR', ' WPR'), ('ALGEBRA', 'ALGEBRA'), ('ALNALSIS', 'ALNALSIS'), ('JAVA', 'JAVA'), ('WIRTSCHAFTSINFORMATIK', 'WIRTSCHAFTSINFORMATIK'), ('BWL', 'BWL')], max_length=100, verbose_name='Fach'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='student_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owners', to='module.Module', verbose_name='Module'),
        ),
    ]