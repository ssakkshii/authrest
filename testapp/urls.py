from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main import settings
from testapp import views
from django.conf.urls import url

router = DefaultRouter()

router.register(r'files', views.StorageFileViewset)

# TODO : Check view route register
urlpatterns = [
    path('', include(router.urls)),
    url(r'folder/', views.FolderView.as_view()),
]