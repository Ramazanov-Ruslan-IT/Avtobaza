

# BSP: Basic Microservices Platform

Данный репозиторий является основной документацией архитектуры BSP _(Basic microservices platform)_ а также содержит пример реализации файлового дерева для удобной поддержки и перехода на архитектуру BSP _(Basic microservices platform)_



### Полезные ссылки
- [Описание архитектуры](#описание-архитектуры)
- [Файловое дерево](#файловое-дерево)
- [Запуск сервиса локально](#команды-для-запуска-сервиса-локально)
- [Запуск в Docker](#команды-для-запуска-сервиса-на-базе-docker)

## Описание архитектуры 
1

---

## Описание файловой структуры

<details>
<summary>Файловое дерево</summary>

```shell
|   .env
|   .env.example
|   .gitignore
|   README.md
|   Dockerfile
|   pyproject.toml
|   requirements.txt
|           
\---v1
    |   
    +---src
    |   |   config.py
    |   |   main.py
    |   |   __init__.py
    |   |   
    |   +---api
    |   |   |   __init__.py
    |   |   |   
    |   |   +---grpc
    |   |   +---kafka
    |   |   +---rest
    |   |       |   api_route_factory.py
    |   |       |   lifespan.py
    |   |       |   __init__.py
    |   |       |
    |   |       +---exceptions
    |   |       |   |   app_exceptions.py
    |   |       |   |   raisers.py
    |   |       |   |   __init__.py
    |   |       |   |
    |   |       |   +---schemas
    |   |       |       |   errors.py
    |   |       |       |   responses.py
    |   |       |       |   __init__.py
    |   |       |
    |   |       +---middlewares
    |   |       |   |   cors.py
    |   |       |   |   process_time.py
    |   |       |   |   register.py
    |   |       |   |   security_headers.py
    |   |       |   |   __init__.py
    |   |       |
    |   |       +---routers
    |   |           |   base_router.py
    |   |           |
    |   |           +---example
    |   |               |   dependencies.py
    |   |               |   router.py
    |   |               |   schemas.py
    |   |           
    |   +---app
    |   |   +---dto
    |   |   |   |   example.py
    |   |   |           
    |   |   +---services
    |   |   |   \---example
    |   |   |       |   abs_service.py
    |   |   |       |   dependencies.py
    |   |   |       |   service.py
    |   |   |       |   __init__.py
    |   |   |
    |   |   |               
    |   |   +---solutions
    |   |   |   \---example
    |   |   |           abs_solution.py
    |   |   |           dependencies.py
    |   |   |           solution.py
    |   |   |           __init__.py
    |   |   |           
    |   |   \---utils
    |   |       |   mapper.py
    |   |               
    |   +---db
    |   |   +---models
    |   |   |   |   base_orm.py
    |   |   |   |   example_orm.py
    |   |   |   |   __init__.py
    |   |   |           
    |   |   +---repositories
    |   |   |   |   __init__.py
    |   |   |   |   
    |   |   |   +---example
    |   |   |       |   abs_repo.py
    |   |   |       |   dependencies.py
    |   |   |       |   repo.py
    |   |   |       |   __init__.py
    |   |   |
    |   |   |           
    |   |   \---settings
    |   |       \---connection
    |   |           |   postgresql.py
    |   |           |   redis.py
    |   |           |   __init__.py
    |   |
    |   |                   
    |   +---resources
    |           
    +---tests
```
</details>

---

### Команды для запуска сервиса локально
```shell
cd example_service
```
```shell
python .\v1\src\main.py  
```

---

### Команды для запуска сервиса на базе Docker
```shell
cd example_service
```
```shell
docker build -t example_service .
```
```shell
docker run --name example_service_container --privileged --cap-add=NET_ADMIN --cap-add=SYS_MODULE --dns=8.8.8.8 -p 8000:8000 example_service
```

