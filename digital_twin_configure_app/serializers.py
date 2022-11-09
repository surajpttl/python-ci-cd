from django.core import serializers
from digital_twin_configure_app.models import (OrganizationMaster,BusinessUnitMaster,PlantMaster,ShopMaster,LineMaster,StationMaster)
from rest_framework import serializers


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationMaster
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

class BusinessUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessUnitMaster
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

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantMaster
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

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopMaster
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

class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineMaster
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



class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StationMaster
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

