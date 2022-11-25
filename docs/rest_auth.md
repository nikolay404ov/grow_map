# General description of auth API

SWAGGER adress - http://{server_url}/docs

## users endpoints

PATCH
/api/v1/change_password

GET
/api/v1/history

GET
/api/v1/is_active

POST
/api/v1/login

POST
/api/v1/logout

GET
/api/v1/profile

POST
/api/v1/refresh

POST
/api/v1/registration

## role

PATCH
/api/v1/change_role

POST
/api/v1/create_role

DELETE
/api/v1/delete_role

GET
/api/v1/list_role

## permission

GET
/api/v1/check_role

POST
/api/v1/grant_role

DELETE
/api/v1/take_role