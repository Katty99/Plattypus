# Generated by Django 4.2.3 on 2023-08-01 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0006_delete_notes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='income',
            old_name='source',
            new_name='category',
        ),
    ]
