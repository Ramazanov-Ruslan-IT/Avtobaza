

# Курсовая работа: Backend автобазы на FastAPI - Python

Данный репозиторий является базой архитектуры боевого проекта Автобазы.



### Полезные ссылки
- [Описание архитектуры сервиса](https://gitverse.ru/Ramazanov/Basic-microservices-platform)
- [Запуск сервиса локально](#команды-для-запуска-сервиса-локально)
- [Запуск в Docker](#команды-для-запуска-сервиса-на-базе-docker)


## Описание файловой структуры проекта

<details>
<summary>Файловое дерево</summary>

```shell
|   .dockerignore
|   .env
|   .env.example
|   .gitignore
|   Dockerfile
|   pyproject.toml
|   pyproject.toml~
|   README.md
|   README.md~
|   requirements.txt
|           
\---v1
    |   __init__.py
    |   
    +---src
    |   |   config.py
    |   |   config.py~
    |   |   main.py
    |   |   
    |   +---api
    |   |   |   __init__.py
    |   |   |   
    |   |   +---grpc
    |   |   +---kafka
    |   |   \---rest
    |   |       |   api_route_factory.py
    |   |       |   lifespan.py
    |   |       |   __init__.py
    |   |       |   
    |   |       +---exceptions
    |   |       |   |   app_exceptions.py
    |   |       |   |   raisers.py
    |   |       |   |   __init__.py
    |   |       |   |   
    |   |       |   \---schemas
    |   |       |           errors.py
    |   |       |           responses.py
    |   |       |           __init__.py
    |   |       |           
    |   |       +---middlewares
    |   |       |       cors.py
    |   |       |       process_time.py
    |   |       |       register.py
    |   |       |       security_headers.py
    |   |       |       __init__.py
    |   |       |       
    |   |       \---routers
    |   |           |   base_router.py
    |   |           |   base_router.py~
    |   |           |   
    |   |           +---access_log
    |   |           |       dependencies.py
    |   |           |       dependencies.py~
    |   |           |       router.py
    |   |           |       router.py~
    |   |           |       schemas.py
    |   |           |       schemas.py~
    |   |           |       
    |   |           +---audit_log
    |   |           |       dependencies.py
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       
    |   |           +---autobase
    |   |           |       dependencies.py
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       schemas.py~
    |   |           |       
    |   |           +---document
    |   |           |       dependencies.py
    |   |           |       dependencies.py~
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       
    |   |           +---efficiency_metric
    |   |           |       dependencies.py
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       
    |   |           +---financial_transaction
    |   |           |       dependencies.py
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       schemas.py~
    |   |           |       
    |   |           +---fuel_type
    |   |           |       dependencies.py
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       
    |   |           +---gas_station
    |   |           |       dependencies.py
    |   |           |       dependencies.py~
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       
    |   |           +---gas_station_contract
    |   |           |       dependencies.py
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       schemas.py~
    |   |           |       
    |   |           +---gas_station_fuel
    |   |           |       dependencies.py
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       
    |   |           +---gps_track
    |   |           |       dependencies.py
    |   |           |       dependencies.py~
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       schemas.py~
    |   |           |       
    |   |           +---maintenance_log
    |   |           |       dependencies.py
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       
    |   |           +---ml_suggestion
    |   |           |       dependencies.py
    |   |           |       dependencies.py~
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       
    |   |           +---part_inventory
    |   |           |       dependencies.py
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       
    |   |           +---refueling_log
    |   |           |       dependencies.py
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       
    |   |           +---repair_request
    |   |           |       dependencies.py
    |   |           |       router.py
    |   |           |       router.py~
    |   |           |       schemas.py
    |   |           |       
    |   |           +---report
    |   |           |       dependencies.py
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       
    |   |           +---role
    |   |           |       dependencies.py
    |   |           |       dependencies.py~
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       schemas.py~
    |   |           |       
    |   |           +---route
    |   |           |       dependencies.py
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       schemas.py~
    |   |           |       
    |   |           +---schedule
    |   |           |       dependencies.py
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       
    |   |           +---scheduled_task
    |   |           |       dependencies.py
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       
    |   |           +---storage_fuel
    |   |           |       dependencies.py
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       
    |   |           +---supplier
    |   |           |       dependencies.py
    |   |           |       dependencies.py~
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       
    |   |           +---system_event
    |   |           |       dependencies.py
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       
    |   |           +---user
    |   |           |       dependencies.py
    |   |           |       dependencies.py~
    |   |           |       router.py
    |   |           |       schemas.py
    |   |           |       
    |   |           \---vehicle
    |   |                   dependencies.py
    |   |                   router.py
    |   |                   router.py~
    |   |                   schemas.py
    |   |                   schemas.py~
    |   |                   
    |   +---app
    |   |   +---dto
    |   |   |       access_log.py
    |   |   |       audit_log.py
    |   |   |       audit_log.py~
    |   |   |       autobase.py
    |   |   |       autobase.py~
    |   |   |       base.py
    |   |   |       document.py
    |   |   |       document.py~
    |   |   |       efficiency_metric.py
    |   |   |       financial_transaction.py
    |   |   |       financial_transaction.py~
    |   |   |       fuel_type.py
    |   |   |       fuel_type.py~
    |   |   |       gas_station.py
    |   |   |       gas_station.py~
    |   |   |       gas_station_contract.py
    |   |   |       gas_station_contract_orm.py~
    |   |   |       gas_station_fuel.py
    |   |   |       gas_station_fuel_orm.py~
    |   |   |       gps_track.py
    |   |   |       gps_track.py~
    |   |   |       maintenance_log.py
    |   |   |       ml_suggestion.py
    |   |   |       ml_suggestion.py~
    |   |   |       part_inventory.py
    |   |   |       refueling_log.py
    |   |   |       repair_request.py
    |   |   |       repair_request.py~
    |   |   |       report.py
    |   |   |       report.py~
    |   |   |       role.py
    |   |   |       route.py
    |   |   |       route.py~
    |   |   |       schedule.py
    |   |   |       schedule.py~
    |   |   |       scheduled_task.py
    |   |   |       scheduled_task.py~
    |   |   |       storage_fuel.py
    |   |   |       supplier.py
    |   |   |       system_event.py
    |   |   |       user.py
    |   |   |       user.py~
    |   |   |       vehicle.py
    |   |   |       vehicle.py~
    |   |   |       __init__.py
    |   |   |       __init__.py~
    |   |   |       
    |   |   +---services
    |   |   |   +---access_log
    |   |   |   |       abs_service.py
    |   |   |   |       dependencies.py
    |   |   |   |       service.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---audit_log
    |   |   |   |       abs_service.py
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       service.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---autobase
    |   |   |   |       abs_service.py
    |   |   |   |       dependencies.py
    |   |   |   |       service.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---document
    |   |   |   |       abs_service.py
    |   |   |   |       dependencies.py
    |   |   |   |       service.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---efficiency_metric
    |   |   |   |       abs_service.py
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       service.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---financial_transaction
    |   |   |   |       abs_service.py
    |   |   |   |       dependencies.py
    |   |   |   |       service.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---fuel_type
    |   |   |   |       abs_service.py
    |   |   |   |       dependencies.py
    |   |   |   |       service.py
    |   |   |   |       service.py~
    |   |   |   |       __init__.py
    |   |   |   |       __init__.py~
    |   |   |   |       
    |   |   |   +---gas_station
    |   |   |   |       abs_service.py
    |   |   |   |       dependencies.py
    |   |   |   |       service.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---gas_station_contract
    |   |   |   |       abs_service.py
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       service.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---gas_station_fuel
    |   |   |   |       abs_service.py
    |   |   |   |       dependencies.py
    |   |   |   |       service.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---gps_track
    |   |   |   |       abs_service.py
    |   |   |   |       dependencies.py
    |   |   |   |       service.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---maintenance_log
    |   |   |   |       abs_service.py
    |   |   |   |       abs_service.py~
    |   |   |   |       dependencies.py
    |   |   |   |       service.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---ml_suggestion
    |   |   |   |       abs_service.py
    |   |   |   |       dependencies.py
    |   |   |   |       service.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---part_inventory
    |   |   |   |       abs_service.py
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       service.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---refueling_log
    |   |   |   |       abs_service.py
    |   |   |   |       abs_service.py~
    |   |   |   |       dependencies.py
    |   |   |   |       service.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---repair_request
    |   |   |   |       abs_service.py
    |   |   |   |       dependencies.py
    |   |   |   |       service.py
    |   |   |   |       service.py~
    |   |   |   |       __init__.py
    |   |   |   |       __init__.py~
    |   |   |   |       
    |   |   |   +---report
    |   |   |   |       abs_service.py
    |   |   |   |       abs_service.py~
    |   |   |   |       dependencies.py
    |   |   |   |       service.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---role
    |   |   |   |       abs_service.py
    |   |   |   |       abs_service.py~
    |   |   |   |       dependencies.py
    |   |   |   |       service.py
    |   |   |   |       __init__.py
    |   |   |   |       __init__.py~
    |   |   |   |       
    |   |   |   +---route
    |   |   |   |       abs_service.py
    |   |   |   |       dependencies.py
    |   |   |   |       service.py
    |   |   |   |       __init__.py
    |   |   |   |       __init__.py~
    |   |   |   |       
    |   |   |   +---schedule
    |   |   |   |       abs_service.py
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       service.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---scheduled_task
    |   |   |   |       abs_service.py
    |   |   |   |       dependencies.py
    |   |   |   |       service.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---storage_fuel
    |   |   |   |       abs_service.py
    |   |   |   |       abs_service.py~
    |   |   |   |       dependencies.py
    |   |   |   |       service.py
    |   |   |   |       __init__.py
    |   |   |   |       __init__.py~
    |   |   |   |       
    |   |   |   +---supplier
    |   |   |   |       abs_service.py
    |   |   |   |       dependencies.py
    |   |   |   |       service.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---system_event
    |   |   |   |       abs_service.py
    |   |   |   |       abs_service.py~
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       service.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---user
    |   |   |   |       abs_service.py
    |   |   |   |       abs_service.py~
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       service.py
    |   |   |   |       service.py~
    |   |   |   |       __init__.py
    |   |   |   |       __init__.py~
    |   |   |   |       
    |   |   |   \---vehicle
    |   |   |           abs_service.py
    |   |   |           abs_service.py~
    |   |   |           dependencies.py
    |   |   |           service.py
    |   |   |           service.py~
    |   |   |           __init__.py
    |   |   |           
    |   |   +---solutions
    |   |   |   \---example
    |   |   |           abs_solution.py
    |   |   |           dependencies.py
    |   |   |           solution.py
    |   |   |           __init__.py
    |   |   |           
    |   |   \---utils
    |   |           mapper.py
    |   |           
    |   +---db
    |   |   +---models
    |   |   |        ml_suggestion_orm.py~
    |   |   |       access_log_orm.py
    |   |   |       access_log_orm.py~
    |   |   |       audit_log_orm.py
    |   |   |       autobase_orm.py
    |   |   |       autobase_orm.py~
    |   |   |       base_orm.py
    |   |   |       document_orm.py
    |   |   |       document_orm.py~
    |   |   |       efficiency_metric_orm.py
    |   |   |       efficiency_metric_orm.py~
    |   |   |       financial_transaction_orm.py
    |   |   |       financial_transaction_orm.py~
    |   |   |       fuel_type_orm.py
    |   |   |       fuel_type_orm.py~
    |   |   |       gas_station_contract_orm.py
    |   |   |       gas_station_contract_orm.py~
    |   |   |       gas_station_fuel_orm.py
    |   |   |       gas_station_fuel_orm.py~
    |   |   |       gas_station_orm.py
    |   |   |       gas_station_orm.py~
    |   |   |       gps_track_orm.py
    |   |   |       gps_track_orm.py~
    |   |   |       maintenance_log_orm.py
    |   |   |       maintenance_log_orm.py~
    |   |   |       ml_suggestion_orm.py
    |   |   |       part_inventory_orm.py
    |   |   |       part_inventory_orm.py~
    |   |   |       refueling_log_orm.py
    |   |   |       refueling_log_orm.py~
    |   |   |       repair_request_orm.py
    |   |   |       repair_request_orm.py~
    |   |   |       report_orm.py
    |   |   |       report_orm.py~
    |   |   |       role_orm.py
    |   |   |       role_orm.py~
    |   |   |       route_orm.py
    |   |   |       route_orm.py~
    |   |   |       scheduled_task_orm.py
    |   |   |       scheduled_task_orm.py~
    |   |   |       schedule_orm.py
    |   |   |       schedule_orm.py~
    |   |   |       storage_fuel_orm.py
    |   |   |       storage_fuel_orm.py~
    |   |   |       supplier_orm.py
    |   |   |       supplier_orm.py~
    |   |   |       system_event_orm.py
    |   |   |       system_event_orm.py~
    |   |   |       user_orm.py
    |   |   |       user_orm.py~
    |   |   |       vehicle_orm.py
    |   |   |       vehicle_orm.py~
    |   |   |       __init__.py
    |   |   |       
    |   |   +---repositories
    |   |   |   |   __init__.py
    |   |   |   |   
    |   |   |   +---access_log
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       repo.py
    |   |   |   |       repo.py~
    |   |   |   |       __init__.py
    |   |   |   |       __init__.py~
    |   |   |   |       
    |   |   |   +---audit_log
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       repo.py
    |   |   |   |       repo.py~
    |   |   |   |       __init__.py
    |   |   |   |       __init__.py~
    |   |   |   |       
    |   |   |   +---autobase
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       repo.py
    |   |   |   |       repo.py~
    |   |   |   |       __init__.py
    |   |   |   |       __init__.py~
    |   |   |   |       
    |   |   |   +---document
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       repo.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---efficiency_metric
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       repo.py
    |   |   |   |       repo.py~
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---financial_transaction
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       repo.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---fuel_type
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       repo.py
    |   |   |   |       __init__.py
    |   |   |   |       __init__.py~
    |   |   |   |       
    |   |   |   +---gas_station
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       repo.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---gas_station_contract
    |   |   |   |       abs_repo.py
    |   |   |   |       dependencies.py
    |   |   |   |       repo.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---gas_station_fuel
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       repo.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---gps_track
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       repo.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---maintenance_log
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       repo.py
    |   |   |   |       __init__.py
    |   |   |   |       __init__.py~
    |   |   |   |       
    |   |   |   +---ml_suggestion
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       repo.py
    |   |   |   |       repo.py~
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---part_inventory
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       repo.py
    |   |   |   |       repo.py~
    |   |   |   |       __init__.py
    |   |   |   |       __init__.py~
    |   |   |   |       
    |   |   |   +---refueling_log
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       repo.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---repair_request
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       repo.py
    |   |   |   |       repo.py~
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---report
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       repo.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---role
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       repo.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---route
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       repo.py
    |   |   |   |       __init__.py
    |   |   |   |       __init__.py~
    |   |   |   |       
    |   |   |   +---schedule
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       repo.py
    |   |   |   |       __init__.py
    |   |   |   |       __init__.py~
    |   |   |   |       
    |   |   |   +---scheduled_task
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       repo.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---storage_fuel
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       repo.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---supplier
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       repo.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   +---system_event
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       repo.py
    |   |   |   |       __init__.py
    |   |   |   |       __init__.py~
    |   |   |   |       
    |   |   |   +---user
    |   |   |   |       abs_repo.py
    |   |   |   |       abs_repo.py~
    |   |   |   |       dependencies.py
    |   |   |   |       dependencies.py~
    |   |   |   |       repo.py
    |   |   |   |       __init__.py
    |   |   |   |       
    |   |   |   \---vehicle
    |   |   |           abs_repo.py
    |   |   |           abs_repo.py~
    |   |   |           dependencies.py
    |   |   |           dependencies.py~
    |   |   |           repo.py
    |   |   |           __init__.py
    |   |   |           
    |   |   \---settings
    |   |       \---connection
    |   |               postgresql.py
    |   |               redis.py
    |   |               __init__.py
    |   |               
    |   \---resources
    \---tests
            __init__.py
          
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

