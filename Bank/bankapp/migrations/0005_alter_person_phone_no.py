# Generated by Django 4.2 on 2023-04-20 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0004_rename_phone_number_person_phone_no_person_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone_no',
            field=models.CharField(max_length=15),
        ),
    ]
