# Generated by Django 4.2 on 2023-06-09 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_QA', '0003_remove_dailytest_lasers_dailytest_laserx_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyTestDraft',
            fields=[
                ('index', models.AutoField(db_column='Index', primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(db_column='Date_added')),
                ('gantry', models.IntegerField(db_column='Gantry', null=True)),
                ('visionrt_check', models.IntegerField(blank=True, db_column='VisionRT_check', null=True)),
                ('flatpanels_check', models.IntegerField(blank=True, db_column='FlatPanels_check', null=True)),
                ('dynr', models.IntegerField(blank=True, db_column='DynR', null=True)),
                ('laserx', models.IntegerField(blank=True, db_column='Laserx', null=True)),
                ('lasery', models.IntegerField(blank=True, db_column='Lasery', null=True)),
                ('laserz', models.IntegerField(blank=True, db_column='Laserz', null=True)),
                ('temperature', models.DecimalField(blank=True, db_column='Temperature', decimal_places=2, max_digits=10, null=True)),
                ('pressure', models.DecimalField(blank=True, db_column='Pressure', decimal_places=2, max_digits=10, null=True)),
                ('kfactor', models.DecimalField(blank=True, db_column='KFactor', decimal_places=3, max_digits=10, null=True)),
                ('lynxid', models.IntegerField(blank=True, db_column='LynxID', null=True)),
                ('lynx70_95', models.DecimalField(blank=True, db_column='Lynx70_95', decimal_places=3, max_digits=10, null=True)),
                ('lynx70_99', models.DecimalField(blank=True, db_column='Lynx70_99', decimal_places=3, max_digits=10, null=True)),
                ('lynx70_avg', models.DecimalField(blank=True, db_column='Lynx70_avg', decimal_places=3, max_digits=10, null=True)),
                ('lynx70_max', models.DecimalField(blank=True, db_column='Lynx70_max', decimal_places=3, max_digits=10, null=True)),
                ('lynx115_95', models.DecimalField(blank=True, db_column='Lynx115_95', decimal_places=3, max_digits=10, null=True)),
                ('lynx115_99', models.DecimalField(blank=True, db_column='Lynx115_99', decimal_places=3, max_digits=10, null=True)),
                ('lynx115_avg', models.DecimalField(blank=True, db_column='Lynx115_avg', decimal_places=3, max_digits=10, null=True)),
                ('lynx115_max', models.DecimalField(blank=True, db_column='Lynx115_max', decimal_places=3, max_digits=10, null=True)),
                ('lynx145_95', models.DecimalField(blank=True, db_column='Lynx145_95', decimal_places=3, max_digits=10, null=True)),
                ('lynx145_99', models.DecimalField(blank=True, db_column='Lynx145_99', decimal_places=3, max_digits=10, null=True)),
                ('lynx145_avg', models.DecimalField(blank=True, db_column='Lynx145_avg', decimal_places=3, max_digits=10, null=True)),
                ('lynx145_max', models.DecimalField(blank=True, db_column='Lynx145_max', decimal_places=3, max_digits=10, null=True)),
                ('lynx226_95', models.DecimalField(blank=True, db_column='Lynx226_95', decimal_places=3, max_digits=10, null=True)),
                ('lynx226_99', models.DecimalField(blank=True, db_column='Lynx226_99', decimal_places=3, max_digits=10, null=True)),
                ('lynx226_avg', models.DecimalField(blank=True, db_column='Lynx226_avg', decimal_places=3, max_digits=10, null=True)),
                ('lynx226_max', models.DecimalField(blank=True, db_column='Lynx226_max', decimal_places=3, max_digits=10, null=True)),
                ('icid', models.IntegerField(blank=True, db_column='IcID', null=True)),
                ('ic70_nc', models.DecimalField(blank=True, db_column='Ic70_nc', decimal_places=3, max_digits=10, null=True)),
                ('ic70_mu', models.DecimalField(blank=True, db_column='Ic70_MU', decimal_places=3, max_digits=10, null=True)),
                ('ic100_nc', models.DecimalField(blank=True, db_column='Ic100_nc', decimal_places=3, max_digits=10, null=True)),
                ('ic100_mu', models.DecimalField(blank=True, db_column='Ic100_MU', decimal_places=3, max_digits=10, null=True)),
                ('ic170_nc', models.DecimalField(blank=True, db_column='Ic170_nc', decimal_places=3, max_digits=10, null=True)),
                ('ic170_mu', models.DecimalField(blank=True, db_column='Ic170_MU', decimal_places=3, max_digits=10, null=True)),
                ('ic226_nc', models.DecimalField(blank=True, db_column='Ic226_nc', decimal_places=3, max_digits=10, null=True)),
                ('ic226_mu', models.DecimalField(blank=True, db_column='Ic226_MU', decimal_places=3, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'daily_test_draft',
                'db_table_comment': 'Lasers stored as binary number (0-x, 1-z, 2-y)',
                'managed': True,
            },
        ),
    ]
