from pydantic import BaseModel


class ContainerRegistrationRequest(BaseModel):
    container_id: str
    container_name: str
    created_by: str
    app_name: str

class ContainerRegistrationResponse(BaseModel):
    status: bool