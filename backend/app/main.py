from fastapi import FastAPI
import logging

from app.core.logging import setup_logging
from app.exceptions.custom import AppException
from app.exceptions.handlers import app_exception_handler
from app.api.v1.api import api_router
from app.core.config import settings

# Initialize logging FIRST
setup_logging()

logger = logging.getLogger(__name__)

logger.info("Backend server started successfully.")

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)

app.include_router(api_router, prefix=settings.API_V1_PREFIX)

app.add_exception_handler(
    AppException,
    app_exception_handler,
)