# Generated by Django 4.2.3 on 2023-07-30 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_plattypususer_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plattypususer',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Do not show', 'Do not show'), ('Female', 'Female')], max_length=12),
        ),
        migrations.AlterField(
            model_name='plattypususer',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
