# Generated by Django 4.2.3 on 2023-07-30 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0002_expense_to_profile_income_to_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='to_profile',
            new_name='user_profile',
        ),
        migrations.RenameField(
            model_name='income',
            old_name='to_profile',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='income',
            name='amount',
            field=models.FloatField(),
        ),
    ]
