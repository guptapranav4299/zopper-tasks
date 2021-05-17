from .models import UserModel
from django.core.exceptions import ValidationError
from rest_framework import fields, serializers

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})
    re_password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = UserModel
        fields =[
            'first_name',
            'last_name',
            'email',
            'password',
            're_password',
        ]
    
    def create(self, validated_data):

        return UserModel.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.title = validated_data.get('first_name', instance.first_name)
        instance.code = validated_data.get('last_name', instance.last_name)
        instance.linenos = validated_data.get('email', instance.email)
        instance.language = validated_data.get('password', instance.password)
        instance.style = validated_data.get('re_password', instance.re_password)
        instance.save()
        return instance


# check if password is re entered correctly
    def validate(self,data):
        if not data['email'].endswith('@zopper.com'):
            raise serializers.ValidationError('Please use zopper id')

        if not data['password'] == data['re_password']:
            raise ValidationError("Passwords do not match")
        return data


