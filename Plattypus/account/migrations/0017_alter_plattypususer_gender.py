# Generated by Django 4.2.3 on 2023-08-01 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_alter_plattypususer_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plattypususer',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show')], max_length=12),
        ),
    ]
