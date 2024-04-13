from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from account.models import Vendor


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        first_name = validated_data.get('first_name') or ""
        last_name = validated_data.get('last_name') or ""
        email = validated_data.get('email') or ""
        user = User.objects.create_user(username=username, password=password,
                                   first_name=first_name, last_name=last_name, email=email)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        first_name = validated_data.get('first_name') or ""
        last_name = validated_data.get('last_name') or ""
        phone = validated_data.get('phone') or ""
        address = validated_data.get('address') or ""
        email = validated_data.get('email') or ""
        user = Vendor.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            address=address,
            email=email
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs
