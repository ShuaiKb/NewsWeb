# Generated by Django 3.1.3 on 2021-02-18 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MinTest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='classes_id',
            new_name='classes',
        ),
    ]