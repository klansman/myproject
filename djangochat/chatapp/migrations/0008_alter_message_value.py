# Generated by Django 4.2.13 on 2024-07-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0007_rename_chatrooms_rooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='value',
            field=models.CharField(max_length=1000000),
        ),
    ]
