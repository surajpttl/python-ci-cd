import json
import jwt
from datetime import datetime, timezone
from django.conf import settings
import requests
from django.utils import timezone
from django.utils import timezone
from part_family_app.models import (TagCriticality,PartFamily,PartFamilyShopMapping,PartFamilyTagCriticalityMapping)
from part_family_app.serializers import (
TagCriticalitySerializer,PartFamilySerializer,PartFamilyShopMappingSerializer,PartFamilyTagCriticalityMappingSerializer)
from . import validations

def store_tag_criticality(request_data):
    try:
        if len(request_data['tag_name'])<=0:
            return False,"Tag name should not be blank"
        request_data['tag_name'] = request_data['tag_name'].upper()
        request_data['tag_name'] = validations.trim_string(request_data['tag_name'])
        status,message = validations.check_tag_name_is_present(request_data['tag_name'],'insert',0)
        if status==False:
            return status,message
        updated_on = timezone.now()
        created_by = request_data['created_by']
        updated_by = request_data['updated_by']
        obj = TagCriticality.objects.create(tag_name=request_data['tag_name'],created_by=created_by,created_on=updated_on, is_active=True, updated_by=updated_by,updated_on=updated_on)
        return True, "Tag created successfully"
    except Exception as e:
        return False,str(e)

def update_tag_criticality(request_data):
    try:
        if len(request_data['tag_name'])<=0:
            return False,"Tag name should not be blank"
        queryParams = TagCriticality.objects.filter(id=request_data['id'], is_active=True,
                                                          is_deleted=False).first()
        if queryParams == None:
            return False, "Record not found or not active now"
        request_data['tag_name'] = request_data['tag_name'].upper()
        request_data['tag_name'] = validations.trim_string(request_data['tag_name'])
        status,message = validations.check_tag_name_is_present(request_data['tag_name'],'update',request_data['id'])
        if status==False:
            return status,message
        updated_on = timezone.now()
        updated_by = request_data['updated_by']
        updateData = {
            "tag_name": request_data["tag_name"],
            "updated_by": updated_by,
            "updated_on": updated_on
        }
        instance = TagCriticality.objects.filter(id=int(request_data['id'])).first()
        if instance:
            serializer = TagCriticalitySerializer(
                instance,
                data=updateData,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return True, "Data Update successfully"
    except Exception as e:
        return False,str(e)

def store_part_family(request_data):
    try:
        if len(request_data['part_family_name']) <= 0:
            return False, "Part family name should not be blank"
        if len(request_data['shop_types']) <= 0:
            return False, "Shop type should not be blank"
        if len(request_data['tags']) <= 0:
            return False, "Tags should not be blank"
        request_data['part_family_name'] = request_data['part_family_name'].upper()
        request_data['part_family_name'] = validations.trim_string(request_data['part_family_name'])
        status, message = validations.check_family_name_is_present(request_data['part_family_name'], 'insert', 0)
        if status==False:
            return status,message
        updated_on = timezone.now()
        created_by = request_data['created_by']
        updated_by = request_data['updated_by']
        obj = PartFamily.objects.create(part_family_name=request_data['part_family_name'],created_by=created_by,created_on=updated_on,is_active=True,updated_by=updated_by,updated_on=updated_on)
        last_inserted_query = PartFamily.objects.latest('id')
        partFamilySerializer = PartFamilySerializer(last_inserted_query)
        status, message = store_shop_mapping(request_data['shop_types'], partFamilySerializer.data['id'],
                                             request_data['created_by'], "multiple")
        if status==True:
            status, message = store_tag_mapping(request_data['tags'], partFamilySerializer.data['id'],
                                                 request_data['created_by'],'multiple')

            return True,"Part Family created successfully "

    except Exception as e:
        return False,str(e)

def store_tag_mapping(tags,id,user,type):
    created_by = user
    updated_by = user
    updated_on = timezone.now()
    try:
        if type=="single":
            obj = PartFamilyTagCriticalityMapping.objects.create(tag_criticality_id=TagCriticality.objects.get(id=int(tags)),part_family_id=PartFamily.objects.get(id=id),created_by=created_by,created_on=updated_on, is_active=True, updated_by=updated_by, updated_on=updated_on)
        else:
            for tag in tags:
                obj = PartFamilyTagCriticalityMapping.objects.create(tag_criticality_id=TagCriticality.objects.get(id=int(tag)), part_family_id=PartFamily.objects.get(id=id),created_by=created_by, created_on=updated_on,is_active=True,updated_by=updated_by,updated_on=updated_on)
            return True,"Part Family shop type created successfully"
    except Exception as e:
        print(str(e))
        return False,str(e)


def store_shop_mapping(shop_types,id,user,type):
    created_by = user
    updated_by = user
    updated_on = timezone.now()
    try:
        if type=="single":
            obj = PartFamilyShopMapping.objects.create(shop_type=shop_types.upper(),part_family_id=PartFamily.objects.get(id=id),
                created_by=created_by,created_on=updated_on, is_active=True, updated_by=updated_by, updated_on=updated_on)
        else:
            for shop_type in shop_types:
                obj = PartFamilyShopMapping.objects.create(shop_type=shop_type.upper(), part_family_id=PartFamily.objects.get(id=id),created_by=created_by, created_on=updated_on,is_active=True,updated_by=updated_by,updated_on=updated_on)
            return True,"Part Family shop type created successfully"
    except Exception as e:
        return False,str(e)


def update_part_family(request_data):
    try:
        queryParams = PartFamily.objects.filter(id=request_data['id'], is_active=True,
                                                    is_deleted=False).first()
        if queryParams == None:
            return False, "Record not found or not active now"
        if len(request_data['part_family_name']) <= 0:
            return False, "Part family name should not be blank"
        if len(request_data['shop_types']) <= 0:
            return False, "Shop type should not be blank"
        if len(request_data['tags']) <= 0:
            return False, "Tags should not be blank"
        request_data['part_family_name'] = request_data['part_family_name'].upper()
        request_data['part_family_name'] = validations.trim_string(request_data['part_family_name'])
        status, message = validations.check_family_name_is_present(request_data['part_family_name'], 'update', request_data['id'])
        if status==False:
            return status,message
        updated_on = timezone.now()
        created_by = request_data['created_by']
        updated_by = request_data['updated_by']
        updateData = {
            "part_family_name": request_data["part_family_name"],
            "updated_by": updated_by,
            "updated_on": updated_on
        }
        instance = PartFamily.objects.filter(id=int(request_data['id'])).first()
        update_status = False
        if instance:
            serializer = PartFamilySerializer(
                instance,
                data=updateData,
                partial=True
            )
            update_status = serializer.is_valid(raise_exception=True)
            serializer.save()
        shop_status,message = update_shop_mapping(request_data)
        tag_status, message = update_tag_criticality_mapping(request_data)
        if update_status==True and shop_status==True and tag_status==True:
            return True, "Part Family created successfully "
        else:
            return True,"Somethong went wrong"
    except Exception as e:
        return False,str(e)

def update_shop_mapping(request_data):
    try:
        shop_types_upper = [shop_type.upper() for shop_type in request_data['shop_types']]
        queryParams = PartFamilyShopMapping.objects.filter(
            part_family_id=PartFamily.objects.get(id=request_data['id'])).exclude(
            shop_type__in=list(shop_types_upper))
        if queryParams:
            partFamilyShopMappingSerializer = PartFamilyShopMappingSerializer(queryParams, many=True)
            for deleteItem in partFamilyShopMappingSerializer.data:
                PartFamilyShopMapping.objects.filter(id=deleteItem['id']).delete()
        for shop_type in shop_types_upper:
            queryParams = PartFamilyShopMapping.objects.filter(
                part_family_id =PartFamily.objects.get(id=request_data['id']), shop_type=shop_type)
            if not queryParams:
                store_shop_mapping(shop_type, request_data['id'], request_data['updated_by'], 'single')
        return True,"Shop mapping update"
    except Exception as e:
        return False,str(e)

def update_tag_criticality_mapping(request_data):
    try:
        queryParams = PartFamilyTagCriticalityMapping.objects.filter(
            part_family_id=PartFamily.objects.get(id=request_data['id'])).exclude(
            tag_criticality_id__in=list(request_data['tags']))
        if queryParams:
            partFamilyTagCriticalityMappingSerializer = PartFamilyTagCriticalityMappingSerializer(queryParams, many=True)
            for deleteItem in partFamilyTagCriticalityMappingSerializer.data:
                PartFamilyTagCriticalityMapping.objects.filter(id=deleteItem['id']).delete()
        for tag in request_data['tags']:
            queryParams = PartFamilyTagCriticalityMapping.objects.filter(
                part_family_id=PartFamily.objects.get(id=request_data['id']), tag_criticality_id=TagCriticality.objects.get(id=int(tag)))
            if not queryParams:
                store_shop_mapping(tag, request_data['id'], request_data['updated_by'], 'single')
        return True, "Shop mapping update"
    except Exception as e:
        return False,str(e)


def get_part_family(request_data):
    queryParams = PartFamily.objects.filter(is_active=True, is_deleted=False).order_by('id')
    if not queryParams:
        return True, "No more record found"
    partFamilySerializer = PartFamilySerializer(queryParams, many=True)
    all_part_family = []
    for part_family in partFamilySerializer.data:
        shop_mapping_query = PartFamilyShopMapping.objects.filter(
            part_family_id=PartFamily.objects.get(id=part_family['id']),is_active=True)
        part_family['shop_type'] = PartFamilyShopMappingSerializer(shop_mapping_query, many=True).data
        tag_mapping_query = PartFamilyTagCriticalityMapping.objects.filter(
            part_family_id=PartFamily.objects.get(id=part_family['id']),is_active=True)
        part_family['tags'] = PartFamilyTagCriticalityMappingSerializer(tag_mapping_query, many=True).data
        all_part_family.append(part_family)
    return True, partFamilySerializer.data


def get_tags(request_data):
    tag_query = TagCriticality.objects.filter(is_active=True)
    if not tag_query:
        return True, "No more record found"
    tagCriticalitySerializer = TagCriticalitySerializer(tag_query, many=True)
    return True, tagCriticalitySerializer.data

def delete_part_family(request_data):
    try:
        updated_on = timezone.now()
        updated_by = request_data['updated_by']
        updateData = {
            "is_active": False,
            "is_deleted": True,
            "updated_by": updated_by,
            "updated_on": updated_on
        }
        instance = PartFamily.objects.filter(id=int(request_data['id'])).first()
        update_status = False
        if instance:
            serializer = PartFamilySerializer(
                instance,
                data=updateData,
                partial=True
            )
            update_status = serializer.is_valid(raise_exception=True)
            serializer.save()
            return update_status,"Part Family Deleted successfully"
    except Exception as e:
        return False,str(e)
