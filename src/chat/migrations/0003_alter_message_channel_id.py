# Generated by Django 5.0 on 2023-12-24 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_remove_message_id_alter_message_message_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='channel_id',
            field=models.IntegerField(default=0),
        ),
    ]
