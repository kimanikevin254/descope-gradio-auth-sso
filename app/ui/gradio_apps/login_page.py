import gradio as gr

def show_login_message():
    return "# Welcome", "Please log in to access your dashboard"

with gr.Blocks() as main:
    title = gr.Markdown()
    message = gr.Markdown()
    login_button = gr.Button("Login", link="/auth/login")

    main.load(fn=show_login_message, outputs=[title, message])

if __name__ == "__main__":
    main.launch()
