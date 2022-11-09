from django.db import models
from django.contrib.postgres.fields import JSONField
from datetime import datetime
class TagCriticality(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, blank=False, null=False)
    tag_name = models.CharField(max_length=200, blank=False, null=False,default='')
    created_by = models.CharField(max_length=100,null=False, blank=False,default='')
    created_on = models.DateTimeField(blank=False, null=False)
    is_active = models.BooleanField(default=False, null=False)
    is_deleted = models.BooleanField(default=False, null=False)
    updated_by = models.CharField(max_length=100,null=False, blank=False,default='')
    updated_on = models.DateTimeField(blank=False, null=False)
    class Meta:
        managed = True
        db_table = 'tag_criticality_master'
        app_label = 'part_family_app'

class PartFamily(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, blank=False, null=False)
    part_family_name = models.CharField(max_length=200, blank=False, null=False,default='')
    created_by = models.CharField(max_length=100,null=False, blank=False,default='')
    created_on = models.DateTimeField(blank=False, null=False)
    is_active = models.BooleanField(default=False, null=False)
    is_deleted = models.BooleanField(default=False, null=False)
    updated_by = models.CharField(max_length=100,null=False, blank=False,default='')
    updated_on = models.DateTimeField(blank=False, null=False)
    class Meta:
        managed = True
        db_table = 'part_family'
        app_label = 'part_family_app'

class PartFamilyTagCriticalityMapping(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, blank=False, null=False)
    tag_criticality_id = models.ForeignKey(TagCriticality, models.DO_NOTHING, blank=False, null=False)
    part_family_id = models.ForeignKey(PartFamily, models.DO_NOTHING, blank=False, null=False)
    created_by = models.CharField(max_length=100,null=False, blank=False,default='')
    created_on = models.DateTimeField(blank=False, null=False)
    is_active = models.BooleanField(default=False, null=False)
    is_deleted = models.BooleanField(default=False, null=False)
    updated_by = models.CharField(max_length=100,null=False, blank=False,default='')
    updated_on = models.DateTimeField(blank=False, null=False)
    class Meta:
        managed = True
        db_table = 'part_family_tag_criticality_mapping'
        app_label = 'part_family_app'

class PartFamilyShopMapping(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, blank=False, null=False)
    shop_type = models.CharField(max_length=150, blank=False, null=False, default='')
    part_family_id = models.ForeignKey(PartFamily, models.DO_NOTHING, blank=False, null=False)
    created_by = models.CharField(max_length=100, null=False, blank=False, default='')
    created_on = models.DateTimeField(blank=False, null=False)
    is_active = models.BooleanField(default=False, null=False)
    is_deleted = models.BooleanField(default=False, null=False)
    updated_by = models.CharField(max_length=100, null=False, blank=False, default='')
    updated_on = models.DateTimeField(blank=False, null=False)
    class Meta:
        managed = True
        db_table = 'part_family_shop_mapping'
        app_label = 'part_family_app'
