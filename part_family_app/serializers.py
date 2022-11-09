from django.core import serializers
from part_family_app.models import (TagCriticality,PartFamily,PartFamilyTagCriticalityMapping,PartFamilyShopMapping,PartFamilyTagCriticalityMapping)
from rest_framework import serializers


class TagCriticalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TagCriticality
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




class PartFamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = PartFamily
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


class PartFamilyShopMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartFamilyShopMapping
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

class PartFamilyTagCriticalityMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartFamilyTagCriticalityMapping
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