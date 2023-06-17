from django.db import models

# Create your models here.
class emp(models.Model):
    empno=models.IntegerField(min)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    MGR=models.IntegerField(min)
    Hiredate=models.DateField()
    sal=models.IntegerField()
    deptno=models.IntegerField(max)
class Dept(models.Model):
    deptno=models.OneToOneField(emp,on_delete=models.CASCADE)
    dname=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)