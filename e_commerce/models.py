# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    username = models.CharField(
        db_column='Username', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    password = models.CharField(
        db_column='Password', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    role = models.CharField(
        db_column='Role', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account'


class Address(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    city = models.CharField(
        db_column='City', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    district = models.CharField(
        db_column='District', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    ward = models.CharField(
        db_column='Ward', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    description = models.CharField(
        db_column='Description', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


class Cart(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    price = models.FloatField(blank=True, null=True)
    # Field name made lowercase.
    customerid = models.ForeignKey(
        'Customer', models.DO_NOTHING, db_column='CustomerID', blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart'


class Comment(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    descrip = models.CharField(
        db_column='Descrip', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    itemid = models.ForeignKey(
        'Item', models.DO_NOTHING, db_column='ItemID', blank=True, null=True)
    # Field name made lowercase.
    customerid = models.ForeignKey(
        'Customer', models.DO_NOTHING, db_column='CustomerID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class Customer(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=11, blank=True, null=True)
    # Field name made lowercase.
    accountid = models.ForeignKey(
        Account, models.DO_NOTHING, db_column='AccountID', blank=True, null=True)
    # Field name made lowercase.
    fullnameid = models.ForeignKey(
        'Fullname', models.DO_NOTHING, db_column='FullnameID', blank=True, null=True)
    # Field name made lowercase.
    addressid = models.ForeignKey(
        Address, models.DO_NOTHING, db_column='AddressID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Employee(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=11, blank=True, null=True)
    # Field name made lowercase.
    accountid = models.ForeignKey(
        Account, models.DO_NOTHING, db_column='AccountID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Fullname(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    firstname = models.CharField(
        db_column='FirstName', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    lastname = models.CharField(
        db_column='LastName', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fullname'


class Item(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    cartid = models.ForeignKey(
        Cart, models.DO_NOTHING, db_column='CartID', blank=True, null=True)
    # Field name made lowercase.
    productid = models.ForeignKey(
        'Product', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'


class Order(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    price = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    cartid = models.ForeignKey(
        Cart, models.DO_NOTHING, db_column='CartID', blank=True, null=True)
    # Field name made lowercase.
    paymentid = models.ForeignKey(
        'Payment', models.DO_NOTHING, db_column='PaymentID', blank=True, null=True)
    # Field name made lowercase.
    shipmentid = models.ForeignKey(
        'Shipment', models.DO_NOTHING, db_column='ShipmentID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order'


class Orderprocess(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    employeeid = models.ForeignKey(
        Employee, models.DO_NOTHING, db_column='EmployeeID', blank=True, null=True)
    # Field name made lowercase.
    orderid = models.ForeignKey(
        Order, models.DO_NOTHING, db_column='OrderID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orderprocess'


class Payment(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    price = models.FloatField(blank=True, null=True)
    payment_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'


class Product(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_type = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    public = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class Productrating(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    ratingid = models.ForeignKey(
        'Rating', models.DO_NOTHING, db_column='RatingID', blank=True, null=True)
    # Field name made lowercase.
    productid = models.ForeignKey(
        Product, models.DO_NOTHING, db_column='ProductID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productrating'


class Rating(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    star = models.IntegerField(db_column='Star', blank=True, null=True)
    # Field name made lowercase.
    itemid = models.ForeignKey(
        Item, models.DO_NOTHING, db_column='ItemID', blank=True, null=True)
    # Field name made lowercase.
    customerid = models.ForeignKey(
        Customer, models.DO_NOTHING, db_column='CustomerID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating'


class Shipment(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    fee = models.FloatField(blank=True, null=True)
    shipment_type = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    addressid = models.ForeignKey(
        Address, models.DO_NOTHING, db_column='AddressID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment'
