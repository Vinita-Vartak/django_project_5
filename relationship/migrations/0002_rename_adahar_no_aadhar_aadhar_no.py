# Generated by Django 4.2.1 on 2023-06-23 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationship', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aadhar',
            old_name='adahar_no',
            new_name='aadhar_no',
        ),
    ]
