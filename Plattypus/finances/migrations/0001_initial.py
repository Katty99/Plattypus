# Generated by Django 4.2.3 on 2023-07-27 09:28

import Plattypus.finances.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(validators=[Plattypus.finances.validators.minimum_income])),
                ('currency', models.CharField(choices=[('BGN', 'BGN'), ('EUR', 'EUR'), ('USD', 'USD'), ('CHF', 'CHF'), ('CAD', 'CAD'), ('AUD', 'AUD'), ('INR', 'INR'), ('JPY', 'JPY')])),
                ('details', models.CharField(blank=True, null=True)),
                ('to_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('currency', models.CharField(choices=[('BGN', 'BGN'), ('EUR', 'EUR'), ('USD', 'USD'), ('CHF', 'CHF'), ('CAD', 'CAD'), ('AUD', 'AUD'), ('INR', 'INR'), ('JPY', 'JPY')])),
                ('category', models.CharField(choices=[('Household', 'Household'), ('Transport', 'Transport'), ('Food', 'Food'), ('Utilities', 'Utilities'), ('Clothing', 'Clothing'), ('Skincare', 'Skincare'), ('Insurance', 'Insurance'), ('Healthcare', 'Healthcare'), ('Personal', 'Personal'), ('Debt', 'Debt'), ('Retirement', 'Retirement'), ('Savings', 'Savings'), ('Education', 'Education'), ('Entertainment', 'Entertainment'), ('Savings', 'Savings'), ('Travel', 'Travel'), ('Other', 'Other')])),
                ('details', models.CharField(blank=True, null=True)),
                ('to_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
    ]