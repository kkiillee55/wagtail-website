# Generated by Django 3.0.8 on 2020-08-16 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moment',
            old_name='data',
            new_name='date',
        ),
    ]
