import json
from django.views.decorators.csrf import csrf_exempt
import requests as requests
from rest_framework.decorators import api_view
from common_app import responseCode
from . import helper
from common_app import validations
# Create your views here.
@csrf_exempt
@api_view(('POST',))
def store_tag_criticality(request):
    """
        This API is called for get new token..
        url : "part_family/store-tag-criticality"
        @payload = {
                    "tag_name":"      Emission SAFETY     "
                    }
        success response :
            {
                "STATUS": "SUCCESS",
                "RESPONSE": {
                    "STATUS_CODE": 200,
                    "MESSAGE": "tag store successfully",
                    "DATA": "tag created successfully"
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
        status,data = helper.store_tag_criticality(request_data)
        if status:
            return responseCode.successResponse("Tag store successfully",data)
        if status==False:
            return responseCode.errorResponse(data)
    except Exception as e:
        return responseCode.errorResponse(str(e))

@csrf_exempt
@api_view(('PUT',))
def update_tag_criticality(request):
    """
          This API is called for get new token..
          url : "part_family/store-tag-criticality"
          @payload = {
                      "id":1
                      "tag_name":"      Emission SAFETY     "
                      }
          success response :
              {
                  "STATUS": "SUCCESS",
                  "RESPONSE": {
                      "STATUS_CODE": 200,
                      "MESSAGE": "tag update successfully",
                      "DATA": "tag update successfully"
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
        status, data = helper.update_tag_criticality(request_data)
        if status:
            return responseCode.successResponse("Tag update successfully", data)
        if status == False:
            return responseCode.errorResponse(data)
    except Exception as e:
        return responseCode.errorResponse(str(e))

@csrf_exempt
@api_view(('POST',))
def store_part_family(request):
    """
    This API is called for get new token..
    url : "part_family/store-part-family"
    @payload = {
                "part_family_name":"Wiring Harness",
                "shop_types":["Chassis","Engine","Cab"],
                "tags":[1,2,3]
                }
    success response :
        {
            "STATUS": "SUCCESS",
            "RESPONSE": {
                "STATUS_CODE": 200,
                "MESSAGE": "tag store successfully",
                "DATA": "tag created successfully"
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
        status, data = helper.store_part_family(request_data)
        if status:
            return responseCode.successResponse("Tag update successfully", data)
        if status == False:
            return responseCode.errorResponse(data)
    except Exception as e:
        return responseCode.errorResponse(str(e))

@csrf_exempt
@api_view(('PUT',))
def update_part_family(request):
    """
       This API is called for get new token..
       url : "part_family/update-part-family"
       @payload = {
                   "part_family_name":"Wiring Harness",
                   "shop_types":["Chassis","Engine","Cab"],
                   "tags":[1,2,3]
                   }
       success response :
           {
               "STATUS": "SUCCESS",
               "RESPONSE": {
                   "STATUS_CODE": 200,
                   "MESSAGE": "Tag update successfully",
                   "DATA": "Tag update successfully"
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
        status, data = helper.update_part_family(request_data)
        if status:
            return responseCode.successResponse("Tag update successfully", data)
        if status == False:
            return responseCode.errorResponse(data)
    except Exception as e:
        return responseCode.errorResponse(str(e))

@csrf_exempt
@api_view(('GET',))
def get_part_family(request):
    """
       This API is called for get new token..
       url : "part_family/get-part-family"
       @payload = {}
       success response :
           {
               "STATUS": "SUCCESS",
               "RESPONSE": {
                   "STATUS_CODE": 200,
                   "MESSAGE": "Part Family fetch successfully",
                   "DATA": [
                                    {
                                    "id": 4,
                                    "part_family_name": "WIRING HARNESS",
                                    "created_by": "configurator-service",
                                    "created_on": "2022-10-12T17:22:23.215280+05:30",
                                    "is_active": true,
                                    "is_deleted": false,
                                    "updated_by": "configurator-service",
                                    "updated_on": "2022-10-12T17:22:23.215280+05:30",
                                    "shop_type": [],
                                    "tags": []
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
        status, data = helper.get_part_family(request_data)
        if status:
            return responseCode.successResponse("Part family fetch successfully", data)
        if status == False:
            return responseCode.errorResponse(data)
    except Exception as e:
        return responseCode.errorResponse(str(e))

@csrf_exempt
@api_view(('GET',))
def get_tags(request):
    """
       This API is called for get new token..
       url : "part_family/get-tags"
       @payload = {}
       success response :
           {
               "STATUS": "SUCCESS",
               "RESPONSE": {
                   "STATUS_CODE": 200,
                   "MESSAGE": "tag Fetch successfully",
                   "DATA": [
                        {
                        "id": 1,
                        "tag_name": "EMISSION",
                        "created_by": "configurator-service",
                        "created_on": "2022-10-12T16:48:55.790476+05:30",
                        "is_active": true,
                        "is_deleted": false,
                        "updated_by": "configurator-service",
                        "updated_on": "2022-10-12T16:48:55.790476+05:30"
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
        status, data = helper.get_tags(request_data)
        if status:
            return responseCode.successResponse("Tag Fetch successfully", data)
        if status == False:
            return responseCode.errorResponse(data)
    except Exception as e:
        return responseCode.errorResponse(str(e))

@csrf_exempt
@api_view(('DELETE',))
def delete_part_family(request):
    """
           This API is called for get new token..
           url : "part_family/delete_part_family"
           @payload = {}
           success response :
               {
                   "STATUS": "SUCCESS",
                   "RESPONSE": {
                       "STATUS_CODE": 200,
                       "MESSAGE": "tag Fetch successfully",
                       "DATA": [
                            {
                            "id": 1,
                            "tag_name": "EMISSION",
                            "created_by": "configurator-service",
                            "created_on": "2022-10-12T16:48:55.790476+05:30",
                            "is_active": true,
                            "is_deleted": false,
                            "updated_by": "configurator-service",
                            "updated_on": "2022-10-12T16:48:55.790476+05:30"
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
        status, data = helper.delete_part_family(request_data)
        if status:
            return responseCode.successResponse("Part family deleted", data)
        if status == False:
            return responseCode.errorResponse(data)
    except Exception as e:
        return responseCode.errorResponse(str(e))
