# Generated by Django 4.2 on 2023-04-19 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_alter_person_branch_alter_person_district_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='state',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='bankapp.state'),
            preserve_default=False,
        ),
    ]
