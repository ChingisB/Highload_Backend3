from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import KeyValuePropertyModel
from .serializers import KeyValueSerializer

class KeyValueView(APIView):
    def get(self, request, key):
        try:
            kv = KeyValuePropertyModel.objects.get(key=key)
            serializer = KeyValueSerializer(kv)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except KeyValuePropertyModel.DoesNotExist:
            return Response({"error": "Key not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, key):
        data = {'key': key, 'value': request.data.get('value')}
        try:
            kv = KeyValuePropertyModel.objects.get(key=key)
            serializer = KeyValueSerializer(kv, data=data)
        except KeyValuePropertyModel.DoesNotExist:
            serializer = KeyValueSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)