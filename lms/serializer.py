from django.contrib.auth.models import User
from rest_framework import serializers
from lms.models import Leave


class LeaveSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='User.username')

    class Meta:
        model = Leave
        fields = ['id', 'owner', 'start_date', 'end_date', 'leave_type', 'note']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],
                                   first_name=validated_data['first_name'],
                                   last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user
