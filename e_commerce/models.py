# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ward = models.CharField(db_column='Ward', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'address'


class Cart(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cart'


class CartItem(models.Model):
    cartid = models.OneToOneField(Cart, models.DO_NOTHING, db_column='CartID', primary_key=True)  # Field name made lowercase.
    itemid = models.ForeignKey('Item', models.DO_NOTHING, db_column='ItemID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cart_item'
        unique_together = (('cartid', 'itemid'),)


class Custom(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    birthday = models.DateField(db_column='Birthday', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='Phonenumber', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'custom'


class Fullname(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fullname'


class Item(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item'


class Order(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    paymentid = models.ForeignKey('Payment', models.DO_NOTHING, db_column='PaymentID')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    discount = models.FloatField(db_column='Discount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'


class OrderItem(models.Model):
    orderid = models.OneToOneField(Order, models.DO_NOTHING, db_column='OrderID', primary_key=True)  # Field name made lowercase.
    itemid = models.ForeignKey(Item, models.DO_NOTHING, db_column='ItemID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_item'
        unique_together = (('orderid', 'itemid'),)


class Payment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment'


class User(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fullnameid = models.ForeignKey(Fullname, models.DO_NOTHING, db_column='FullnameID', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
