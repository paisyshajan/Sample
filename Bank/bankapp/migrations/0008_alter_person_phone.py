# Generated by Django 4.2 on 2023-04-20 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0007_rename_phoneno_person_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.IntegerField(max_length=15),
        ),
    ]