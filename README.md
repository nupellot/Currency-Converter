# Конвертер валют
Сервис для конвертации валют, работающий по API
### Пример GET-запроса
/api/rates?from=USD&to=RUB&value=1
### Пример ответа сервера
{ 
  "result": 62.16 
}

Информацию об актуальных курсах валют сервис черпает из https://www.cbr-xml-daily.ru/daily_json.js

### Контейнеризация
Конфигурационный файл Dockerfile настроен для создания подходящего для контейнеризации образа.
Готовый образ можно получить по ссылке https://hub.docker.com/repository/docker/nupellot/currency-converter/general
