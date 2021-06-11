# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255, blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=255, blank=True, null=True)  # Field name made lowercase.        

    class Meta:
        managed = False
        db_table = 'account'


class Address(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ward = models.CharField(db_column='Ward', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'address'


class Customer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    email = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=11, blank=True, null=True)
    accountid = models.ForeignKey(Account, models.DO_NOTHING, db_column='AccountID', blank=True, null=True)  # Field name made lowercase.
    fullnameid = models.ForeignKey('Fullname', models.DO_NOTHING, db_column='FullnameID', blank=True, null=True)  # Field name made lowercase.
    addressid = models.ForeignKey(Address, models.DO_NOTHING, db_column='AddressID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class Fullname(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fullname'