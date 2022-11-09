from django.conf import settings
import requests
import jwt
from django.utils import timezone
import re
from part_family_app.models import (TagCriticality,PartFamily)
from part_family_app.serializers import (
TagCriticalitySerializer,PartFamilySerializer)
from common_app import validations

def check_tag_name_is_present(tag_name,check_flag,id):
    try:
        if type(tag_name) != str:
            return False,"Tag name must be an String"
        if validations.check_special_characters(tag_name)==False:
            return False, "Special characters are not allow"
        if check_flag == 'insert':
            queryParams = TagCriticality.objects.filter(tag_name=tag_name).first()
        if check_flag == 'update':
            queryParams = TagCriticality.objects.filter(tag_name=tag_name).exclude(id=id).first()
        if queryParams:
            tagCriticalitySerializer = TagCriticalitySerializer(queryParams)
            if len(tagCriticalitySerializer.data) != 0:
                return False, "tag name is already present"
        else:
            return True,""
    except Exception as e:
        return False,str(e)

def trim_string(input):
    input = input.rstrip()
    input = input.lstrip()
    return input

def check_family_name_is_present(part_family_name,check_flag,id):
    try:
        if type(part_family_name) != str:
            return False,"Tag name must be an String"
        if validations.check_special_characters(part_family_name)==False:
            return False, "Special characters are not allow"
        if check_flag == 'insert':
            queryParams = PartFamily.objects.filter(part_family_name=part_family_name,is_active=True,is_deleted=False).first()
        if check_flag == 'update':
            queryParams = PartFamily.objects.filter(part_family_name=part_family_name,is_active=True,is_deleted=False).exclude(id=id).first()
        if queryParams:
            partFamilySerializer = PartFamilySerializer(queryParams)
            if len(partFamilySerializer.data) != 0:
                return False, "Family name is already present"
        else:
            return True,""
    except Exception as e:
        return False,str(e)



