# Generated by Django 4.2 on 2023-12-11 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_QA', '0002_dailytest_dailytestdraft_dailytestinput_dlynxconfig_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailytest',
            name='kfactor',
            field=models.DecimalField(blank=True, db_column='KFactor', decimal_places=3, max_digits=10, null=True),
        ),
    ]