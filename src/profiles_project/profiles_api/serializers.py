from rest_framework import serializers
from . import models


class HelloSerializers(serializers.Serializer):
    """ serializers a name field for testing our API view """

    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """ A Model Serializer class """

    class Meta:
        model = models.UserProfile
        fields = ['id','name','email','password']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        """ Create and retuns user data """

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
            )
        user.set_password(validated_data['password'])
        user.save()

        return user
