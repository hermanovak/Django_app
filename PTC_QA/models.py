# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class DailyTest(models.Model):
    index = models.AutoField(db_column='Index', primary_key=True)  # Field name made lowercase.
    date_added = models.DateTimeField(db_column='Date_added')  # Field name made lowercase.
    gantry = models.IntegerField(db_column='Gantry', null=True)  # Field name made lowercase.
    visionrt_check = models.IntegerField(db_column='VisionRT_check', blank=True, null=True)  # Field name made lowercase.
    flatpanels_check = models.IntegerField(db_column='FlatPanels_check', blank=True, null=True)  # Field name made lowercase.
    dynr = models.IntegerField(db_column='DynR', blank=True, null=True)  # Field name made lowercase.
    laserx = models.IntegerField(db_column='Laserx', blank=True, null=True)  # Field name made lowercase.
    lasery = models.IntegerField(db_column='Lasery', blank=True, null=True)
    laserz = models.IntegerField(db_column='Laserz', blank=True, null=True)
    temperature = models.DecimalField(db_column='Temperature', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pressure = models.DecimalField(db_column='Pressure', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    kfactor = models.DecimalField(db_column='KFactor', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    
    #def __str__(self):
    #    return f'This record is from {self.date_added.date()} and gantry #{self.gantry}'

class DIcDavkaReference(models.Model):
    index = models.AutoField(db_column='Index', primary_key=True)  # Field name made lowercase.
    gantry = models.IntegerField(db_column='Gantry', blank=True, null=True)  # Field name made lowercase.
    energy_mev_field = models.IntegerField(db_column='Energy[MeV]')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    version = models.IntegerField(blank=True, null=True)
    ref_dose_corric2_gy_field = models.DecimalField(db_column='Ref.dose.corrIC2[Gy]', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'd_ic_davka_reference'
        db_table_comment = 'FBTR1: IK 3190 s Dose 1 16101\nGTR2: IK 4218 s Dose 1 16091\nGTR3: IK 5414 s Dose 1 14485\nGTR4: IK 5414 s Dose 1 16098'


class DIcKoefReference(models.Model):
    sn = models.IntegerField(db_column='SN', primary_key=True)  # Field name made lowercase.
    ic = models.CharField(db_column='IC', max_length=20)  # Field name made lowercase.
    version = models.IntegerField(blank=True, null=True)
    gantry = models.CharField(db_column='Gantry', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ndw = models.IntegerField(db_column='Ndw')  # Field name made lowercase.
    ksat = models.DecimalField(db_column='Ksat', max_digits=10, decimal_places=4)  # Field name made lowercase.
    kpol = models.DecimalField(db_column='Kpol', max_digits=10, decimal_places=4)  # Field name made lowercase.
    kqq0 = models.DecimalField(db_column='kQQ0', max_digits=10, decimal_places=4)  # Field name made lowercase.
    ref_response_corr_for_t_and_p = models.DecimalField(db_column='Ref.response.corr.for.T.and.P', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ref_response_date = models.DateField(db_column='Ref.response.date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cert_with_electrometer = models.CharField(db_column='Cert.with.electrometer', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cert_for_voltage = models.IntegerField(db_column='Cert.for.voltage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cert_validity = models.DateField(db_column='Cert.validity', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_90sr_ref_value = models.DecimalField(db_column='90Sr.ref.value', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_90sr_ref_value_date = models.DateField(db_column='90Sr.ref.value.date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'd_ic_koef_reference'


class DIcMeasurement(models.Model):
    index = models.AutoField(db_column='Index', primary_key=True)
    measurementid = models.ForeignKey(DailyTest, db_column='measurementid', on_delete=models.CASCADE, null=True, blank=True, default=None)
    #configid = models.ForeignKey(DIcConfig, models.DO_NOTHING, db_column='configID', blank=True, null=True)  # Field name made lowercase.
    ic_id = models.IntegerField(db_column='IC_ID', blank=True, null=True)  # Field name made lowercase.
    energy = models.IntegerField(blank=True, null=True)
    response_nc = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    response_mu = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'd_ic_measurement'


class DLynxMeasurement(models.Model):
    index = models.AutoField(db_column='Index', primary_key=True)  # Field name made lowercase.
    measurementid = models.ForeignKey(DailyTest, db_column='measurementid', on_delete=models.CASCADE, null=True, blank=True, default=None)  # Field name made lowercase.
    val95 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    val99 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    avg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    max = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    lynxid = models.IntegerField(db_column='LynxID', blank=True, null=True)  # Field name made lowercase.
    energy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'd_lynx_measurement'


class DLynxReference(models.Model):
    index = models.IntegerField(db_column='Index', primary_key=True)  # Field name made lowercase.
    lynx = models.CharField(db_column='Lynx', max_length=25)  # Field name made lowercase.
    version = models.IntegerField(blank=True, null=True)
    iris = models.IntegerField(db_column='Iris', blank=True, null=True)  # Field name made lowercase.
    reference_maps = models.CharField(max_length=45, blank=True, null=True)
    reference_maps_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_lynx_reference'


class DMlicMeasurement(models.Model):
    index = models.AutoField(db_column='Index', primary_key=True)
    measurementid = models.ForeignKey(DailyTest, db_column='measurementid', on_delete=models.CASCADE, null=True, blank=True, default=None)
    mlicid = models.IntegerField(db_column='MlicID', blank=True, null=True)
    energy = models.IntegerField(blank=True, null=True)
    range = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'd_mlic_measurement'


class DMlicReference(models.Model):
    index = models.AutoField(db_column='Index', primary_key=True)  # Field name made lowercase.
    e_mev_field = models.IntegerField(db_column='E [MeV]')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    gantry = models.IntegerField(db_column='Gantry', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(blank=True, null=True)
    ref_90_g_cm2_field = models.DecimalField(db_column='Ref 90 [g/cm2]', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ref_distal_spad_g_cm2_field = models.DecimalField(db_column='Ref distal spad [g/cm2]', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    dosah_na_vstupu_nozzle_g_cm2_field = models.DecimalField(db_column='Dosah na vstupu nozzle [g/cm2]', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'd_mlic_reference'
        db_table_comment = 'MLIC SN18206 (k datu 1/2023) \\nRef 90 u energi� 100,170,226 se pou��v� p�� denn�\n'





class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MDosimetryConfig(models.Model):
    configid = models.IntegerField(db_column='configID', primary_key=True)  # Field name made lowercase.
    version = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_dosimetry_config'


class MDosimetryMeasurement(models.Model):
    measurementid = models.IntegerField(db_column='measurementID', primary_key=True)  # Field name made lowercase.
    configid = models.ForeignKey(MDosimetryConfig, models.DO_NOTHING, db_column='configID', blank=True, null=True)  # Field name made lowercase.
    energy_mev_field = models.IntegerField(db_column='energy [MeV]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    value = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_dosimetry_measurement'


class MFlatpanelsReproducibilityConfig(models.Model):
    configid = models.IntegerField(db_column='configID', primary_key=True)  # Field name made lowercase.
    version = models.IntegerField(blank=True, null=True)
    angle = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_flatpanels.reproducibility_config'


class MFlatpanelsReproducibilityMeasurement(models.Model):
    measurementid = models.IntegerField(db_column='measurementID', primary_key=True)  # Field name made lowercase.
    configid = models.ForeignKey(MFlatpanelsReproducibilityConfig, models.DO_NOTHING, db_column='configID', blank=True, null=True)  # Field name made lowercase.
    value = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_flatpanels.reproducibility_measurement'


class MIgrtContrastResolutionConfig(models.Model):
    configid = models.IntegerField(db_column='configID', primary_key=True)  # Field name made lowercase.
    version = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_igrt.contrast.resolution_config'


class MIgrtContrastResolutionMeasurement(models.Model):
    measurementid = models.IntegerField(db_column='measurementID', primary_key=True)  # Field name made lowercase.
    configid = models.ForeignKey(MIgrtContrastResolutionConfig, models.DO_NOTHING, db_column='configID', blank=True, null=True)  # Field name made lowercase.
    value = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_igrt.contrast.resolution_measurement'


class MPpsMotionTestConfig(models.Model):
    configid = models.IntegerField(db_column='configID', primary_key=True)  # Field name made lowercase.
    version = models.IntegerField(blank=True, null=True)
    #nam��en�_hodnoty_se_z�t��_kg_field = models.IntegerField(db_column='Nam��en� hodnoty se z�t�� [kg]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    label = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_pps.motion.test_config'


class MPpsMotionTestMeasurement(models.Model):
    measurementid = models.IntegerField(db_column='measurementID', primary_key=True)  # Field name made lowercase.
    configid = models.ForeignKey(MPpsMotionTestConfig, models.DO_NOTHING, db_column='configID', blank=True, null=True)  # Field name made lowercase.
    value = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_pps.motion.test_measurement'


class MonthlyTest(models.Model):
    field_index = models.AutoField(db_column=' Index', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    date_added = models.DateTimeField(db_column='Date_added')  # Field name made lowercase.
    gantry = models.IntegerField(db_column='Gantry')  # Field name made lowercase.
    igrt_contrast_resolution_measurementid = models.ForeignKey(MIgrtContrastResolutionMeasurement, models.DO_NOTHING, db_column='IGRT.contrast.resolution_measurementID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    flatpanels_reproducibility_measurementid = models.ForeignKey(MFlatpanelsReproducibilityMeasurement, models.DO_NOTHING, db_column='FlatPanels.reproducibility_measurementID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pps_motion_test_measurementid = models.ForeignKey(MPpsMotionTestMeasurement, models.DO_NOTHING, db_column='PPS.motion.test_measurementID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pps_table_position_0_2_field = models.IntegerField(db_column='PPS.table.position(0-2)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    pps_collision_test_0_7_field = models.IntegerField(db_column='PPS.collision.test(0-7)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    dosimetry_measurementid = models.ForeignKey(MDosimetryMeasurement, models.DO_NOTHING, db_column='Dosimetry_measurementID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'monthly_test'
        db_table_comment = 'pozice stolu: 0-pokles vysky stolu po 10min, 1-rotace stolu uhel1, rotace stolu uhel2\nkolize: 0-PPS JOG prime sily, 1-PPS JOG momenty, 2-PPS JOG ramena, 3-SNOUT JOG prime sily, 4-PPS GOTO prime sily'


class WGantryAngleVerificationConfig(models.Model):
    configid = models.IntegerField(db_column='configID', primary_key=True)  # Field name made lowercase.
    version = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'w_gantry.angle.verification_config'


class WGantryAngleVerificationMeasurement(models.Model):
    measurementid = models.IntegerField(db_column='measurementID', primary_key=True)  # Field name made lowercase.
    configid = models.ForeignKey(WGantryAngleVerificationConfig, models.DO_NOTHING, db_column='configID', blank=True, null=True)  # Field name made lowercase.
    value = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'w_gantry.angle.verification_measurement'


class WIgrtCorrectionVectorConfig(models.Model):
    configid = models.IntegerField(db_column='configID', primary_key=True)  # Field name made lowercase.
    version = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'w_igrt.correction.vector_config'


class WIgrtCorrectionVectorMeasurement(models.Model):
    measurementid = models.IntegerField(db_column='measurementID', primary_key=True)  # Field name made lowercase.
    configid = models.ForeignKey(WIgrtCorrectionVectorConfig, models.DO_NOTHING, db_column='configID', blank=True, null=True)  # Field name made lowercase.
    value = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'w_igrt.correction.vector_measurement'


class WLasersIsocenterAgreementConfig(models.Model):
    configid = models.IntegerField(db_column='configID', primary_key=True)  # Field name made lowercase.
    version = models.IntegerField()
    label = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'w_lasers.isocenter.agreement_config'


class WLasersIsocenterAgreementMeasurement(models.Model):
    measurementid = models.IntegerField(db_column='measurementID', primary_key=True)  # Field name made lowercase.
    configid = models.ForeignKey(WLasersIsocenterAgreementConfig, models.DO_NOTHING, db_column='configID', blank=True, null=True)  # Field name made lowercase.
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'w_lasers.isocenter.agreement_measurement'


class WRtgProtonbeamAlignmentConfig(models.Model):
    configid = models.IntegerField(db_column='configID', primary_key=True)  # Field name made lowercase.
    version = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'w_rtg.protonbeam.alignment_config'


class WRtgProtonbeamAlignmentMeasurement(models.Model):
    measurementid = models.IntegerField(db_column='measurementID', primary_key=True)  # Field name made lowercase.
    configid = models.ForeignKey(WRtgProtonbeamAlignmentConfig, models.DO_NOTHING, db_column='configID', blank=True, null=True)  # Field name made lowercase.
    lynxid = models.IntegerField(db_column='LynxID', blank=True, null=True)  # Field name made lowercase.
    value = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'w_rtg.protonbeam.alignment_measurement'


class WRtgProtonbeamAlignmentReference(models.Model):
    index = models.AutoField(db_column='Index', primary_key=True)  # Field name made lowercase.
    skutecny_uhel_gantry = models.IntegerField(db_column='skutecny uhel gantry', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    gantry = models.IntegerField(db_column='Gantry', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(blank=True, null=True)
    posun = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'w_rtg.protonbeam.alignment_reference'
        db_table_comment = 'vektor posuny'


class WeeklyTest(models.Model):
    index = models.AutoField(db_column='Index', primary_key=True)  # Field name made lowercase.
    date_added = models.DateTimeField(db_column='Date_added')  # Field name made lowercase.
    gantry = models.IntegerField(db_column='Gantry')  # Field name made lowercase.
    rtg_protonbeam_alignment_measurementid = models.ForeignKey(WRtgProtonbeamAlignmentMeasurement, models.DO_NOTHING, db_column='RTG.protonbeam.alignment_measurementID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lasers_0_7_field = models.IntegerField(db_column='Lasers(0-7)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lasers_isocenter_agreement_measurementid = models.ForeignKey(WLasersIsocenterAgreementMeasurement, models.DO_NOTHING, db_column='Lasers.isocenter.agreement_measurementID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    igrt_correction_vector_measurementid = models.ForeignKey(WIgrtCorrectionVectorMeasurement, models.DO_NOTHING, db_column='IGRT.correction.vector_measurementID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtr_angle_verification_measurementid = models.ForeignKey(WGantryAngleVerificationMeasurement, models.DO_NOTHING, db_column='GTR.angle.verification_measurementID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'weekly_test'
        #db_table_comment = 'Lasers (0-horn� na nozzlu, 1-doln� na nozzlu, 2-vertik�ln� na st�n� gtr, 3-horizont�ln� na st�n� gtr, 4-stropn�, 5-bo�n� na zdi, 6-bo�n� na nozzlu, 7-vz�jemn� odchylka v izocentru)'
