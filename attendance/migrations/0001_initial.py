# Generated by Django 3.1.7 on 2021-03-12 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=250)),
                ('lname', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('phone', models.IntegerField()),
                ('semester', models.IntegerField(blank=True, null=True)),
                ('gr_no', models.IntegerField(blank=True)),
                ('enrollment_no', models.IntegerField(blank=True)),
                ('branch', models.CharField(blank=True, max_length=25, null=True)),
                ('password', models.CharField(max_length=500)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Students',
                'db_table': 'Student',
                'ordering': ['-fname'],
            },
        ),
    ]