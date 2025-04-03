from fastapi import APIRouter

from services.heartbeat_service import register_heartbeat

router = APIRouter()

@router.get("/heartbeat/{container_id}")
def receive_heartbeat(container_id: str) -> str:
    print(container_id)
    register_heartbeat(container_id)
    return "DONE"