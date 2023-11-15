# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customers(models.Model):
    cno = models.IntegerField(primary_key=True) 
    cname = models.CharField(max_length=18, blank=True, null=True)
    street = models.CharField(max_length=30, blank=True, null=True)
    zip = models.CharField(max_length=6, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'customers'


class Employees(models.Model):
    eno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=18, blank=True, null=True)
    zip = models.CharField(max_length=6, blank=True, null=True)
    hdate = models.DateField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'employees'

class Orders(models.Model):
    ono = models.IntegerField( primary_key=True )
    cno = models.IntegerField(blank=True, null=True)
    eno = models.IntegerField(blank=True, null=True)
    received = models.DateField(blank=True, null=True)
    shipped = models.DateField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'orders'


class Parts(models.Model):
    pno = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=30, blank=True, null=True)
    qoh = models.IntegerField(blank=True, null=True)
    prices = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    wlevel = models.IntegerField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'parts'

class Odetails(models.Model):
    odetails_id = models.AutoField(primary_key=True)
    ono = models.ForeignKey('Orders', on_delete=models.CASCADE, db_column='ono')
    pno = models.ForeignKey('Parts', on_delete=models.CASCADE, db_column='pno')
    qty = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'odetails'


class Zipcodes(models.Model):
    zip = models.CharField(max_length=6, primary_key=True)
    city = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'zipcodes'
