# Generated by Django 4.2 on 2023-04-20 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0006_rename_phone_no_person_phoneno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='phoneno',
            new_name='phone',
        ),
    ]
