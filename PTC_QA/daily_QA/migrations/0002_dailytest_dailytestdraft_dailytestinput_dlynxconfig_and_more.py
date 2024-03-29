# Generated by Django 4.2 on 2023-12-13 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daily_QA', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyTest',
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
            ],
            options={
                'db_table': 'daily_test',
                'db_table_comment': 'Lasers stored as binary number (0-x, 1-z, 2-y)',
                'managed': True,
            },
        ),
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
                ('mlicid', models.IntegerField(blank=True, db_column='MlicID', null=True)),
                ('mlic70_range', models.DecimalField(blank=True, db_column='Mlic70_range', decimal_places=3, max_digits=10, null=True)),
                ('mlic100_range', models.DecimalField(blank=True, db_column='Mlic100_range', decimal_places=3, max_digits=10, null=True)),
                ('mlic170_range', models.DecimalField(blank=True, db_column='Mlic170_range', decimal_places=3, max_digits=10, null=True)),
                ('mlic226_range', models.DecimalField(blank=True, db_column='Mlic226_range', decimal_places=3, max_digits=10, null=True)),
                ('validate', models.IntegerField(blank=True, db_column='Validate', null=True)),
            ],
            options={
                'db_table': 'daily_test_draft',
                'db_table_comment': 'Lasers stored as binary number (0-x, 1-z, 2-y)',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DailyTestInput',
            fields=[
                ('index', models.AutoField(db_column='Index', primary_key=True, serialize=False)),
                ('energyID', models.IntegerField(db_column='energyID', null=True)),
                ('input1', models.DecimalField(blank=True, db_column='input1', decimal_places=4, max_digits=10, null=True)),
                ('input2', models.DecimalField(blank=True, db_column='input2', decimal_places=4, max_digits=10, null=True)),
                ('input3', models.DecimalField(blank=True, db_column='input3', decimal_places=4, max_digits=10, null=True)),
                ('input4', models.DecimalField(blank=True, db_column='input4', decimal_places=4, max_digits=10, null=True)),
                ('configID', models.IntegerField(db_column='configID', default=0)),
            ],
            options={
                'db_table': 'daily_test_input',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DLynxConfig',
            fields=[
                ('configid', models.IntegerField(db_column='configID', primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('label', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'd_lynx_config',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DLynxReference',
            fields=[
                ('index', models.IntegerField(db_column='Index', primary_key=True, serialize=False)),
                ('lynx', models.CharField(db_column='Lynx', max_length=25)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('iris', models.IntegerField(blank=True, db_column='Iris', null=True)),
                ('reference_maps', models.CharField(blank=True, max_length=45, null=True)),
                ('reference_maps_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'd_lynx_reference',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DMlicMeasurement',
            fields=[
                ('index', models.AutoField(db_column='Index', primary_key=True, serialize=False)),
                ('mlicid', models.IntegerField(blank=True, db_column='MlicID', null=True)),
                ('energy', models.IntegerField(blank=True, null=True)),
                ('range', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('measurementid', models.ForeignKey(blank=True, db_column='measurementid', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='daily_QA.dailytest')),
            ],
            options={
                'db_table': 'd_mlic_measurement',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DLynxMeasurement',
            fields=[
                ('index', models.AutoField(db_column='Index', primary_key=True, serialize=False)),
                ('val95', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('val99', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('avg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('max', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('lynxid', models.IntegerField(blank=True, db_column='LynxID', null=True)),
                ('energy', models.IntegerField(blank=True, null=True)),
                ('measurementid', models.ForeignKey(blank=True, db_column='measurementid', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='daily_QA.dailytest')),
            ],
            options={
                'db_table': 'd_lynx_measurement',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DIcMeasurement',
            fields=[
                ('index', models.AutoField(db_column='Index', primary_key=True, serialize=False)),
                ('ic_id', models.IntegerField(blank=True, db_column='IC_ID', null=True)),
                ('energy', models.IntegerField(blank=True, null=True)),
                ('response_nc', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('response_mu', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('measurementid', models.ForeignKey(blank=True, db_column='measurementid', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='daily_QA.dailytest')),
            ],
            options={
                'db_table': 'd_ic_measurement',
                'managed': True,
            },
        ),
    ]
