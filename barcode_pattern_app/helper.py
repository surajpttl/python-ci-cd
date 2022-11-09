import json
import jwt
from datetime import datetime, timezone
from django.conf import settings
import requests
from django.utils import timezone
from barcode_pattern_app.models import (BarcodePatternMaster,BarcodeShopMapping)
from barcode_pattern_app.serializers import (
BarcodePatternMasterSerializer,BarcodeShopMappingSerializer)
from digital_twin_configure_app.models import (ShopMaster)
from digital_twin_configure_app.serializers import (ShopSerializer)
from . import validations

BARCODE_TYPE = ["BARCODE","QR CODE"]

def store_barcode_pattern(request_data):
    try:
        if len(request_data['shop_type'])<=0:
            return False,"Select at least one shop type"
        status,message = validations.check_code_type_is_present(request_data['code_type'],'insert',0)
        if status==False:
            return status,message
        status, message = validations.check_pattern_sample_is_present(request_data['pattern_sample'], 'insert', 0)
        if status == False:
            return status, message
        status, message = validations.check_code_description(request_data['pattern_description'])
        if status == False:
            return status, message
        status, message = validations.check_pn_bt_bs(request_data['pattern_name'],"Pattern name")
        if status == False:
            return status, message
        status, message = validations.check_pn_bt_bs(request_data['code_format'], "Barcode type")
        if status == False:
            return status, message
        status, message = validations.check_pn_bt_bs(request_data['pattern_sample'], "Pattern sample")
        if status == False:
            return status, message
        status, message = validations.check_barcode_length(request_data['pattern_length'],request_data['pattern_sample'])
        if status == False:
            return status, message
        if request_data['code_format'].upper() not in BARCODE_TYPE:
            return False, "Barcode type not found"
        status, message = validations.check_extra_information(request_data)
        if status == False:
            return status, message
        status,message = storeData(request_data)
        if status:
            last_inserted_query = BarcodePatternMaster.objects.latest('id')
            barcode_pattern_master_serializer = BarcodePatternMasterSerializer(last_inserted_query)
            status,message = store_shop_mapping(request_data['shop_type'],barcode_pattern_master_serializer.data['id'],request_data['created_by'],"multiple")
        return status,message
    except Exception as e:
        return False,str(e)

def storeData(request_data):
    try:
        request_data['code_format'] = request_data['code_format'].upper()
        updated_on = timezone.now()
        created_by=request_data['created_by']
        updated_by=request_data['updated_by']
        obj = BarcodePatternMaster.objects.create(code_type=int(request_data['code_type']),pattern_description=request_data['pattern_description'], pattern_name=request_data['pattern_name'],code_format=request_data['code_format'],pattern_sample=request_data['pattern_sample'],pattern_length=request_data['pattern_length'],remark=request_data['remark'],part_number=request_data['part_number'],part_number_start_at=request_data['part_number_start_at'],part_number_end_at=request_data['part_number_end_at'],vendor_code = request_data['vendor_code'], vendor_code_start_at = request_data['vendor_code_start_at'], vendor_code_end_at = request_data['vendor_code_end_at'],batch_code = request_data['batch_code'], batch_code_start_at = request_data['batch_code_start_at'], batch_code_end_at = request_data['batch_code_end_at'],created_by=created_by,is_active=True,updated_by=updated_by,updated_on=updated_on)
        return True,"Barcode pattern created successfully"
    except Exception as e:
        return False,str(e)

def store_shop_mapping(shop_types,barcode_pattern_id,user,type):
    created_by = user
    updated_by = user
    updated_on = timezone.now()
    try:
        if type=="single":
            obj = BarcodeShopMapping.objects.create(
                barcode_pattern_id=BarcodePatternMaster.objects.get(id=barcode_pattern_id), shop_type=shop_types.upper(),
                created_by=created_by, is_active=True, updated_by=updated_by, updated_on=updated_on)
        else:
            for shop_type in shop_types:
              obj = BarcodeShopMapping.objects.create(barcode_pattern_id=BarcodePatternMaster.objects.get(id=barcode_pattern_id),shop_type=shop_type.upper(),created_by=created_by,is_active=True,updated_by=updated_by,updated_on=updated_on)
            return True,"Barcode pattern created successfully"
    except Exception as e:
        return False,str(e)

def update_barcode_pattern(request_data):
    try:
        queryParams = BarcodePatternMaster.objects.filter(id=request_data['id'],is_active=True,is_deleted=False).first()
        if queryParams==None:
            return False, "Record not found or not active now"
        if len(request_data['shop_type'])<=0:
            return False,"Select at least one shop type"
        status,message = validations.check_code_type_is_present(request_data['code_type'],'update',request_data['id'])
        if status==False:
            return status,message
        status, message = validations.check_code_description(request_data['pattern_description'])
        if status == False:
            return status, message
        status, message = validations.check_pn_bt_bs(request_data['pattern_name'],"Pattern name")
        if status == False:
            return status, message
        status, message = validations.check_pn_bt_bs(request_data['code_format'], "code format")
        if status == False:
            return status, message
        status, message = validations.check_pn_bt_bs(request_data['pattern_sample'], "Pattern sample")
        if status == False:
            return status, message
        status, message = validations.check_barcode_length(request_data['pattern_length'],request_data['pattern_sample'])
        if status == False:
            return status, message
        if request_data['code_format'].upper() not in BARCODE_TYPE:
            return False, "Barcode type not found"
        status, message = validations.check_extra_information(request_data)
        if status == False:
            return status, message
        status,message = update_barcode_pattern_data(request_data)
        if status:
            status,message = update_shop_mapping(request_data['shop_type'],request_data['id'],request_data['updated_by'])
        return status,"Pattern Update successfully"
    except Exception as e:
        print(str(e))
        return False,str(e)

def update_barcode_pattern_data(request_data,*args, **kwargs):
    updated_on = timezone.now()
    updated_by = request_data['updated_by']
    updateData = {
                    "code_type":request_data["code_type"],
                    "pattern_description":request_data["pattern_description"],
                    "pattern_name":request_data["pattern_name"],
                    "code_format":request_data["code_format"],
                    "pattern_sample":request_data["pattern_sample"],
                    "pattern_length":request_data["pattern_length"],
                    "shop_type":request_data["shop_type"],
                    "remark":request_data["remark"],
                   # "is_part_number":request_data["is_part_number"],
                    "part_number":request_data["part_number"],
                    "part_number_start_at":request_data["part_number_start_at"],
                    "part_number_end_at":request_data["part_number_end_at"],
                   # "is_vendor_code":request_data["is_vendor_code"],
                    "vendor_code":request_data["vendor_code"],
                    "vendor_code_start_at":request_data["vendor_code_start_at"],
                    "vendor_code_end_at":request_data["vendor_code_end_at"],
                   # "is_batch_code":request_data["is_batch_code"],
                    "batch_code":request_data["batch_code"],
                    "batch_code_start_at":request_data["batch_code_start_at"],
                    "batch_code_end_at":request_data["batch_code_end_at"],
                    "updated_by":updated_by,
                    "updated_on":updated_on
                    }
    try:
        instance = BarcodePatternMaster.objects.filter(id=int(request_data['id'])).first()
        if instance:
            serializer = BarcodePatternMasterSerializer(
            instance,
            data=updateData,
            partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return True,"Data Update successfully"
    except Exception as e:
        return False,str(e)

def update_shop_mapping(shop_types,barcode_pattern_id,updated_by):
    try:
        shop_types_upper = [shop_type.upper() for shop_type in shop_types]
        queryParams = BarcodeShopMapping.objects.filter(
                barcode_pattern_id=BarcodePatternMaster.objects.get(id=barcode_pattern_id)).exclude(shop_type__in=list(shop_types_upper))
        if queryParams:
            barcodeShopMappingSerializer = BarcodeShopMappingSerializer(queryParams, many=True)
            for deleteItem in barcodeShopMappingSerializer.data:
                BarcodeShopMapping.objects.filter(id=deleteItem['id']).delete()
        for shop_type in shop_types_upper:
            queryParams = BarcodeShopMapping.objects.filter(
                barcode_pattern_id=BarcodePatternMaster.objects.get(id=barcode_pattern_id),shop_type=shop_type)
            if not queryParams:
                store_shop_mapping(shop_type,barcode_pattern_id,updated_by,'single')
        return True, "Pattern Update successfully"
    except Exception as e:
        return False, str(e)

def get_barcode_patterns(request_data):
    queryParams = BarcodePatternMaster.objects.filter(is_active=True,is_deleted=False).order_by('id')
    if not queryParams:
        return True,"No more record found"
    barcodePatternMasterSerializer = BarcodePatternMasterSerializer(queryParams,many=True)
    all_barcode_paterns = []
    for pattern in  barcodePatternMasterSerializer.data:
        shop_mapping_query = BarcodeShopMapping.objects.filter(
            barcode_pattern_id=BarcodePatternMaster.objects.get(id=pattern['id']))
        pattern['shop_type'] = BarcodeShopMappingSerializer(shop_mapping_query,many=True).data
        all_barcode_paterns.append(pattern)
    return True,barcodePatternMasterSerializer.data

def get_shop_types(request_data):
    query_params = ShopMaster.objects.distinct("shop_type")
    shopSerializer = ShopSerializer(query_params,many=True)
    return True,shopSerializer.data

def get_pattern_types(request_data):
    return True,BARCODE_TYPE

def delete_barcode_pattern(request_data):
    updated_on = timezone.now()
    updated_by = request_data['updated_by']
    queryParams = BarcodePatternMaster.objects.filter(id=request_data['id']).first()
    if queryParams == None:
        return False, "Record not found"
    updateData = {
                    "is_active":False,
                    "is_deleted": True,
                    "updated_by": updated_by,
                    "updated_on": updated_on
                 }
    try:
        instance = BarcodePatternMaster.objects.filter(id=int(request_data['id'])).first()
        if instance:
            serializer = BarcodePatternMasterSerializer(
                instance,
                data=updateData,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return True, "Data Update successfully"
    except Exception as e:
        return False, str(e)
