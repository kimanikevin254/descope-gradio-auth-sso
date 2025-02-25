from fastapi import Request, HTTPException, status
from authlib.integrations.starlette_client import OAuth, OAuthError
from typing import Optional

class Auth:
    def __init__(self):
        self.oauth = OAuth()
        self.settings = None

    
auth = Auth()