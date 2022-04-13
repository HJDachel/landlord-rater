from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    property_street_address = serializers.CharField(max_length=200)
    property_city_address = serializers.CharField(max_length=200)
    property_state_address = serializers.CharField(max_length=200)

    class Meta:
        model = Property
        fields = ('__all__')