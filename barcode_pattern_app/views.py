import json

from django.views.decorators.csrf import csrf_exempt
import requests as requests
from rest_framework.decorators import api_view
from barcode_pattern_app.models import (BarcodePatternMaster,BarcodeShopMapping)
from barcode_pattern_app.serializers import (
BarcodePatternMasterSerializer,BarcodeShopMappingSerializer)
from digital_twin_configure_app import responseCode
from . import helper
from common_app import validations
# Create your views here.
@csrf_exempt
@api_view(('POST',))
def store_barcode_pattern(request):
    """
        This API is called for get new token..
        url : "barcode/store-barcode-pattern"
        @payload = {
                    "code_type":"3",
                    "code_description":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
                    "pattern_name":"Lorem Ipsum is simply dummy text ",
                    "barcode_type":"Barcode",
                    "barcode_sample":"1234567890ABC",
                    "barcode_length":"13",
                    "remark":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                    "is_part_number":"true",
                    "part_number":"67890ABC",
                    "part_number_start_at":"6",
                    "part_number_end_at":"13",
                    "is_vendor_code":0,
                    "vendor_code":"",
                    "vendor_code_start_at":"0",
                    "vendor_code_end_at":"0",
                    "is_batch_code":0,
                    "batch_code":"",
                    "batch_code_start_at":"0",
                    "batch_code_end_at":"0",
                    "created_by":"",
                    "is_active":"",
                    "updated_by":"",
                    "updated_on":""
                    }
        success response :
            {
                "STATUS": "SUCCESS",
                "RESPONSE": {
                    "STATUS_CODE": 200,
                    "MESSAGE": "Barcode pattern store successfully",
                    "DATA": "Barcode created successfully"
                    }
            }
        error response :
            {
            "STATUS":"BAD REQUEST",
            "RESPONSE":{
                            "STATUS_CODE":500,
                            "MESSAGE":"something went wrong.",
                            "DATA": []
                        }
            }
    """
    try:
        request_data = request.data
        status, user_name = validations.get_user_name_from_token(request)
        if status:
            request_data['created_by'] = user_name
            request_data['updated_by'] = user_name
        status,data = helper.store_barcode_pattern(request_data)
        if status:
            return responseCode.successResponse("Barcode pattern store successfully",data)
        if status==False:
            return responseCode.errorResponse(data)
    except Exception as e:
        return responseCode.errorResponse(str(e))

@csrf_exempt
@api_view(('PUT',))
def update_barcode_pattern(request):
    """
        This API is called for get new token..
        url : "barcode/update-barcode-pattern"
        @payload = {
                    "id":1,
                    "code_type":"3",
                    "code_description":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
                    "pattern_name":"Lorem Ipsum is simply dummy text ",
                    "barcode_type":"Barcode",
                    "barcode_sample":"1234567890ABC",
                    "barcode_length":"13",
                    "remark":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                    "is_part_number":"true",
                    "part_number":"67890ABC",
                    "part_number_start_at":"6",
                    "part_number_end_at":"13",
                    "is_vendor_code":0,
                    "vendor_code":"",
                    "vendor_code_start_at":"0",
                    "vendor_code_end_at":"0",
                    "is_batch_code":0,
                    "batch_code":"",
                    "batch_code_start_at":"0",
                    "batch_code_end_at":"0",
                    "created_by":"",
                    "is_active":"",
                    "updated_by":"",
                    "updated_on":""
                    }
        success response :
            {
                "STATUS": "SUCCESS",
                "RESPONSE": {
                    "STATUS_CODE": 200,
                    "MESSAGE": "Barcode pattern store successfully",
                    "DATA": "Barcode created successfully"
                    }
            }
        error response :
            {
            "STATUS":"BAD REQUEST",
            "RESPONSE":{
                            "STATUS_CODE":500,
                            "MESSAGE":"something went wrong.",
                            "DATA": []
                        }
            }
    """
    try:
        request_data = request.data
        status,user_name = validations.get_user_name_from_token(request)
        if status:
            request_data['created_by']=user_name
            request_data['updated_by'] =user_name
        status,data = helper.update_barcode_pattern(request_data)
        if status:
            return responseCode.successResponse("Pattern Update successfully",data)
        if status==False:
            return responseCode.errorResponse(data)
    except Exception as e:
        return responseCode.errorResponse(str(e))

@csrf_exempt
@api_view(('GET',))
def get_barcode_patterns(request):
    """
        This API is called for get new token..
        url : "barcode/get-barcode-patterns"
        @payload = {}
        success response :
            {
                "STATUS":"SUCCESS",
                "RESPONSE":{
                "STATUS_CODE":200,
                "MESSAGE":"Barcode pattern store successfully",
                "DATA":[
                {
                "id":12,
                "code_type":11,
                "code_description":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
                "pattern_name":"Lorem Ipsum is simply dummy text ",
                "barcode_type":"BARCODE",
                "barcode_sample":"1234567890ABC",
                "barcode_length":13,
                "remark":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                "part_number":"67890ABC",
                "part_number_start_at":6,
                "part_number_end_at":13,
                "vendor_code":"",
                "vendor_code_start_at":0,
                "vendor_code_end_at":0,
                "batch_code":"",
                "batch_code_start_at":0,
                "batch_code_end_at":0,
                "created_by":10,
                "is_active":true,
                "updated_by":10,
                "updated_on":"2022-10-06T06:24:07.691280Z",
                "shop_type":[
                            {
                            "id":10,
                            "shop_type":"CHASSIS",
                            "created_by":10,
                            "is_active":true,
                            "updated_by":10,
                            "updated_on":"2022-10-06T06:24:07.697069Z",
                            "barcode_pattern_id":12
                            },
                            {
                            "id":11,
                            "shop_type":"ENGINE",
                            "created_by":10,
                            "is_active":true,
                            "updated_by":10,
                            "updated_on":"2022-10-06T06:24:07.697069Z",
                            "barcode_pattern_id":12
                            },
                            {
                            "id":12,
                            "shop_type":"CAB",
                            "created_by":10,
                            "is_active":true,
                            "updated_by":10,
                            "updated_on":"2022-10-06T06:24:07.697069Z",
                            "barcode_pattern_id":12
                            }
                        ]
                    }
                ]
                }
                }
        error response :
            {
            "STATUS":"BAD REQUEST",
            "RESPONSE":{
                            "STATUS_CODE":500,
                            "MESSAGE":"something went wrong.",
                            "DATA": []
                        }
            }
    """
    try:
        request_data = request.data
        status, user_name = validations.get_user_name_from_token(request)
        if status:
            request_data['created_by'] = user_name
            request_data['updated_by'] = user_name
        status, data = helper.get_barcode_patterns(request_data)
        if status:
            return responseCode.successResponse("Barcode pattern fetch successfully", data)
        if status == False:
            return responseCode.errorResponse(data)
    except Exception as e:
        return responseCode.errorResponse(str(e))


@csrf_exempt
@api_view(('GET',))
def get_shop_types(request):
    """
        This API is called for get new token..
        url : "api/get-shop-types"
        @payload = {
                }
        success response :
                            {
                                "STATUS": "SUCCESS",
                                "RESPONSE": {
                                    "STATUS_CODE": 200,
                                    "MESSAGE": "All Station data has been set successfully",
                                    "DATA": [
                                        {
                                            "id": 32,
                                            "dt_shop_id": 164,
                                            "name": "FES",
                                            "description": "Faceless Structure",
                                            "shop_type": "Cab",
                                            "updated_on": "2022-09-27T05:25:47.996244Z",
                                            "dt_plant_id": 4
                                        }
                                    ]
                                }
                            }
        error response :
            {
            "STATUS":"BAD REQUEST",
            "RESPONSE":{
                            "STATUS_CODE":500,
                            "MESSAGE":"something went wrong.",
                            "DATA": []
                        }
            }
    """
    try:
        status, data = helper.get_shop_types(request)
        if status:
            return responseCode.successResponse("Shop type fetch successfully", data)
        if status == False:
            return responseCode.successResponse("No More data found", [])
    except Exception as e:
        return responseCode.errorResponse(str(e))

@csrf_exempt
@api_view(('GET',))
def get_pattern_types(request):
    """
        This API is called for get new token..
        url : "api/get_pattern_types"
        @payload = {"id":2}
        success response :
                            {
                                "STATUS": "SUCCESS",
                                "RESPONSE": {
                                    "STATUS_CODE": 200,
                                    "MESSAGE": "All Station data has been set successfully",
                                    "DATA": [
                                        {
                                            "id": 32,
                                            "dt_shop_id": 164,
                                            "name": "FES",
                                            "description": "Faceless Structure",
                                            "shop_type": "Cab",
                                            "updated_on": "2022-09-27T05:25:47.996244Z",
                                            "dt_plant_id": 4
                                        }
                                    ]
                                }
                            }
        error response :
            {
            "STATUS":"BAD REQUEST",
            "RESPONSE":{
                            "STATUS_CODE":500,
                            "MESSAGE":"something went wrong.",
                            "DATA": []
                        }
            }
    """
    try:
        status, data = helper.get_pattern_types(request)
        if status:
            return responseCode.successResponse("Patterns type fetch successfully", data)
        if status == False:
            return responseCode.successResponse("No More data found", [])
    except Exception as e:
        return responseCode.errorResponse(str(e))

@csrf_exempt
@api_view(('DELETE',))
def delete_barcode_pattern(request):
    print(request)
    """
        This API is called for get new token..
        url : "api/delete_barcode_pattern"
        @payload = {"id":2}
        success response :
                            {
                                "STATUS": "SUCCESS",
                                "RESPONSE": {
                                    "STATUS_CODE": 200,
                                    "MESSAGE": "All Station data has been set successfully",
                                    "DATA": []
                                }
                            }
        error response :
            {
            "STATUS":"BAD REQUEST",
            "RESPONSE":{
                            "STATUS_CODE":500,
                            "MESSAGE":"something went wrong.",
                            "DATA": []
                        }
            }
    """
    try:
        request_data = request.data
        status, user_name = validations.get_user_name_from_token(request)
        if status:
            request_data['created_by'] = user_name
            request_data['updated_by'] = user_name
        status, data = helper.delete_barcode_pattern(request_data)
        if status:
            return responseCode.successResponse("Barcode pattern deleted successfully", data)
        if status == False:
            return responseCode.successResponse("No More data found", [])
    except Exception as e:
        return responseCode.errorResponse(str(e))