from sqlalchemy import Column, String, DateTime, func, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import pytz

Base = declarative_base()

def utc_now():
    return datetime.now(pytz.UTC)

class ContainerInfo(Base):
    __tablename__ = "container_info"

    container_id = Column(String, primary_key=True)
    container_name = Column(String, nullable=False, unique=True)
    created_by = Column(String, nullable=False, unique=True)
    app_name = Column(String, nullable=False, unique=True)
    container_alive = Column(Boolean, default=True, nullable=False)

    last_heartbeat = Column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)
    created_at = Column(DateTime(timezone=True), default=utc_now)
    updated_at = Column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)
