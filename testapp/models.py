from django.db import models
import os
from django.contrib.auth.models import User
from django.db.models import DO_NOTHING


def get_file_path(instance, filename):
    return os.path.join(str(instance.created_by.username), filename)


class StorageFiles(models.Model):

    name = models.CharField(max_length=200, blank=False, null=False)
    file = models.FileField(null=False, db_column="file", blank=False, upload_to=get_file_path)
    created_by = models.ForeignKey(User, related_name='file_user', on_delete=DO_NOTHING)

    def delete(self, *args, **kwargs):
        self.file.storage.delete(self.file.name)
        super(StorageFiles, self).delete()

    def __str__(self):
        return self.name
