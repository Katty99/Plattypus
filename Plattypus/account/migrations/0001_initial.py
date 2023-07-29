# Generated by Django 4.2.3 on 2023-07-27 09:28

import Plattypus.account.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('age', models.IntegerField(validators=[Plattypus.account.validators.minimum_age_validator])),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
