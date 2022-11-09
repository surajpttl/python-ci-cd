from django.test import TestCase
from digital_twin_configure_app.models import (OrganizationMaster,BusinessUnitMaster,PlantMaster,ShopMaster,LineMaster,StationMaster)
from django.utils import timezone
updated_on = timezone.now()
from django.test import Client
from django.urls import reverse

class ConfigutorTestCase(TestCase):
    
    def setUp(self):
        pass
    def test_organization_master(self):     
        response = self.client.get('/digital_twin/fetch-organization-master')
        self.assertEqual(response.status_code, 200)

    def test_business_unit_master(self):     
        response = self.client.get('/digital_twin/fetch-business-unit-master')
        self.assertEqual(response.status_code, 200)

    def test_plant_master(self):     
        response = self.client.get('/digital_twin/fetch-plant-master')
        self.assertEqual(response.status_code, 200)

    def test_shop_master(self):     
        response = self.client.get('/digital_twin/fetch-shop-master')
        self.assertEqual(response.status_code, 200)

    def test_line_master(self):     
        response = self.client.get('/digital_twin/fetch-line-master')
        self.assertEqual(response.status_code, 200)

    def test_station_master(self):     
        response = self.client.get('/digital_twin/fetch-station-master')
        self.assertEqual(response.status_code, 200)

    

    