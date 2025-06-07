from fastapi import APIRouter

from v1.src.api.rest.routers.access_log.router import router as access_log_router
from v1.src.api.rest.routers.audit_log.router import router as audit_log_router
from v1.src.api.rest.routers.autobase.router import router as autobase_router
from v1.src.api.rest.routers.document.router import router as document_router
from v1.src.api.rest.routers.efficiency_metric.router import router as efficiency_metric_router
from v1.src.api.rest.routers.fuel_type.router import router as fuel_type_router
from v1.src.api.rest.routers.gas_station.router import router as gas_station_router
from v1.src.api.rest.routers.gas_station_contract.router import router as gas_station_contract_router
from v1.src.api.rest.routers.gas_station_fuel.router import router as gas_station_fuel_router
from v1.src.api.rest.routers.gps_track.router import router as gps_track_router
from v1.src.api.rest.routers.maintenance_log.router import router as maintenance_log_router
from v1.src.api.rest.routers.ml_suggestion.router import router as ml_suggestion_router
from v1.src.api.rest.routers.part_inventory.router import router as part_inventory_router
from v1.src.api.rest.routers.refueling_log.router import router as refueling_log
from v1.src.api.rest.routers.repair_request.router import router as repair_request_router
from v1.src.api.rest.routers.report.router import router as report_router
from v1.src.api.rest.routers.role.router import router as role_router
from v1.src.api.rest.routers.route.router import router as route_router
from v1.src.api.rest.routers.schedule.router import router as schedule_router
from v1.src.api.rest.routers.scheduled_task.router import router as scheduled_task_router
from v1.src.api.rest.routers.storage_fuel.router import router as storage_fuel_router
from v1.src.api.rest.routers.supplier.router import router as supplier_router
from v1.src.api.rest.routers.system_event.router import router as system_event_router
from v1.src.api.rest.routers.user.router import router as user_router
from v1.src.api.rest.routers.vehicle.router import router as vehicle_router


from v1.src.api.rest.api_route_factory import api_get


base_router = APIRouter(prefix="/v1")


base_router.include_router(user_router)
base_router.include_router(role_router)
base_router.include_router(vehicle_router)
base_router.include_router(autobase_router)
base_router.include_router(document_router)
base_router.include_router(route_router)
base_router.include_router(repair_request_router)
base_router.include_router(report_router)
base_router.include_router(maintenance_log_router)
base_router.include_router(gas_station_router)
base_router.include_router(fuel_type_router)
base_router.include_router(gas_station_fuel_router)
base_router.include_router(gas_station_contract_router)
base_router.include_router(storage_fuel_router)
base_router.include_router(schedule_router)
base_router.include_router(part_inventory_router)
base_router.include_router(supplier_router)

base_router.include_router(gps_track_router)
base_router.include_router(efficiency_metric_router)
base_router.include_router(ml_suggestion_router)

base_router.include_router(scheduled_task_router)
base_router.include_router(system_event_router)

base_router.include_router(access_log_router)
base_router.include_router(audit_log_router)
base_router.include_router(refueling_log)


@api_get(base_router, "/", dict, summary="Базовый эндпоинт сервиса")
async def root():
    return {"message": "Welcome to the Autobase Service"}


@api_get(base_router, "/ping", dict, summary="Проверка доступности сервиса")
async def ping():
    return {"pong": True}
