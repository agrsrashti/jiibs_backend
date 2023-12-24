from rest_framework import serializers
from jiibs_backend.models import Users

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'mobile_no','email','dob','role','property_name','property_management_company']
