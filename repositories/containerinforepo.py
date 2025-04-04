import pytz
from datetime import timedelta, datetime

from database import get_db
from models.containerinfo import ContainerInfo

db = get_db()

def createContainerInfo(container_info: ContainerInfo):
    try:
        db.add(container_info)
        db.commit()
        db.refresh(container_info)
        return True
    except Exception as e:
        return False


def update_heartbeat(container_id: str) -> bool:
    """Finds a container by ID and updates its last_heartbeat to current UTC time."""
    utc_now = datetime.now(pytz.UTC)

    container = db.query(ContainerInfo).filter(ContainerInfo.container_id == container_id).first()

    if container:
        container.last_heartbeat = utc_now
        db.commit()
        db.refresh(container)
        return True

    return False

def get_records_gt_hour() -> list[ContainerInfo]:
    time_threshold = datetime.now(pytz.UTC) - timedelta(minutes=60)

    return (
        db.query(ContainerInfo)
        .filter(ContainerInfo.last_heartbeat < time_threshold)
        .filter(ContainerInfo.container_alive == True)
        .all()
    )

def update_on_termination(container_id: str) -> ContainerInfo:
    try:
        container: ContainerInfo = db.query(ContainerInfo).filter(ContainerInfo.container_id == container_id).first()
        if container:
            container.container_alive = False
            db.commit()
            db.refresh(container)
            return container
    except Exception as e:
        return None