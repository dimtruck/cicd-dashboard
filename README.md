# CI-CD Dashboard application

Contains api endpoints for ci/cd dashboard.

## Getting started

Make sure you have docker installed on your machine:

* `docker build -t local .`
* `docker run -ti --rm -p 8080:8000 -v $(pwd):/opt/local local`
* `gunicorn -b 0.0.0.0:8000 app:app`

## API endponts

### Applications

`GET /apps`

`POST /apps`

`DELETE /apps/{id}`

`PUT /apps/{id}`

### Questions

`GET /questions`

`POST /questions`

`DELETE /questions/{id}`

`PUT /questions/{id}`

`GET /questions/{id}/votes`

`POST /questions/{id}/votes`