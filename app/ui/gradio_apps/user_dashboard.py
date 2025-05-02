import gradio as gr

def load_user_dashboard(request: gr.Request):
    user = request.request.session.get('user')
    if not user:
        return "Hello, Guest! 👋. Once you set up auth, you will be able to view your details here.", "", gr.update(visible=False)  # Hide profile
    
    tenants = user.get('tenants', [])
    roles = set()

    if isinstance(tenants, dict):
        for data in tenants.values():
            roles.update(data.get('roles', []))
        
    roles_display = ', '.join(roles) if roles else "No roles assigned"
    welcome_msg = f"Hello, {user.get('name', 'User')}! 👋"
    profile_info = f"### Here is your profile info:\n- **Email:** {user.get('email', 'N/A')}\n- **Roles:** {roles_display}"
    
    return welcome_msg, profile_info, gr.update(visible=True)  # Show profile

with gr.Blocks() as main:
    gr.Markdown("# User Dashboard")
    welcome_message = gr.Markdown()
    profile_details = gr.Markdown(visible=False)  # Initially hidden
    
    main.load(fn=load_user_dashboard, 
                  outputs=[welcome_message, profile_details, profile_details])
    
    logout_button = gr.Button("Logout", link="/auth/logout")

if __name__ == "__main__":
    main.launch()