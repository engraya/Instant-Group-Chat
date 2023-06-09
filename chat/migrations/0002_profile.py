# Generated by Django 4.1.3 on 2023-05-19 16:45

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=200, null=True)),
                ('lastName', models.CharField(blank=True, max_length=200, null=True)),
                ('date_of_birth', models.DateField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('profession', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images')),
                ('adress', models.CharField(blank=True, max_length=200, null=True)),
                ('phoneNumber', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
