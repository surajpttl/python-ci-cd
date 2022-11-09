from django.db import models
from django.contrib.postgres.fields import JSONField
from datetime import datetime
from django.db.models import JSONField
# Create your models here.
class OrganizationMaster(models.Model):
    dt_organization_id=models.BigIntegerField(unique=True)
    name = models.CharField(max_length=110)
    updated_on = models.DateTimeField(blank=False, null=False)
    class Meta:
        managed = True
        db_table = 'organization_master'
        app_label = 'digital_twin_configure_app'

class BusinessUnitMaster(models.Model):
    dt_business_unit_id=models.BigIntegerField(unique=True)
    name = models.CharField(max_length=100)
    #dt_organization_id=models.ForeignKey(OrganizationMaster, models.DO_NOTHING, blank=False, null=False)
    updated_on = models.DateTimeField(blank=False, null=False) 
    class Meta:
        managed = True
        db_table = 'business_unit_master'
        app_label = 'digital_twin_configure_app'

class PlantMaster(models.Model):
    dt_plant_id=models.BigIntegerField(unique=True)
    name=models.CharField(max_length=100,blank=False,null=False)
    city=models.CharField(max_length=100,blank=False,null=False)
    state=models.CharField(max_length=100,blank=False,null=False)
    country=models.CharField(max_length=100,blank=False,null=False)
    dt_business_unit_id=models.ForeignKey(BusinessUnitMaster, models.DO_NOTHING, blank=False, null=False)
    updated_on = models.DateTimeField(blank=False, null=False)
    class Meta:
        managed = True
        db_table = 'plant_master'
        app_label = 'digital_twin_configure_app'
        
class ShopMaster(models.Model):
    dt_shop_id =models.BigIntegerField(unique=True)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    shop_type=models.CharField(max_length=100)
    dt_plant_id =models.ForeignKey(PlantMaster, models.DO_NOTHING, blank=False, null=False) 
    updated_on = models.DateTimeField(blank=False, null=False)
    class Meta:
        managed = True
        db_table = 'shop_master'
        app_label = 'digital_twin_configure_app'

        
class LineMaster(models.Model):
    dt_line_id =models.BigIntegerField(unique=True)
    name =models.CharField(max_length=100)
    description =models.CharField(max_length=100)
    dt_shop_id = models.ForeignKey(ShopMaster, models.DO_NOTHING, blank=False, null=False) 
    line_type =models.CharField(max_length=100)
    updated_on = models.DateTimeField(blank=False, null=False)
    class Meta:
        managed = True
        db_table = 'line_master'
        app_label = 'digital_twin_configure_app'

class StationMaster(models.Model):
    dt_station_id =models.BigIntegerField(unique=True)
    name=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    dt_line_id =models.ForeignKey(LineMaster, models.DO_NOTHING, blank=False, null=False) 
    updated_on = models.DateTimeField(blank=False, null=False)
    class Meta:
        managed = True
        db_table = 'station_master'
        app_label = 'digital_twin_configure_app'


