# Generated by Django 4.2.3 on 2023-07-30 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_plattypususer_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plattypususer',
            name='gender',
            field=models.CharField(choices=[('Do not show', 'Do not show'), ('Male', 'Male'), ('Female', 'Female')], max_length=12),
        ),
    ]
