# Generated by Django 4.0.6 on 2022-07-17 22:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
