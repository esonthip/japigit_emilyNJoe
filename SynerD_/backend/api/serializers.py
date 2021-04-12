from rest_framework import serializers
from ..models import UserInfo, Subscriber, Service, Organization
class UserInfoSerializer(serializers.ModelSerializer): 
    class Meta: 

        model = UserInfo
        fields = ['firstname', 'middlename', 'lastname']

class SubscriberSerializer(serializers.ModelSerializer): 
    class Meta: 

        model = Subscriber
        fields = ['username', 'subscriptiontypecode', 'servicecode']

class ServiceSerializer(serializers.ModelSerializer): 
    class Meta: 

        model = Service
        fields = ['servicecode', 'servicename', 'description']

class OrganizationSerializer(serializers.ModelSerializer): 
    class Meta: 

        model = Organization
        fields = ['address1', 'city', 'zipcode']
