from fastapi import APIRouter, Depends

from models.containerregistration import ContainerRegistrationRequest,ContainerRegistrationResponse
from services.containerregistrationservice import ContainerRegistrationService, get_instance

router = APIRouter()

@router.post("/register-container")
def register_container(container_registration_request: ContainerRegistrationRequest,
                       container_registration_service: ContainerRegistrationService =  Depends(get_instance)) -> ContainerRegistrationResponse:
    res: bool = container_registration_service.register_container(container_registration_request)
    return ContainerRegistrationResponse(status = res)