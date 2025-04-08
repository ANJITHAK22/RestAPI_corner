from .models import user
from  rest_framework import serializers

class apiserializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields = '__all__'
