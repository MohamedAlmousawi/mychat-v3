# Generated by Django 3.2.15 on 2022-09-03 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_message_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomchat',
            name='secret_key',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
