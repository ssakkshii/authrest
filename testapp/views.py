import os
from rest_framework import viewsets, views

from main.settings import DOCUMENT_DIRECTORY
from testapp.io_utils.utils import IOUtil
from testapp.models import StorageFiles
from testapp.serializers import StorageFileSerializer, FolderSerializer
from rest_framework.permissions import IsAuthenticated
from http import HTTPStatus
from rest_framework.response import Response


class CustomViewSet(viewsets.ModelViewSet):

    def set_request_field(self, request, field, value, *args, **kwargs):
        data = request.data.copy()
        serializer = self.get_serializer(*args, **kwargs)

        if field in serializer.fields.keys():
            data[field] = value
        request._full_data = data
        return request

    def create(self, request, *args, **kwargs):
        user = self.request.user.id
        request = self.set_request_field(request, 'created_by', user, *args, **kwargs)
        return super().create(request, *args, **kwargs)


class StorageFileViewset(CustomViewSet):

    queryset = StorageFiles.objects.all()
    serializer_class = StorageFileSerializer
    permission_classes = [IsAuthenticated]


class FolderView(views.APIView):

    serializer_class = FolderSerializer

    @staticmethod
    def post(request):
        serializer = FolderSerializer(data=request.data)

        if serializer.is_valid():
            folder_name = serializer.validated_data.get('name')

            try:
                folder_path = os.path.join(DOCUMENT_DIRECTORY, folder_name)
                IOUtil.create_directory(folder_path)
            except:
                return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR, data={'success': False})
            return Response(status=HTTPStatus.OK, data={'folder_path': folder_path})

        return Response(status=HTTPStatus.BAD_REQUEST, data={'success': False})

    @staticmethod
    def delete(request):
        serializer = FolderSerializer(data=request.data)

        if serializer.is_valid():
            folder_name = serializer.validated_data.get('name')

            try:
                folder_path = os.path.join(DOCUMENT_DIRECTORY, folder_name)
                IOUtil.delete_directory(folder_path)
            except:
                return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR, data={'success': False})
            return Response(status=HTTPStatus.OK, data={'folder_path': folder_path})

        return Response(status=HTTPStatus.BAD_REQUEST, data={'success': False})



