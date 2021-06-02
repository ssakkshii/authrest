from rest_framework import serializers

from testapp.models import *


class StorageFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = StorageFiles
        fields = '__all__'


class FolderSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=30)
