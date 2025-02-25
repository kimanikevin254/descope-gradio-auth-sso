from fastapi import Request, HTTPException, status
from authlib.integrations.starlette_client import OAuth, OAuthError
from typing import Optional

class Auth:
    def __init__(self):
        self.oauth = OAuth()
        self.settings = None

    # Initialize the OAuth client with settings
    def init_oauth(self, settings):
        self.settings = settings
        self.oauth.register(
            name=self.settings.OAUTH_CLIENT_NAME,
            client_id=self.settings.OAUTH_CLIENT_ID,
            client_secret=self.settings.OAUTH_CLIENT_SECRET,
            authorize_url=self.settings.OAUTH_AUTHORIZE_URL,
            access_token_url=self.settings.OAUTH_ACCESS_TOKEN_URL,
            redirect_uri=self.settings.OAUTH_REDIRECT_URI,
            jwks_uri=self.settings.OAUTH_JWKS_URI,
            userinfo_endpoint=self.settings.OAUTH_USERINFO_ENDPOINT,
            client_kwargs={'scope': self.settings.OAUTH_SCOPES},
        )

    # Redirect to authorization endpoint
    async def authorize_redirect(self, request: Request, redirect_uri: str):
        return await getattr(self.oauth, self.settings.OAUTH_CLIENT_NAME).authorize_redirect(request, redirect_uri)

    # Exchange authorization code for access token    
    async def authorize_access_token(self, request: Request):
        try:
            return await getattr(self.oauth, self.settings.OAUTH_CLIENT_NAME).authorize_access_token(request)
        except OAuthError as error:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"OAuth error: {error.error}"
            )
    
    # Get the current authenticated user name
    def get_current_user(self, request: Request) -> Optional[str]:
        user = request.session.get("user")
        if user:
            return user['email']
        return None
    
    # Authenticate user and authorize based on path and roles
    # To protect Gradio app routes
    def authenticate_and_authorize(self, request: Request) -> Optional[str]:
        path = request.url.path
        user = request.session.get("user", {})
        tenants = user.get('tenants', [])
        roles = set()

        for data in tenants.values():
            roles.update(data.get('roles', []))

        # Avoid blocking the gradio queue requests
        if '/gradio_api/queue' in path and user:
            return user['email']

        if user and self.settings.ADMIN_ROLE in roles and path == self.settings.ADMIN_DASHBOARD_PATH:
            print('pass. returning', user['email'])
            return user['email']
        elif user and path == self.settings.USER_DASHBOARD_PATH:
            return user['email']
        else:
            return None
        
    # Determine the Gradio app to show the user based on their roles
    def get_user_redirect_path(self, request: Request) -> str:
        user = request.session.get("user", {})
        tenants = user.get('tenants', [])
        roles = set()

        for data in tenants.values():
            roles.update(data.get('roles', []))
        
        if not user:
            return self.settings.LOGIN_PAGE_PATH
        
        if self.settings.ADMIN_ROLE in roles:
            return self.settings.ADMIN_DASHBOARD_PATH
        else:
            return self.settings.USER_DASHBOARD_PATH
        
    # Log out the user
    def logout(self, request: Request) -> None:
        request.session.pop("user", None)

auth = Auth()