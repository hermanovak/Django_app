# Generated by Django 4.2 on 2023-06-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_QA', '0002_alter_dailytestinput_indexid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailytest',
            name='lasers',
        ),
        migrations.AddField(
            model_name='dailytest',
            name='laserx',
            field=models.IntegerField(blank=True, db_column='Laserx', null=True),
        ),
        migrations.AddField(
            model_name='dailytest',
            name='lasery',
            field=models.IntegerField(blank=True, db_column='Lasery', null=True),
        ),
        migrations.AddField(
            model_name='dailytest',
            name='laserz',
            field=models.IntegerField(blank=True, db_column='Laserz', null=True),
        ),
    ]
