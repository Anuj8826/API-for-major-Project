from rest_framework import serializers
from .models import User, USER_TYPE
from django.contrib.auth.models import Group

class GroupSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('name', 'id')

    def validate(self, value):
        print "sdada"
        return value

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email','groups')
        depth = 1
        readonlyfields = ('id', 'groups')
        write_only_fields = ('password',)

    def create(self, validated_data):
        print validated_data

        ud = User(**validated_data)
        ud.is_active = True
        ud.save()
        ud.add_to_group('EMPLOYEE')
        ud.save()
        # ud.set_unusable_password()
        return ud

class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'groups')
        depth = 1
        readonlyfields = ('id', 'groups')
        write_only_fields = ('password',)

    def create(self, validated_data):
        print validated_data
        
        ud = User(**validated_data)
        ud.is_active = True
        ud.save()
        ud.add_to_group('MANAGER')
        ud.save()
        return ud
