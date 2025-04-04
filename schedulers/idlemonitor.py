import logging
from apscheduler.schedulers.background import BackgroundScheduler
from docker.errors import APIError, NotFound

from repositories.containerinforepo import get_records_gt_hour, update_on_termination
import docker

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()

def terminate_docker_container(container_id: str):
    client = docker.from_env()

    try:
        container = client.containers.get(container_id)
        container.kill()
        container.remove()
        update_on_termination(container_id)
        logger.info("killed and removed container %s", container_id)

    except NotFound:
        logger.error("Container %s not found", container_id)
    except APIError as e:
        logger.error("Docker API error %s", e.explanation)
    except Exception as e:
        logger.error("Unexpected error: ", e)


def checkIdleContainers():
    logging.info("fetching containers for termination")
    target_containers = get_records_gt_hour()
    logging.info("found %d containers, available for termination", len(target_containers))
    for container in target_containers:
        terminate_docker_container(container.container_id)

scheduler.add_job(checkIdleContainers, "interval", minutes = 15)