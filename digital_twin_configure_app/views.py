from django.views.decorators.csrf import csrf_exempt
import requests as requests
from rest_framework.decorators import api_view
from digital_twin_configure_app.models import (OrganizationMaster,BusinessUnitMaster,PlantMaster,ShopMaster,LineMaster,StationMaster)
from digital_twin_configure_app.serializers import (
OrganizationSerializer,BusinessUnitSerializer,PlantSerializer,ShopSerializer,LineSerializer,StationSerializer)
from . import helper
from . import responseCode

@csrf_exempt
@api_view(('GET',))
def fetch_organization_master(request):
    """
        This API is called for get new token..
        url : "api/fetch_organization_master"
        @payload = {
                "Authorization":"Bearer "+access_token,
                "Content-Type": "application/json"
                } 
        success response :
            {
                "STATUS": "SUCCESS",
                "RESPONSE": {
                    "STATUS_CODE": 200,
                    "MESSAGE": "All Organization has been set successfully",
                    "DATA": [
                        {
                            "id": 10,
                            "name": "Tata Motors Limited"
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
        status,data = helper.fetch_organization_master(request)
        if status:
            return responseCode.successResponse("All Organization has been set successfully",data)
        if status==False:
            return responseCode.successResponse("No More data found",[])
    except Exception as e:
        return responseCode.errorResponse(str(e))


@csrf_exempt
@api_view(('GET',))
def fetch_business_unit_master(request):
    """
        This API is called for get new token..
        url : "api/fetch_business_unit_master"
        @payload = {
                "Authorization":"Bearer "+access_token,
                "Content-Type": "application/json"
                } 
        success response :
            {
                "STATUS": "SUCCESS",
                "RESPONSE": {
                    "STATUS_CODE": 200,
                    "MESSAGE": "All BusinessUnit has been set successfully",
                    "DATA": [
                        {
                            "id": 10,
                            "name": "CVBU"
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
        status,data = helper.fetch_business_unit_master(request)
        if status:
            return responseCode.successResponse("All BusinessUnit has been set successfully",data)
        if status==False:
            return responseCode.successResponse("No More data found",[])
    except Exception as e:
        print(str(e))
        return responseCode.errorResponse(str(e))

@csrf_exempt
@api_view(('GET',))
def fetch_plant_master(request):
    """
        This API is called for get new token..
        url : "api/fetch_plant_master"
        @payload = {
                "Authorization":"Bearer "+access_token,
                "Content-Type": "application/json"
                } 
        success response :
            {
                "STATUS": "SUCCESS",
                "RESPONSE": {
                    "STATUS_CODE": 200,
                    "MESSAGE": "All Plant Data has been set successfully",
                    "DATA": [
                        {
                            "id": 1,
                            "name": "Pune",
                            "city": "Pune",
                            "state": "Maharashtra",
                            "country": "India",
                            "sapPlantId": 1,
                            "ipmsPlantId": 1,
                            "businessUnit": {
                                "id": 1
                            }
                        },
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
        status,data = helper.fetch_plant_master(request)
        if status:
            return responseCode.successResponse("All Plant Data has been set successfully",data)
        if status==False:
            return responseCode.successResponse("No More data found",[])
    except Exception as e:
        return responseCode.errorResponse(str(e))

@csrf_exempt
@api_view(('GET',))
def fetch_shop_master(request):
    """
        This API is called for get new token..
        url : "api/fetch_shop_master"
        @payload = {
                "Authorization":"Bearer "+access_token,
                "Content-Type": "application/json"
                } 
        success response :
            {
                "STATUS": "SUCCESS",
                "RESPONSE": {
                    "STATUS_CODE": 200,
                    "MESSAGE": "All Shop data has been set successfully",
                    "DATA": [
                        {
                            "id": 133,
                            "name": "1C",
                            "description": "Trim Chassis Fitment",
                            "type": "Chassis",
                            "plant": {
                                "id": 3100
                            }
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
        status,data = helper.fetch_shop_master(request)
        if status:
            return responseCode.successResponse("All Shop data has been set successfully",data)
        if status==False:
            return responseCode.successResponse("No More data found",[])
    except Exception as e:
        return responseCode.errorResponse(str(e))


@csrf_exempt
@api_view(('GET',))
def fetch_line_master(request):
    """
        This API is called for get new token..
        url : "api/fetch_line_master"
        @payload = {
                "Authorization":"Bearer "+access_token,
                "Content-Type": "application/json"
                } 
        success response :
            {
                "STATUS": "SUCCESS",
                "RESPONSE": {
                    "STATUS_CODE": 200,
                    "MESSAGE": "All Line data has been set successfully",
                    "DATA": [
                        {
                            "id": 1016,
                            "name": "D9",
                            "description": "497 / 697",
                            "type": "Main",
                            "typeAlias": "Assembly",
                            "sapLineId": "26500002",
                            "ipmsLineId": "8",
                            "shop": {
                                "id": 153
                            },
                            "organization": {
                                "id": 10
                            }
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
        status,data = helper.fetch_line_master(request)
        if status:
            return responseCode.successResponse("All Line data has been set successfully",data)
        if status==False:
            return responseCode.successResponse("No More data found",[])
    except Exception as e:
        return responseCode.errorResponse(str(e))

@csrf_exempt
@api_view(('GET',))
def fetch_station_master(request):
    """
        This API is called for get new token..
        url : "api/fetch_station_master"
        @payload = {
                "Authorization":"Bearer "+access_token,
                "Content-Type": "application/json"
                } 
        success response :
            {
                        "STATUS": "SUCCESS",
                        "RESPONSE": {
                            "STATUS_CODE": 200,
                            "MESSAGE": "All Station data has been set successfully",
                            "DATA": [
                                {
                                    "id": 10000,
                                    "name": "Frame dropping",
                                    "number": "CH 01",
                                    "line": {
                                        "id": 1000
                                    }
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
        status,data = helper.fetch_station_master(request)
        if status:
            return responseCode.successResponse("All Station data has been set successfully",data)
        if status==False:
            return responseCode.successResponse("No More data found",[])
    except Exception as e:
        return responseCode.errorResponse(str(e))   



