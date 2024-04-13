from .models import Service, Plan, Event, VendorService, Vendorlist
from rest_framework import serializers


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class VendorlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendorlist
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class VendorServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorService
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    services = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'

    def get_services(self, obj):
        obj_services = obj.services.all()
        return ServiceSerializer(obj_services, many=True, context={"event_instance": obj}).data
