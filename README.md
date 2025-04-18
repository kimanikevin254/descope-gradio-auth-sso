# Add Authentication and SSO to Your Gradio App

This repository is part of an article that aims to guide readers through the process of integrating Descope authentication (specifically, email magic links and OIDC-based SSO) into a Gradio application. It is tailored to assist developers who are either building new apps on Gradio or looking to add authentication and SSO to existing Gradio apps.

## Getting Started

To run this code on your local machine:

1. Follow along with the article to set up Descope, Okta, and obtain the necessary credentials.

   > If you're not following along with the article, this involves [configuring Okta as the OIDC SSO provider](https://docs.descope.com/sso/sso-configuration/setup-guides/okta#how-to-configure-oidc-sso), obtaining the Client ID (Project ID) from the [OIDC default application details page](https://app.descope.com/applications/descope-default-oidc), and obtaining a Client Secret (access key) from the [Access Keys](https://app.descope.com/accessKeys) page    

3. Clone the repo:

    ```bash
    git clone https://github.com/kimanikevin254/descope-gradio-auth-sso.git
    ```

4. Create and activate a virtual environment:

    ```bash
    cd descope-gradio-auth-sso

    python3 -m venv .venv

    source .venv/bin/activate
    ```

5. Install all the dependencies using the command below:

    ```bash
    pip install -r requirements.txt
    ```

6. Rename `.env.example` to `.env` and replace the placeholder values in `OAUTH_CLIENT_ID`, `OAUTH_CLIENT_SECRET`, and `OAUTH_JWKS_URI` with the approproate values.

7. Run the app using the command:

    ```bash
    fastapi dev app/main.py
    ```

8. Navigate to "http://localhost:8000" on your browser.
