# Generated by Django 5.0.4 on 2024-04-19 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='usertype',
            field=models.CharField(default='user', max_length=100),
        ),
    ]
