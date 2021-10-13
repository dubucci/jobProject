from io import TextIOWrapper
from django.db import models

# Create your models here.
# class Dept(models.Model) : 
#     dept_seq = models.CharField(primary_key=True, max_length=255)
#     dept_nm = models.CharField(max_length=255)
#     upper_dept_seq = models.CharField(max_length=255)
#     all_dept_seq = models.CharField(max_length=255)
#     sort = models.CharField(max_length=255)

#     class Meta:
#         db_table = 'tb_dept'
        


# class Code(models.Model) :
#     code = models.CharField(primary_key=True, max_length=50)
#     group_code = models.CharField(max_length=50)
#     code_nm = models.CharField(max_length=100)
#     code_val = models.CharField(max_length=30)
#     code_etc = models.CharField(max_length=30)

#     class Meta:
#         db_table = 't_code'

# class Detail_indicator(models.Model) :
#     code = models.CharField(max_length=50)
#     gubun = models.CharField(max_length=50)
#     year = models.CharField(max_length=10)
#     detail_index = models.CharField(max_length=10)
#     indicator = models.CharField(max_length=30)

#     class Meta:
#         db_table = 't_detail_indicator'

# class Indicator(models.Model) :
#     indicator = models.CharField(primary_key=True, max_length=50)
#     parent_indicator = models.CharField(max_length=50)
#     indicator_nm = models.CharField(max_length=100)
#     indicator_val = models.CharField(max_length=30)
#     indicator_etc = models.CharField(max_length=30)

#     class Meta:
#         db_table = 't_indicator'

# class Unity_indicator(models.Model) :
#     code = models.CharField(max_length=50)
#     gubun = models.CharField(max_length=50)
#     year = models.CharField(max_length=10)
#     unity_index = models.CharField(max_length=10)

#     class Meta:
#         db_table = 't_unity_indicator'
# =======================================
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
    detail_indicator_seq = models.AutoField(primary_key=True)
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
    unity_indicator_seq = models.AutoField(primary_key=True)
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