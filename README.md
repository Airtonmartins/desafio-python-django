# API RESTful de usuários + login

A aplicação consiste em uma API de usuários que possui endpoints para criação, autenticação e visualização de um usuário. Para criação dessa API foi utilizado Django e Django Rest Framework, utilizado Docker e Docker Compose para construir o ambiente local e Heroku como ambiente na nuvem. O domínio da aplicação encontra-se no link https://desafio-django-pitang.herokuapp.com. Abaixo segue os endpoints que foram criados:
 

### POST - /api/signup

* Endpoint que cadastra um novo usuário e retorna o token. Segue exemplo do body da requisição:

```json
    {
      "first_name": "First Name",
      "last_name": "Last name",
      "email": "email123@email.com",
      "password": "password",
      "phones": [
        {
          "number": 999999999,
          "area_code": 81,
          "country_code": "+55"
        }
      ]
    }
```

### POST - /api/signin
* Endpoint que retorna o token de autenticação. Segue exemplo do body da requisição:

```json
    {
      "email": "email123@email.com",
      "password": "password"
    }
```

### GET - /api/me 
* Endpoint que retorna informações do usuário autenticado. É necessário inserir o atributo ``Authorization`` nos headers da requisição, exemplo:

```json
    Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Im....
```

Na raiz do projeto encontra-se o arquivo postman chamado ``Desafio Django Pitang.postman_collection.json``, que pode ser importado e utilizado pra executar as requisições ao host do Heroku.





## Executando aplicação em um Ambiente local:

Para utilizar a aplicação em ambiente local é necessário ter o ``Docker`` e ``Docker Composer`` instalados e executar os seguintes passos:

* Crie um arquivo chamado ``.env`` na raiz do projeto e insira as seguintes variáveis:

```txt
    SECRET_KEY=jkahsdfjkhasldjfgahsd5
    DEBUG=False
    HOST=0.0.0.0:8000
```

* Execute o projeto com o comando:

```sh
    docker-compose up -d --build
```
* Aplicação vai fazer o build, executar os testes e em seguida o ``guinicorn``. Execute o comando a baixo para ver os logs:

```sh
    docker logs desafio-python-django_api_1 -f
```

* A aplicação estará em execução quando apresentar os seguintes logs:

```sh
    Applying users.0007_remove_user_updated_at... OK
    Applying users.0008_auto_20201115_0251... OK
    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).
    ............
    ----------------------------------------------------------------------
    Ran 12 tests in 1.136s

    OK
    Destroying test database for alias 'default'...
    [2020-11-15 23:31:45 +0000] [9] [INFO] Starting gunicorn 20.0.4
    [2020-11-15 23:31:45 +0000] [9] [INFO] Listening at: http://0.0.0.0:8000 (9)
    [2020-11-15 23:31:45 +0000] [9] [INFO] Using worker: sync
    [2020-11-15 23:31:45 +0000] [12] [INFO] Booting worker with pid: 12

```

* A API poderá ser acessada localmente pelo host http://0.0.0.0:8000

## Executando os testes no ambiente local

### Com o ambiente já em execução, entre no container para executar os testes utilizando os seguintes comandos:

```sh
    docker exec -it desafio-python-django_api_1 bash
    cd djangochallenge/
    python manage.py test
```



