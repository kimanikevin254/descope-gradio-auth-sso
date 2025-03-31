# Add Authentication and SSO to Your Gradio App

This repository is part of an article that aims to guide readers through the process of integrating Descope authentication (specifically, email magic links and OIDC-based SSO) into a Gradio application. It is tailored to assist developers who are either building new apps on Gradio or looking to add authentication and SSO to existing Gradio apps.

## Getting Started

To run this code on your local machine:

1. Follow along with the article to set up Descope, Okta, and obtain the necessary credentials.

2. Clone the repo:

    ```bash
    git clone https://github.com/kimanikevin254/descope-gradio-auth-sso.git
    ```

3. Create and activate a virtual environment:

    ```bash
    cd descope-gradio-auth-sso

    python3 -m venv .venv

    source .venv/bin/activate
    ```

4. Install all the dependencies using the command below:

    ```bash
    pip install -r requirements.txt
    ```

5. Rename `.env.example` to `.env` and replace the placeholder values in `OAUTH_CLIENT_ID`, `OAUTH_CLIENT_SECRET`, and `OAUTH_JWKS_URI` with the approproate values.

6. Run the app using the command:

    ```bash
    fastapi dev app/main.py
    ```

7. Navigate to "http://localhost:8000" on your browser.
