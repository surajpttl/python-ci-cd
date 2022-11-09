from django.test import TestCase
from django.utils import timezone
updated_on = timezone.now()
import json
from django.test import Client
from django.urls import reverse
from part_family_app.models import (TagCriticality,PartFamily,PartFamilyShopMapping,PartFamilyTagCriticalityMapping)
# Create your tests here.
class PartFamilyTestCase(TestCase):
    def setUp(self):
        pass
    def test_tag_criticality(self):
        tags_payload = {
                "tag_name":"      QUAlity      "
                }
        response = self.client.post("/part-family/store-tag-criticality", content_type='application/json',
                                    data=tags_payload)
        self.assertEqual(response.status_code, 200)
    def test_store_part_family(self):
        part_family_data = {
            "part_family_name": "Wiring Harness",
            "shop_types": ["Chassis", "Engine", "Cab"],
            "tags": [1, 2, 3]
        }
        response = self.client.post("/part-family/store-part-family", content_type='application/json',data=part_family_data)
        self.assertEqual(response.status_code, 200)
