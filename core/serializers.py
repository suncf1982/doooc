from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class GroupsField(serializers.RelatedField):
    def to_representation(self, value):
        # return {'id': value.id, 'value': value.name}
        return value.name


class UserReadonlySerializer(serializers.ModelSerializer):
    groups = GroupsField(many=True, read_only=True)
    last_login = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M:%S', allow_null=True, required=False)

    class Meta:
        model = User
        fields = '__all__'


class UserKVSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'is_active', 'groups', 'password')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            # groups=validated_data['groups'],
            is_active=validated_data['is_active'],
        )
        user.set_password(validated_data['password'])
        user.save()
        group_ids = validated_data['groups']
        for g_id in group_ids:
            user.groups.add(g_id)
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data['email']
        instance.first_name = validated_data['first_name']
        instance.is_active = validated_data['is_active']
        group_ids = validated_data['groups']
        for g_id in group_ids:
            instance.groups.add(g_id)
        instance.save()
        return instance
