from django.db import models
from django.contrib.postgres.fields import JSONField
from datetime import datetime
from django.db.models import JSONField
class BarcodePatternMaster(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, blank=False, null=False)
    code_type = models.IntegerField(null=True, blank=False)  # Only :1 - 99
    pattern_description = models.CharField(max_length=500, blank=False, null=False,default='')
    pattern_name = models.CharField(max_length=250, blank=False, null=False,default='')
    code_format = models.CharField(max_length=250,blank=False, null=False,default='')  # Two Type Barcode , QR code
    pattern_sample = models.CharField(max_length=250,blank=False, null=False,default='')
    pattern_length = models.IntegerField(null=False, blank=False,)
    remark = models.CharField(max_length=500, null=True, blank=True)
    part_number = models.CharField(max_length=500,null=True, blank=True,default='')
    part_number_start_at = models.IntegerField(blank=True,null=True,default='')
    part_number_end_at = models.IntegerField(null=True, blank=True,default='')
    vendor_code = models.CharField(max_length=500,null=True, blank=True,default='')
    vendor_code_start_at = models.IntegerField(null=True, blank=True,default='')
    vendor_code_end_at = models.IntegerField(null=True, blank=True,default='')
    batch_code = models.CharField(max_length=500,null=True, blank=True,default='')
    batch_code_start_at = models.IntegerField(null=True, blank=True,default='')
    batch_code_end_at = models.IntegerField(null=True, blank=True,default='')
    created_by = models.CharField(max_length=100,null=False, blank=False,default='')
    is_active = models.BooleanField(default=False, null=False)
    is_deleted = models.BooleanField(default=False, null=False)
    updated_by = models.CharField(max_length=100,null=False, blank=False,default='')
    updated_on = models.DateTimeField(blank=False, null=False)
    class Meta:
        managed = True
        db_table = 'barcode_pattern_master'
        app_label = 'barcode_pattern_app'

class BarcodeShopMapping(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, blank=False, null=False)
    barcode_pattern_id = models.ForeignKey(BarcodePatternMaster, models.DO_NOTHING, blank=False, null=False)
    shop_type = models.CharField(max_length=500, null=True, blank=True)  # Based On DT_shop type
    created_by = models.CharField(max_length=100,null=False, blank=False,default='')
    is_active = models.BooleanField(default=False, null=False)
    updated_by = models.CharField(max_length=100,null=False, blank=False,default='')
    updated_on = models.DateTimeField(blank=False, null=False)
    class Meta:
        managed = True
        db_table = 'barcode_shop_mapping'
        app_label = 'barcode_pattern_app'
