from django.db import models
from django.db.models.signals import pre_save,post_save

class Department(models.Model):
    deptno=models.IntegerField(primary_key=True)
    deptname=models.CharField(max_length=20)
    def __str__(self):
        return self.deptname
# Create your models here.
class Employee(models.Model):
    empno=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=20)
    empsal=models.IntegerField(null=True)
    department=models.ForeignKey(Department,null=True,on_delete=models.CASCADE)
    bonus=models.IntegerField(null=True)
    profile_pic=models.ImageField(upload_to='images/',null=True)
    video=models.FileField(upload_to='videos/',null=True)
    def __str__(self):
        return self.empname
class Aadhar(models.Model):
    aadharno=models.IntegerField(max_length=20,primary_key=True)
    dob=models.DateField(auto_now=True)
class Person(models.Model):
    pid=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=20)
    aadhar=models.OneToOneField(Aadhar,on_delete=models.CASCADE)
class Driver(models.Model):
    licenseno=models.CharField(max_length=20,primary_key=True)
    dname=models.CharField(max_length=20)
class Car(models.Model):
    regno=models.CharField(max_length=20,primary_key=True)
    model=models.CharField(max_length=20)
    driver=models.ManyToManyField(Driver)

class Base(models.Model):
    empno=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=20)
    class Meta:
        abstract=True
class Table1(Base):
    address=models.TextField(max_length=150)
class Table2(Base):

    mobile=models.CharField(max_length=13)

class employeedup(Employee):
    class Meta:
        proxy=True
        ordering=['-empname']


def customsendemail(sender,instance,**kwargs):
    print('presave signal received')
    print(sender,instance)
pre_save.connect(customsendemail,Employee)

def display(sender,instance,created,**kwargs):
    print('postsave signal received')
    print(sender,instance,created)
post_save.connect(display,Employee)

