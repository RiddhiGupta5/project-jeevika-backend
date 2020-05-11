from rest_framework import serializers
from .models import (CustomToken, CustomUser, Donation, HelpProgram, 
                     Organization)

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'phone_no', 'address', 'password')

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')

class HelpProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpProgram
        fields = "__all__"
        
class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = "__all__"