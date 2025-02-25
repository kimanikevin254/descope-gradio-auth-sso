from fastapi import APIRouter, Request
from starlette.responses import RedirectResponse
from starlette.status import HTTP_302_FOUND

from app.core.auth import auth

router = APIRouter()

# Main entry point, redirects based on user role
@router.get("/")
def index(request: Request):
    return RedirectResponse(url='/gradio')