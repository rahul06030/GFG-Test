from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
    def create(self, validated_data):
        user = Customer(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
