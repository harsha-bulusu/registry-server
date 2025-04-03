import uuid
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

class CorrelationIdMiddleware(BaseHTTPMiddleware):
    """Middleware to ensure every request has a Correlation-Id"""

    async def dispatch(self, request: Request, call_next):
        correlation_id = request.headers.get("Correlation-Id")

        if not correlation_id:  # If not provided, generate a new one
            correlation_id = str(uuid.uuid4())

        response: Response = await call_next(request)
        response.headers["Correlation-Id"] = correlation_id  # Include in response headers
        request.state.correlation_id = correlation_id  # Store in request state for later use
        return response
