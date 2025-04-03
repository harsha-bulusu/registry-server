import logging
from fastapi import FastAPI
from controllers import heartbeat_controller, registration_controller
from database import close_db
from middleware import CorrelationIdMiddleware
from schedulers import idlemonitor
from contextlib import asynccontextmanager

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("app started")
    yield
    scheduler.shutdown()
    close_db()

app = FastAPI(lifespan = lifespan)

app.include_router(heartbeat_controller.router)
app.include_router(registration_controller.router)
app.add_middleware(CorrelationIdMiddleware)
scheduler = idlemonitor.scheduler

scheduler.start()