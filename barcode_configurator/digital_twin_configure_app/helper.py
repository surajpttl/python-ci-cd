import json
from django.conf import settings
from django.utils import timezone
from digital_twin_configure_app.models import (OrganizationMaster,BusinessUnitMaster,PlantMaster,ShopMaster,LineMaster,StationMaster)
from digital_twin_configure_app.serializers import (
OrganizationSerializer,BusinessUnitSerializer,PlantSerializer,ShopSerializer,LineSerializer,StationSerializer)
from . import validations
from . import api_helper


def generate_token():
    try:
        status,response_data = api_helper.fetch_token("refresh_token")
        if status==False:
            status,response_data = api_helper.fetch_token("access_token")
        if status==True:
            token_information = json.loads(response_data._content)
            if response_data.status_code == 200:
                    settings.DIGITAL_TWIN_ACCESS_TOKEN = token_information.get("access_token")
                    settings.DIGITAL_TWIN_REFRESH_TOKEN = token_information.get("refresh_token")
                    return True,token_information         
        return False,[]
    except Exception as e:
        return False,str(e)  

def fetch_organization_master(request): 
    try:
        end_point = '/plant-master/organizations'
        status,response_data = api_helper.get_api_data(end_point)
        if status:
            organization_information = json.loads(response_data._content)
            if response_data.status_code == 200:
                updated_on = timezone.now()
                for organization in organization_information:
                    if validations.checkValidations("Organization",organization):
                        if updateOrganizationData(organization)==False:
                            obj = OrganizationMaster.objects.create(dt_organization_id=int(organization.get('id')),name=organization.get('name'),updated_on=updated_on)
                            obj.save()
                return True,organization_information
            elif response_data.status_code==401:
                generate_token()
                return fetch_organization_master(request)
        else:
            generate_token()
            return fetch_organization_master(request)            
    except Exception as e:
        return str(e)

def updateOrganizationData(organization,*args, **kwargs):
    try:
        updated_on = timezone.now()
        queryParams  = OrganizationMaster.objects.filter(dt_organization_id=int(organization.get('id'))).first()
        if queryParams:
            organizationSerializer = OrganizationSerializer(queryParams)
            if len(organizationSerializer.data) != 0:
                    instance =  queryParams
                    serializer = OrganizationSerializer(
                    instance,
                    data={'name':organization.get('name'),'updated_on':updated_on},
                    partial=True
                    )
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    return True
        return False
    except Exception as e:
        return False

def fetch_business_unit_master(request):
    try:
        end_point = '/plant-master/business-units'
        status,response_data = api_helper.get_api_data(end_point)
        if status:        
            business_unit_information = json.loads(response_data._content)
            if response_data.status_code == 200:
                updated_on = timezone.now()
                for business_unit in business_unit_information:
                    if validations.checkValidations("BusinessUnit",business_unit):
                        if updateBusinessUnitData(business_unit)==False:
                            obj = BusinessUnitMaster.objects.create(dt_business_unit_id=business_unit.get('id'),name=business_unit.get('name'),updated_on=updated_on)
                            obj.save()
                return True,business_unit_information
            elif response_data.status_code==401:
                generate_token()
                return fetch_business_unit_master(request)
        else:
            generate_token()
            return fetch_business_unit_master(request)
    except Exception as e:
            return str(e)

def updateBusinessUnitData(business_unit,*args, **kwargs):
    try:
        updated_on = timezone.now()
        queryParams  = BusinessUnitMaster.objects.filter(dt_business_unit_id=business_unit.get('id')).first()
        if queryParams:
            #businessUnitSerializer = BusinessUnitSerializer(queryParams)
            instance =  queryParams
            serializer = BusinessUnitSerializer(
            instance,
            data={'name':business_unit.get('name'),'updated_on':updated_on},
            partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return True
        return False
    except Exception as e:
        return False

def fetch_plant_master(request):
    try:
        end_point = '/plant-master/plants'
        status,response_data = api_helper.get_api_data(end_point)
        if status: 
            plant_information = json.loads(response_data._content)
            if response_data.status_code == 200:
                updated_on = timezone.now()
                for plant in plant_information:
                    if validations.checkValidations("Plant",plant):
                        if updatePlantMasterData(plant)==False:
                            businessUnit = plant.get('businessUnit')
                            obj = PlantMaster.objects.create(dt_plant_id=int(plant.get('id')),name=plant.get('name'),city=plant.get('city'),state=plant.get('state'),country=plant.get('country'),dt_business_unit_id=BusinessUnitMaster.objects.get(dt_business_unit_id=businessUnit.get('id')),updated_on=updated_on)
                            obj.save()
                return True,plant_information
            elif response_data.status_code==401:
                generate_token()
                return fetch_plant_master(request)
        else:
            generate_token()
            return fetch_plant_master(request)
                
    except Exception as e:
        return str(e) 

def updatePlantMasterData(plant,*args, **kwargs):
    try:
        updated_on = timezone.now()
        queryParams  = PlantMaster.objects.filter(dt_plant_id=int(plant.get('id'))).first()
        if queryParams:
            businessUnit = plant.get('businessUnit')
            instance =  queryParams
            serializer = PlantSerializer(
            instance,
            data={
                "name":plant.get('name'),
                "city":plant.get('city'),
                "state":plant.get('state'),
                "country":plant.get('country'),
                "dt_business_unit_id":BusinessUnitMaster.objects.get(dt_business_unit_id=businessUnit.get('id')).id,
                "updated_on":updated_on
                },
            partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return True
        return False
    except Exception as e:
        return False

def fetch_shop_master(request):
    try:
        end_point = '/plant-master/shops'
        status,response_data = api_helper.get_api_data(end_point)
        if status:  
            shop_information = json.loads(response_data._content)
            if response_data.status_code == 200:
                updated_on = timezone.now()
                for shop in shop_information:
                    if validations.checkValidations("Shop",shop):
                        if updateShopMasterData(shop)==False:
                            plantData = shop.get('plant')
                            obj = ShopMaster.objects.create(dt_shop_id=int(shop.get('id')),name=shop.get('name'),description=shop.get('description'),shop_type=shop.get('type'),dt_plant_id=PlantMaster.objects.get(dt_plant_id=plantData.get('id')),updated_on=updated_on)
                            obj.save()
                return True,shop_information
            elif response_data.status_code==401:
                    generate_token()
                    return fetch_shop_master(request)
        else:
            generate_token()
            return fetch_shop_master(request)
    except Exception as e:
        return str(e)

def updateShopMasterData(shop,*args, **kwargs):
    try:
        updated_on = timezone.now()
        queryParams  = ShopMaster.objects.filter(dt_shop_id=int(shop.get('id'))).first()
        if queryParams:
            #businessUnitSerializer = BusinessUnitSerializer(queryParams)
            plantData = shop.get('plant')
            instance =  queryParams
            serializer = ShopSerializer(
            instance,
            data={
                "name":shop.get('name'),
                "description":shop.get('description'),
                "shop_type":shop.get('type'),
                "dt_plant_id":PlantMaster.objects.get(dt_plant_id=plantData.get('id')).id,
                "updated_on":updated_on
                },
            partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return True
        return False
    except Exception as e:
        return False

def fetch_line_master(request):
    try:
        end_point = '/plant-master/lines'
        status,response_data = api_helper.get_api_data(end_point)
        if status:
            line_information = json.loads(response_data._content)
            if response_data.status_code == 200:
                updated_on = timezone.now()
                for line in line_information:
                    if validations.checkValidations("Line",line):
                        if updateLineMasterData(line)==False:
                            shopData = line.get('shop')
                            obj = LineMaster.objects.create(dt_line_id=int(line.get('id')),name=line.get('name'),description=line.get('description'),dt_shop_id=ShopMaster.objects.get(dt_shop_id=shopData.get('id')),line_type=line.get('type'),updated_on=updated_on)
                            obj.save()
                return True,line_information
            elif response_data.status_code==401:
                    generate_token()
                    return fetch_line_master(request)
        else:
            generate_token()
            return fetch_line_master(request)       
    except Exception as e:
        return str(e) 

def updateLineMasterData(line,*args, **kwargs):
    try:
        updated_on = timezone.now()
        queryParams  = LineMaster.objects.filter(dt_line_id=int(line.get('id'))).first()
        if queryParams:
            #businessUnitSerializer = BusinessUnitSerializer(queryParams)
            shopData = line.get('shop')
            instance =  queryParams
            serializer = LineSerializer(
            instance,
            data={
                "name":line.get('name'),
                "description":line.get('description'),
                "line_type":line.get('type'),
                "dt_shop_id":ShopMaster.objects.get(dt_shop_id=shopData.get('id')).id,
                "updated_on":updated_on
                },
            partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return True
        return False
    except Exception as e:
        return False

def fetch_station_master(request):
    try:
        end_point = '/plant-master/stations'
        status,response_data = api_helper.get_api_data(end_point)
        if status:
            station_information = json.loads(response_data._content)
            if response_data.status_code == 200:
                #return True,station_information
                updated_on = timezone.now()
                for station in station_information:
                    if validations.checkValidations("Station",station):
                        if updateStationMasterData(station)==False:
                            stationData = station.get('line')
                            obj = StationMaster.objects.create(dt_station_id=int(station.get('id')),name=station.get('name'),number=station.get('number'),dt_line_id=LineMaster.objects.get(dt_line_id=stationData.get('id')),updated_on=updated_on)
                            obj.save()
                return True,station_information
            elif response_data.status_code==401:
                generate_token()
                return fetch_station_master(request)
        else:
            generate_token()
            return fetch_station_master(request)
    except Exception as e:
        return str(e)

def updateStationMasterData(station,*args, **kwargs):
    try:
        updated_on = timezone.now()
        queryParams  = StationMaster.objects.filter(dt_station_id=int(station.get('id'))).first()
        if queryParams:
            #businessUnitSerializer = BusinessUnitSerializer(queryParams)
            stationData = station.get('line')
            instance =  queryParams
            serializer = StationSerializer(
            instance,
            data={
                "name":station.get('name'),
                "number":station.get('number'),
                "dt_line_id":LineMaster.objects.get(dt_line_id=stationData.get('id')).id,
                "updated_on":updated_on
                },
            partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return True
        return False
    except Exception as e:
        return False
 
 
