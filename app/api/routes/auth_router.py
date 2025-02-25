from fastapi import APIRouter, Request, HTTPException
from starlette.responses import RedirectResponse
from starlette.status import HTTP_302_FOUND

from app.core.auth import auth

router = APIRouter()