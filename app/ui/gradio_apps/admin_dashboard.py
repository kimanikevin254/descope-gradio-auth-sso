import gradio as gr

def load_user_dashboard(request: gr.Request):
    user = request.request.session.get('user', {})
    if not user:
        return "Hello, Guest! 👋. Once you set up auth, you will be able to view your details here.", "", gr.update(visible=False)
    
    tenants = user.get('tenants', [])
    roles = set()

    if isinstance(tenants, dict):
        for data in tenants.values():
            roles.update(data.get('roles', []))
        
    welcome_msg = f"Hello, {user.get('name', 'User')}! 👋"
    profile_info = f"### Here is your profile info:\n- **Email:** {user.get('email', 'N/A')}\n- **Roles:** {', '.join(roles)}"
    
    return welcome_msg, profile_info, gr.update(visible=True)

with gr.Blocks() as main: 
    gr.Markdown("# Admin Dashboard")
    welcome_message = gr.Markdown()
    profile_details = gr.Markdown(visible=False)  # Initially hidden
    
    # Added visibility control
    main.load(fn=load_user_dashboard, 
                  outputs=[welcome_message, profile_details, profile_details])
    
    logout_button = gr.Button("Logout", link="/auth/logout")

if __name__ == "__main__":
    main.launch()