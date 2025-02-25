from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from app.core.config import settings
from app.api.routes import auth_router, dashboard_router
from app.core.auth import auth
from app.ui.gradio_mount import GradioMounter

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
)

# Configure middleware
app.add_middleware(
    SessionMiddleware,
    secret_key=settings.SESSION_SECRET_KEY,
    max_age=settings.SESSION_MAX_AGE,
)

# Initialize auth backend
auth.init_oauth(settings)

# Include API routers
app.include_router(auth_router.router, prefix="/auth")
app.include_router(dashboard_router.router, prefix="")

# Mount gradio apps
gradio_mounter = GradioMounter(app, auth, settings)
gradio_mounter.mount_all_apps()