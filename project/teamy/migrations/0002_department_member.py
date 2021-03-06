# Generated by Django 2.2.6 on 2019-10-27 12:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teamy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Department')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='First name')),
                ('last_name', models.CharField(max_length=20, verbose_name='Last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teamy.Department', verbose_name='Department')),
            ],
        ),
    ]
