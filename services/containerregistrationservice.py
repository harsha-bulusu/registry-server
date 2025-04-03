from functools import lru_cache

from models.containerinfo import ContainerInfo
from models.containerregistration import ContainerRegistrationRequest
from repositories.containerinforepo import createContainerInfo

class ContainerRegistrationService:

    def register_container(self, container_registration_request: ContainerRegistrationRequest) -> bool:
        container_info = ContainerInfo()

        container_info.container_id = container_registration_request.container_id
        container_info.container_name = container_registration_request.container_name
        container_info.app_name = container_registration_request.app_name
        container_info.created_by = container_registration_request.created_by

        return createContainerInfo(container_info)

@lru_cache
def get_instance():
    return ContainerRegistrationService()