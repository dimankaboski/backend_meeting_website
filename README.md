# backend_meeting_website

## Ссылка на проект:
http://astro.dimankab1.fvds.ru/api/list

## Авторизация:
### JWT
Bearer {TOKEN}

## API
### /api/list
Список пользователей
#### Filters:
- distance - по удаленности в км (int)
- sex - по полу (str)
- first_name - по имени (str)
- last_name - по фамилии (str)
### /api/clients/create
Добавить пользователя
### /api/clients/{id}/match
Оценить пользователя
### /api/clients/token
Получить access/refresh токены
