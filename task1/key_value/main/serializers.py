from rest_framework.serializers import Serializer, ModelSerializer
from .models import KeyValuePropertyModel


class KeyValueSerializer(ModelSerializer):
    class Meta:
        model = KeyValuePropertyModel
        fields = ['key', 'value']