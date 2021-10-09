from django.db import models

# Create your models here.
class Dept(models.Model) : 
    dept_seq = models.CharField(primary_key=True, max_length=255)
    dept_nm = models.CharField(max_length=255)
    upper_dept_seq = models.CharField(max_length=255)
    all_dept_seq = models.CharField(max_length=255)
    sort = models.CharField(max_length=255)

    class Meta:
        db_table = 'tb_dept'