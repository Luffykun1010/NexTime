# Generated by Django 4.2.7 on 2023-12-05 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatmessage',
            old_name='user',
            new_name='sended_by',
        ),
    ]