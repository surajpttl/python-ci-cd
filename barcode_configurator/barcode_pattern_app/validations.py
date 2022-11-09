from django.conf import settings
import requests
import jwt
from barcode_pattern_app.models import (BarcodePatternMaster,BarcodeShopMapping)
from barcode_pattern_app.serializers import (
BarcodePatternMasterSerializer,BarcodeShopMappingSerializer)

def check_code_type_is_present(code_type,check_flag,id):
    try:
        if type(code_type) == str and code_type.isnumeric() == False:
            return False,"Code type must be an number"
        if check_flag == 'insert':
            queryParams = BarcodePatternMaster.objects.filter(code_type=int(code_type),is_active=True,is_deleted=False).first()
        if check_flag == 'update':
            queryParams = BarcodePatternMaster.objects.filter(code_type=int(code_type),is_active=True,is_deleted=False).exclude(id=id).first()
        if queryParams:
            barcodePatternMasterSerializer = BarcodePatternMasterSerializer(queryParams)
            if len(barcodePatternMasterSerializer.data) != 0:
                return False, "Code type is already present"
        else:
            return True,""
    except Exception as e:
        return False,str(e)

def check_pattern_sample_is_present(pattern_sample,check_flag,id):
    try:
        if check_flag == 'insert':
            queryParams = BarcodePatternMaster.objects.filter(pattern_sample=pattern_sample,is_active=True,is_deleted=False).first()
        if check_flag == 'update':
            queryParams = BarcodePatternMaster.objects.filter(pattern_sample=pattern_sample,is_active=True,is_deleted=False).exclude(id=id).first()
        if queryParams:
            barcodePatternMasterSerializer = BarcodePatternMasterSerializer(queryParams)
            if len(barcodePatternMasterSerializer.data) != 0:
                return False, "Pattern sample is already present"
        else:
            return True,""
    except Exception as e:
        return False,str(e)

def check_code_description(code_description):
    try:
        if len(code_description)>500:
            return False, "Code description should be 500 character"
        return True,""
    except Exception as e:
        return False,str(e)

def check_pn_bt_bs(request_string,request_key):
    try:
        if len(request_string)>250:
            return False, request_key+" should be 250 character"
        return True,""
    except Exception as e:
        return False,str(e)

def check_barcode_length(barcode_length,barcode_sample):
    try:
        if type(barcode_length) == str and barcode_length.isnumeric() == False:
            return False, "barcode length should be numeric"
        if int(barcode_length) != len(barcode_sample):
            return False, "barcode length and barcode sample length are not same"
        return True,""
    except Exception as e:
        return False,str(e)


def check_extra_information(request_data):
    if request_data['is_part_number']:
        status,message = check_start_end_numeric(request_data['part_number_start_at'],request_data['part_number_end_at'],"Part Number")
        if status==False:
            return status,message
        status, substring = genrate_substring(request_data['part_number_start_at'],
                                           request_data['part_number_end_at'], request_data['pattern_sample'])
        if status==False:
            status, message
        if substring != request_data['part_number']:
            return False,"Part no is not matching"
    if request_data['is_vendor_code']==True:
        status, message = check_start_end_numeric(request_data['vendor_code_start_at'],
                                                  request_data['vendor_code_end_at'],"Vendor Code")
        if status == False:
            return status, message
        status, substring = genrate_substring(request_data['vendor_code_start_at'],
                                              request_data['vendor_code_end_at'], request_data['pattern_sample'])
        if status == False:
            status, message
        if substring != request_data['vendor_code']:
            return False, "Vendor code is not matching"
    if request_data['is_batch_code']:
        status, message = check_start_end_numeric(request_data['batch_code_start_at'],
                                                  request_data['batch_code_end_at'],"Batch Code")
        if status == False:
            return status, message
        status, substring = genrate_substring(request_data['batch_code_start_at'],
                                              request_data['batch_code_end_at'], request_data['pattern_sample'])
        if status == False:
            status, message
        if substring != request_data['batch_code']:
            return False, "Vendor code is not matching"
    return True,""

def check_start_end_numeric(start_at,end_at,request_key):
    try:
        if type(start_at) == str and start_at.isnumeric() == False:
            return False, request_key+" start at should be numeric"
        if type(end_at) == str and end_at.isnumeric() == False:
            return False, request_key+" end at should be numeric"
        if int(start_at) >= int(end_at):
            return False, request_key+" start at should be less than  end at"
        return True,""
    except Exception as e:
        return False,str(e)

def genrate_substring(start_at,end_at,original_string):
    try:
        #original_string = " "+original_string
        start_at = int(start_at)-1
        end_at = int(end_at)
        return  True,original_string[start_at:end_at]
    except Exception as e:
        return False, str(e)
def get_user_name_from_token(request):
    user_name = request.META['user_name']
    if not user_name:
        return False
    return True,user_name

