# Generated by Django 4.2.3 on 2023-07-30 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_plattypususer_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plattypususer',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]
