from repositories.containerinforepo import update_heartbeat


def register_heartbeat(container_id: str):
    update_heartbeat(container_id)