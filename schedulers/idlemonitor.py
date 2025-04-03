import logging
from apscheduler.schedulers.background import BackgroundScheduler
from repositories.containerinforepo import get_records_gt_hour

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()


def checkIdleContainers():
    logging.info("fetching containers for termination")
    target_containers = get_records_gt_hour()
    logging.info("found %d containers, available for termination", len(target_containers))
    for container in target_containers:
        print(container.container_id)

scheduler.add_job(checkIdleContainers, "interval", minutes = 15)