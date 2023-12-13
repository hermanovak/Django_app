# Generated by Django 4.2 on 2023-12-13 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DIcConfig',
            fields=[
                ('configid', models.IntegerField(db_column='configID', primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('label', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'd_ic_config',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DIcDavkaReference',
            fields=[
                ('index', models.AutoField(db_column='Index', primary_key=True, serialize=False)),
                ('gantry', models.IntegerField(blank=True, db_column='Gantry', null=True)),
                ('energy_mev_field', models.IntegerField(db_column='Energy[MeV]')),
                ('version', models.IntegerField(blank=True, null=True)),
                ('ref_dose_corric2_gy_field', models.DecimalField(blank=True, db_column='Ref.dose.corrIC2[Gy]', decimal_places=5, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'd_ic_davka_reference',
                'db_table_comment': 'FBTR1: IK 3190 s Dose 1 16101\nGTR2: IK 4218 s Dose 1 16091\nGTR3: IK 5414 s Dose 1 14485\nGTR4: IK 5414 s Dose 1 16098',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DIcKoefReference',
            fields=[
                ('sn', models.IntegerField(db_column='SN', primary_key=True, serialize=False)),
                ('ic', models.CharField(db_column='IC', max_length=20)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('gantry', models.CharField(blank=True, db_column='Gantry', max_length=10, null=True)),
                ('ndw', models.IntegerField(db_column='Ndw')),
                ('ksat', models.DecimalField(db_column='Ksat', decimal_places=4, max_digits=10)),
                ('kpol', models.DecimalField(db_column='Kpol', decimal_places=4, max_digits=10)),
                ('kqq0', models.DecimalField(db_column='kQQ0', decimal_places=4, max_digits=10)),
                ('ref_response_corr_for_t_and_p', models.DecimalField(blank=True, db_column='Ref.response.corr.for.T.and.P', decimal_places=4, max_digits=10, null=True)),
                ('ref_response_date', models.DateField(blank=True, db_column='Ref.response.date', null=True)),
                ('cert_with_electrometer', models.CharField(blank=True, db_column='Cert.with.electrometer', max_length=45, null=True)),
                ('cert_for_voltage', models.IntegerField(blank=True, db_column='Cert.for.voltage', null=True)),
                ('cert_validity', models.DateField(blank=True, db_column='Cert.validity', null=True)),
                ('number_90sr_ref_value', models.DecimalField(blank=True, db_column='90Sr.ref.value', decimal_places=4, max_digits=10, null=True)),
                ('number_90sr_ref_value_date', models.DateField(blank=True, db_column='90Sr.ref.value.date', null=True)),
            ],
            options={
                'db_table': 'd_ic_koef_reference',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DMlicConfig',
            fields=[
                ('configid', models.IntegerField(db_column='configID', primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('label', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'd_mlic_config',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DMlicReference',
            fields=[
                ('index', models.AutoField(db_column='Index', primary_key=True, serialize=False)),
                ('e_mev_field', models.IntegerField(db_column='E [MeV]')),
                ('gantry', models.IntegerField(blank=True, db_column='Gantry', null=True)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('ref_90_g_cm2_field', models.DecimalField(blank=True, db_column='Ref 90 [g/cm2]', decimal_places=2, max_digits=10, null=True)),
                ('ref_distal_spad_g_cm2_field', models.DecimalField(blank=True, db_column='Ref distal spad [g/cm2]', decimal_places=3, max_digits=10, null=True)),
                ('dosah_na_vstupu_nozzle_g_cm2_field', models.DecimalField(blank=True, db_column='Dosah na vstupu nozzle [g/cm2]', decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'd_mlic_reference',
                'db_table_comment': 'MLIC SN18206 (k datu 1/2023) \\nRef 90 u energi� 100,170,226 se pou��v� p�� denn�\n',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Energie',
            fields=[
                ('index', models.AutoField(db_column='Index', primary_key=True, serialize=False)),
                ('gantry', models.IntegerField(blank=True, db_column='Gantry', null=True)),
                ('test', models.CharField(blank=True, db_column='Test', max_length=45, null=True)),
                ('device', models.CharField(blank=True, db_column='Device', max_length=45, null=True)),
                ('energie', models.IntegerField(blank=True, db_column='Energie', null=True)),
            ],
            options={
                'db_table': 'energie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MDosimetryConfig',
            fields=[
                ('configid', models.IntegerField(db_column='configID', primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('label', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'm_dosimetry_config',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MDosimetryMeasurement',
            fields=[
                ('measurementid', models.IntegerField(db_column='measurementID', primary_key=True, serialize=False)),
                ('energy_mev_field', models.IntegerField(blank=True, db_column='energy [MeV]', null=True)),
                ('value', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'm_dosimetry_measurement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MFlatpanelsReproducibilityConfig',
            fields=[
                ('configid', models.IntegerField(db_column='configID', primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('uhel', models.IntegerField(blank=True, null=True)),
                ('label', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'm_flatpanels.reproducibility_config',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MFlatpanelsReproducibilityMeasurement',
            fields=[
                ('measurementid', models.IntegerField(db_column='measurementID', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'm_flatpanels.reproducibility_measurement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MIgrtContrastResolutionConfig',
            fields=[
                ('configid', models.IntegerField(db_column='configID', primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('label', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'm_igrt.contrast.resolution_config',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MIgrtContrastResolutionMeasurement',
            fields=[
                ('measurementid', models.IntegerField(db_column='measurementID', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'm_igrt.contrast.resolution_measurement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MonthlyTest',
            fields=[
                ('field_index', models.AutoField(db_column=' Index', primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(db_column='Date_added')),
                ('gantry', models.IntegerField(db_column='Gantry')),
                ('pps_table_position_0_2_field', models.IntegerField(blank=True, db_column='PPS.table.position(0-2)', null=True)),
                ('pps_collision_test_0_7_field', models.IntegerField(blank=True, db_column='PPS.collision.test(0-7)', null=True)),
            ],
            options={
                'db_table': 'monthly_test',
                'db_table_comment': 'pozice stolu: 0-pokles vysky stolu po 10min, 1-rotace stolu uhel1, rotace stolu uhel2\nkolize: 0-PPS JOG prime sily, 1-PPS JOG momenty, 2-PPS JOG ramena, 3-SNOUT JOG prime sily, 4-PPS GOTO prime sily',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MPpsMotionTestConfig',
            fields=[
                ('configid', models.IntegerField(db_column='configID', primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('namerene_hodnoty_kg_field', models.IntegerField(blank=True, db_column='Nam��en� hodnoty se z�t�� [kg]', null=True)),
                ('label', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'm_pps.motion.test_config',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MPpsMotionTestMeasurement',
            fields=[
                ('measurementid', models.IntegerField(db_column='measurementID', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'm_pps.motion.test_measurement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeeklyTest',
            fields=[
                ('index', models.AutoField(db_column='Index', primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(db_column='Date_added')),
                ('gantry', models.IntegerField(db_column='Gantry')),
                ('lasers_0_7_field', models.IntegerField(db_column='Lasers(0-7)')),
            ],
            options={
                'db_table': 'weekly_test',
                'db_table_comment': 'Lasers (0-horn� na nozzlu, 1-doln� na nozzlu, 2-vertik�ln� na st�n� gtr, 3-horizont�ln� na st�n� gtr, 4-stropn�, 5-bo�n� na zdi, 6-bo�n� na nozzlu, 7-vz�jemn� odchylka v izocentru)',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WGantryAngleVerificationConfig',
            fields=[
                ('configid', models.IntegerField(db_column='configID', primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('label', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'w_gantry.angle.verification_config',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WGantryAngleVerificationMeasurement',
            fields=[
                ('measurementid', models.IntegerField(db_column='measurementID', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'w_gantry.angle.verification_measurement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WIgrtCorrectionVectorConfig',
            fields=[
                ('configid', models.IntegerField(db_column='configID', primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('label', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'w_igrt.correction.vector_config',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WIgrtCorrectionVectorMeasurement',
            fields=[
                ('measurementid', models.IntegerField(db_column='measurementID', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'w_igrt.correction.vector_measurement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WLasersIsocenterAgreementConfig',
            fields=[
                ('configid', models.IntegerField(db_column='configID', primary_key=True, serialize=False)),
                ('version', models.IntegerField()),
                ('label', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'w_lasers.isocenter.agreement_config',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WLasersIsocenterAgreementMeasurement',
            fields=[
                ('measurementid', models.IntegerField(db_column='measurementID', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'w_lasers.isocenter.agreement_measurement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WRtgProtonbeamAlignmentConfig',
            fields=[
                ('configid', models.IntegerField(db_column='configID', primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('label', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'w_rtg.protonbeam.alignment_config',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WRtgProtonbeamAlignmentMeasurement',
            fields=[
                ('measurementid', models.IntegerField(db_column='measurementID', primary_key=True, serialize=False)),
                ('lynxid', models.IntegerField(blank=True, db_column='LynxID', null=True)),
                ('value', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'w_rtg.protonbeam.alignment_measurement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WRtgProtonbeamAlignmentReference',
            fields=[
                ('index', models.AutoField(db_column='Index', primary_key=True, serialize=False)),
                ('skutecny_uhel_gantry', models.IntegerField(blank=True, db_column='skutecny uhel gantry', null=True)),
                ('gantry', models.IntegerField(blank=True, db_column='Gantry', null=True)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('posun', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'w_rtg.protonbeam.alignment_reference',
                'db_table_comment': 'vektor posuny',
                'managed': False,
            },
        ),
    ]
