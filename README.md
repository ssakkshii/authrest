# authrest

Description:
A REST API using django-restframework authentication and authorization support.

login api: 
POST: /login

Create a folder:
POST: http://127.0.0.1:8000/folder/
{name: 'folder_name_to_be_created'}

Delete folder:
DELETE: http://127.0.0.1:8000/folder/
{name: 'folder_name_to_be_created'}

Upload a file:
POST: http://127.0.0.1:8000/files/

Delete file:
DELETE: http://127.0.0.1:8000/files/<file_id>/

List of uploaded files:
GET: http://127.0.0.1:8000/files/
