# Generated by Django 4.2.3 on 2023-07-30 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_plattypususer_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plattypususer',
            name='gender',
            field=models.CharField(choices=[('Do not show', 'Do not show'), ('Female', 'Female'), ('Male', 'Male')], max_length=12),
        ),
    ]