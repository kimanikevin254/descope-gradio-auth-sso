from fastapi import APIRouter, Request
from starlette.responses import RedirectResponse
from starlette.status import HTTP_302_FOUND

from app.core.auth import auth

router = APIRouter()

# Main entry point, redirects based on user role
@router.get("/")
def index(request: Request):
    user = auth.get_current_user(request)
    if user:
        redirect_path = auth.get_user_redirect_path(request)
        return RedirectResponse(url=redirect_path, status_code=HTTP_302_FOUND)
    else:
        return RedirectResponse(url=auth.settings.LOGIN_PAGE_PATH, status_code=HTTP_302_FOUND)

# Routing endpoint for Gradio dashboards
@router.get("/gradio")
async def route_dashboard(request: Request):
    redirect_path = auth.get_user_redirect_path(request)
    return RedirectResponse(url=redirect_path, status_code=HTTP_302_FOUND)