from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.custom import AppException


async def app_exception_handler(
    request: Request,
    exc: AppException,
):
    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "message": exc.message,
        },
    )