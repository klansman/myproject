# Generated by Django 4.2.13 on 2024-07-23 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0005_alter_message_value'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chatroom',
            new_name='Chatrooms',
        ),
    ]
