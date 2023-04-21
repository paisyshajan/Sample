# Generated by Django 4.2 on 2023-04-20 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0003_branch_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='phone_number',
            new_name='phone_no',
        ),
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.TextField(default=125452, max_length=250),
            preserve_default=False,
        ),
    ]
