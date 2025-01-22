from rest_framework import serializers
from .models import CustomUser, Content
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        validators=[validate_password]
    )

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'phone', 'address', 'city', 'state', 'country', 'pincode', 'role', 'password']
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'
