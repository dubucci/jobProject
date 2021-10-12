from django.db import models

class TCode(models.Model):
    code = models.CharField(db_column='CODE', primary_key=True, max_length=50)  # Field name made lowercase.
    group_code = models.CharField(db_column='GROUP_CODE', max_length=50)  # Field name made lowercase.
    code_nm = models.CharField(db_column='CODE_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    code_val = models.CharField(db_column='CODE_VAL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    code_etc = models.CharField(db_column='CODE_ETC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    regist_dt = models.DateTimeField(db_column='REGIST_DT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_code'
        unique_together = (('code', 'group_code'),)


class TDetailIndicator(models.Model):
    code = models.CharField(db_column='CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gubun = models.CharField(db_column='GUBUN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='YEAR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    detail_index = models.CharField(db_column='DETAIL_INDEX', max_length=10, blank=True, null=True)  # Field name made lowercase.
    indicator = models.CharField(db_column='INDICATOR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    regist_dt = models.DateTimeField(db_column='REGIST_DT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_detail_indicator'


class TIndicator(models.Model):
    indicator = models.CharField(db_column='INDICATOR', primary_key=True, max_length=50)  # Field name made lowercase.
    parent_indicator = models.CharField(db_column='PARENT_INDICATOR', max_length=50)  # Field name made lowercase.
    indicator_nm = models.CharField(db_column='INDICATOR_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    indicator_val = models.CharField(db_column='INDICATOR_VAL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    indicator_etc = models.CharField(db_column='INDICATOR_ETC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    regist_dt = models.DateTimeField(db_column='REGIST_DT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_indicator'


class TUnityIndicator(models.Model):
    code = models.CharField(db_column='CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gubun = models.CharField(db_column='GUBUN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='YEAR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    unity_index = models.CharField(db_column='UNITY_INDEX', max_length=10, blank=True, null=True)  # Field name made lowercase.
    regist_dt = models.DateTimeField(db_column='REGIST_DT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_unity_indicator'


class TbDept(models.Model):
    dept_seq = models.CharField(primary_key=True, max_length=255)
    dept_nm = models.CharField(max_length=255)
    upper_dept_seq = models.CharField(max_length=255)
    all_dept_seq = models.CharField(max_length=255)
    sort = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tb_dept'
