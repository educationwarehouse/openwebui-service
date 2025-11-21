from pathlib import Path
import invoke.exceptions
from edwh import tasks, task  # Use edwh.task to avoid warning
from invoke import Context

# REQUIRED: ensure a .env file exists
if not Path(".env").exists():
    with open(Path(".env"), "x") as env_file:
        env_file.close()

context = Context()
check_env = tasks.check_env
generate_password = tasks.generate_password


@task
def setup(c):
    """Set up environment variables in ./.env file."""
    # Ensure required directories exist
    Path("home/ollama").mkdir(parents=True, exist_ok=True)
    Path("data").mkdir(parents=True, exist_ok=True)
    
    check_env(
        "NAME_SERVICE",
        default="openwebui",
        comment="Name of the service",
    )
    check_env(
        "HOSTINGDOMAIN",
        default="localhost",
        comment="Hosting domain",
    )
    check_env(
        "WEBUI_DOCKER_TAG",
        default="ollama",
        comment="Docker tag for the web UI",
    )
    check_env(
        "OPENROUTER_API_BASE_URL",
        default="https://openrouter.ai/api/v1",
        comment="OpenRouter API base URL",
    )
    check_env(
        "WEBUI_SECRET_KEY",
        default=generate_password(context, 32),
        comment="Secret key for Open WebUI (auto-generated)",
    )

    enable_tunnellm = check_env(
        "TUNNEL_ENABLE",
        default="1",
        comment="Enable TunnelLM?"
    ) == "1"

    if enable_tunnellm:
        check_env(
            "TUNNEL_ENDPOINT",
            default="http://openwebui:8080/api",
            comment="Defaults to local openwebui"
        )

        check_env(
            "TUNNEL_API_KEY",
            default="",
            comment="Settings > Account > API Keys > API Key"
        )

        check_env(
            "TUNNEL_PORT",
            default="11435",
            comment="Defaults to 1 higher than Ollama default"
        )