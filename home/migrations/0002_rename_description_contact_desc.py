# Generated by Django 4.2.2 on 2023-06-11 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='description',
            new_name='desc',
        ),
    ]
