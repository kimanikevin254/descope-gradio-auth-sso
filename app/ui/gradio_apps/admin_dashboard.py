import gradio as gr

def load_user_dashboard(request: gr.Request):
    user = request.request.session.get('user', {})
    roles = user.get('roles', [])
    
    welcome_msg = f"Hello, {user['name']}! 👋"
    profile_info = f"### Here is your profile info:\n- **Email:** {user['email']}\n- **Roles:** {', '.join(roles)}"
    
    return welcome_msg, profile_info

with gr.Blocks() as main:
    gr.Markdown("# Admin Dashboard")
    welcome_message = gr.Markdown()
    profile_details = gr.Markdown()
    logout_button = gr.Button("Logout", link="/auth/logout")

    main.load(fn=load_user_dashboard, outputs=[welcome_message, profile_details])

if __name__ == "__main__":
    main.launch()
