from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  User
        fields =  ["id", 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}, 
                        'email':{'required':True}}
    
    def validate(self, data):
        
        data = super().validate(data)
        email = data.get('email', None)
        qs = User.objects.filter(email = email, is_active = True)
        if qs.exists():
            raise ValidationError({"email": "A user with that email address already exists"})
        return data
    

class UnsubscribeUserSerializer(serializers.Serializer):
    
    def update(self, instance, validated_data):
        instance.is_active = False
        instance.save()
        return instance
