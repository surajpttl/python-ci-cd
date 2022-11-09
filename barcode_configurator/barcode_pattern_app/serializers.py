from django.core import serializers
from barcode_pattern_app.models import (BarcodePatternMaster,BarcodeShopMapping)
from rest_framework import serializers


class BarcodePatternMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarcodePatternMaster
        fields = ('__all__')
    def to_representation(self, instance):
        my_fields = {'description','updated_on'}
        data = super().to_representation(instance)
        for field in my_fields:
            try:
                if not data[field]:
                    data[field] = ""
            except KeyError:
                pass
        return data


class BarcodeShopMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarcodeShopMapping
        fields = ('__all__')
    def to_representation(self, instance):
        my_fields = {'description','updated_on'}
        data = super().to_representation(instance)
        for field in my_fields:
            try:
                if not data[field]:
                    data[field] = ""
            except KeyError:
                pass
        return data