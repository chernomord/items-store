from django.contrib.auth.models import User
from rest_framework import serializers
from store.models import StoreItem


class StoreItemSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = StoreItem
        fields = ('url', 'id', 'price', 'name', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    storeitem = serializers.PrimaryKeyRelatedField(many=True, queryset=StoreItem.objects.all())

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'storeitem',)
