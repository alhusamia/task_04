# Generated by Django 2.1.5 on 2020-02-12 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20200212_1053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='title',
            new_name='name',
        ),
    ]
