from fastapi import APIRouter, Request, HTTPException
from starlette.responses import RedirectResponse
from starlette.status import HTTP_302_FOUND

from app.core.auth import auth

router = APIRouter()

# Redirect to OAuth login provider
@router.get('/login')
async def login(request: Request):
    redirect_uri = request.url_for('auth_callback')
    return await auth.authorize_redirect(request, redirect_uri)

# Handle OAuth callback after successful login
@router.get("/auth/callback", name="auth_callback")
async def auth_callback(request: Request):
    try:
        token = await auth.authorize_access_token(request)
        user = token.get("userinfo")
        request.session["user"] = dict(user)
        return RedirectResponse(url="/", status_code=HTTP_302_FOUND)
    except HTTPException as e:
        # Log the error
        print(f"Authentication error: {e.detail}")
        return RedirectResponse(url="/auth/error", status_code=HTTP_302_FOUND)

# Log out the current user    
@router.get('/logout')
async def logout(request: Request):
    auth.logout(request)
    return RedirectResponse(url="/", status_code=HTTP_302_FOUND)

# Authentication error page
@router.get("/error")
async def auth_error():
    return {"error": "Authentication failed. Please try again."}