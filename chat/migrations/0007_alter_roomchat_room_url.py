# Generated by Django 4.0.6 on 2022-07-17 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_roomchat_room_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomchat',
            name='room_url',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
