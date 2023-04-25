#from django.db import models

# Create your models here.

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


class DIcConfig(models.Model):
    configid = models.IntegerField(db_column='configID', primary_key=True)  # Field name made lowercase.
    version = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_ic_config'


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
    measurementid = models.IntegerField(db_column='measurementID', primary_key=True)  # Field name made lowercase.
    configid = models.ForeignKey(DIcConfig, models.DO_NOTHING, db_column='configID', blank=True, null=True)  # Field name made lowercase.
    ic_id = models.IntegerField(db_column='IC_ID', blank=True, null=True)  # Field name made lowercase.
    energy = models.IntegerField(blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_ic_measurement'


class DLynxConfig(models.Model):
    configid = models.IntegerField(db_column='configID', primary_key=True)  # Field name made lowercase.
    version = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_lynx_config'


class DLynxMeasurement(models.Model):
    measurementid = models.IntegerField(db_column='measurementID', primary_key=True)  # Field name made lowercase.
    lynxconfigid = models.ForeignKey(DLynxConfig, models.DO_NOTHING, db_column='LynxconfigID', blank=True, null=True)  # Field name made lowercase.
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    lynxid = models.IntegerField(db_column='LynxID', blank=True, null=True)  # Field name made lowercase.
    energy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
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


class DMlicConfig(models.Model):
    configid = models.IntegerField(db_column='configID', primary_key=True)  # Field name made lowercase.
    version = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_mlic_config'


class DMlicMeasurement(models.Model):
    measurementid = models.IntegerField(db_column='measurementID', primary_key=True)  # Field name made lowercase.
    configid = models.ForeignKey(DMlicConfig, models.DO_NOTHING, db_column='configID', blank=True, null=True)  # Field name made lowercase.
    energy = models.IntegerField(blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
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


class DailyTest(models.Model):
    index = models.AutoField(db_column='Index', primary_key=True)  # Field name made lowercase.
    date_added = models.DateTimeField(db_column='Date_added')  # Field name made lowercase.
    gantry = models.IntegerField(db_column='Gantry')  # Field name made lowercase.
    visionrt_check = models.IntegerField(db_column='VisionRT_check', blank=True, null=True)  # Field name made lowercase.
    flatpanels_check = models.IntegerField(db_column='FlatPanels_check', blank=True, null=True)  # Field name made lowercase.
    dynr = models.IntegerField(db_column='DynR', blank=True, null=True)  # Field name made lowercase.
    lasers = models.IntegerField(db_column='Lasers', blank=True, null=True)  # Field name made lowercase.
    temperature = models.DecimalField(db_column='Temperature', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pressure = models.DecimalField(db_column='Pressure', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lynx_measurementid = models.ForeignKey(DLynxMeasurement, models.DO_NOTHING, db_column='Lynx_measurementID', blank=True, null=True)  # Field name made lowercase.
    ic_measurementid = models.ForeignKey(DIcMeasurement, models.DO_NOTHING, db_column='IC_measurementID', blank=True, null=True)  # Field name made lowercase.
    mlic_measurementid = models.ForeignKey(DMlicMeasurement, models.DO_NOTHING, db_column='MLIC_measurementID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'daily_test'
        db_table_comment = 'Lasers stored as binary number (0-x, 1-z, 2-y)'


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


