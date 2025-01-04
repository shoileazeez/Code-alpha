from rest_framework import serializers
from .models import User



class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True, required=True)
    class meta:
        models= User
        fiels = ["username", "first_name", "last_name", 
                "email", "role", "password", "password_confirm"]
        
        
    def validate(self, data):
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        
        if len(password) < 8:
            raise serializers.ValidationError(
                "password must contain minimium of 8 character."
            )
        if password != confirm_password:
            raise serializers.ValidationError(
                "password must be the same with confirm password."
            )
        return data
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "A user with this email already exist."
            )
        return value
    def create(self, validated_data):
        validated_data.pop("password_confirm")
        role = validated_data.get(role)
        if not role:
            raise serializers.ValidationError(
                "This field is required."
            )
        user = User(
            email = validated_data["email"],
            username = validated_data["username"],
            first_name = validated_data["first_name"],
            last_name  = validated_data["last_name"],
            role = role,
            is_active  = False,
            role_set_once=True,
        )
        user.set_password(validated_data['password'])
        user.save()
        return user