# authrest

Description:
A REST API using django-restframework authentication and authorization support.

login api: 
POST: /login

Create a folder:
POST: /folder/
{name: 'folder_name_to_be_created'}

Delete folder:
DELETE: /folder/
{name: 'folder_name_to_be_created'}

Upload a file:
POST: /files/

Delete file:
DELETE: /files/<file_id>/

List of uploaded files:
GET: /files/
