import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import ValidationError

load_dotenv()

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='../.env', 
        env_ignore_empty=True
    )

    # Project Info
    PROJECT_NAME: str = 'Descope-Gradio OAuth and SSO'
    DESCRIPTION: str = 'Demonstrating how to integrate Descope authentication (specifically, email magic links and OIDC-based SSO) into a Gradio application.'

    # Auth settings
    SESSION_SECRET_KEY: str
    SESSION_MAX_AGE: int = 3600 * 24  # 24 hours
    
    # OAuth settings(required fields)
    OAUTH_CLIENT_NAME: str
    OAUTH_CLIENT_ID: str
    OAUTH_CLIENT_SECRET: str
    OAUTH_AUTHORIZE_URL: str
    OAUTH_ACCESS_TOKEN_URL: str
    OAUTH_REDIRECT_URI: str
    OAUTH_JWKS_URI: str
    OAUTH_USERINFO_ENDPOINT: str
    OAUTH_SCOPES: str
    
    # App paths
    BASE_PATH: str = "/"
    GRADIO_BASE_PATH: str = "/gradio/"
    ADMIN_DASHBOARD_PATH: str = "/gradio/admin/"
    USER_DASHBOARD_PATH: str = "/gradio/user/"
    LOGIN_PAGE_PATH: str = "/auth/"
    
    # Role settings
    ADMIN_ROLE: str = "Tenant Admin"

try:
    settings = Settings()
except ValidationError as e:
    raise RuntimeError(f"Missing required environment variables: {e}")