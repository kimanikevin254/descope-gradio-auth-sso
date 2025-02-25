import gradio as gr
from fastapi import FastAPI

from app.core.auth import Auth
from app.ui.gradio_apps import user_dashboard, admin_dashboard, login_page
from app.core.config import Settings

class GradioMounter:
    def __init__(self, app: FastAPI, auth: Auth, settings: Settings):
        self.app = app
        self.auth = auth
        self.settings = settings

    # Mount the login demo page
    def mount_login_page(self):
        with gr.Blocks() as login_page_wrapper:
            login_page.main.render()
        
        self.app = gr.mount_gradio_app(
            self.app, 
            login_page_wrapper, 
            path=self.settings.LOGIN_PAGE_PATH
        )

    # Mount the admin dashboard with authorization    
    def mount_admin_dashboard(self):
        with gr.Blocks() as admin_dashboard_wrapper:
            admin_dashboard.main.render()
        
        self.app = gr.mount_gradio_app(
            self.app, 
            admin_dashboard_wrapper, 
            path=self.settings.ADMIN_DASHBOARD_PATH,
        )

    # Mount the user dashboard with authorization 
    def mount_user_dashboard(self):
        with gr.Blocks() as user_dashboard_wrapper:
            user_dashboard.main.render()
        
        self.app = gr.mount_gradio_app(
            self.app, 
            user_dashboard_wrapper, 
            path=self.settings.USER_DASHBOARD_PATH,
        )

    # Mount all Gradio apps
    def mount_all_apps(self):
        self.mount_login_page()
        self.mount_admin_dashboard()
        self.mount_user_dashboard()