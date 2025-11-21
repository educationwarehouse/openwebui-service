# OpenWebUI Service

OpenWebUI (Ollama edition) deployment.

EDWH tooling compliant - use `edwh setup; edwh restic.configure -c local` to also include a local backup. See
`ew help restic.configure` for other destinations

## TunnelLM

**TunnelLM** is a lightweight proxy container that exposes your local OpenWebUI endpoint (or any other OpenAI compatible
API endpoint such as OpenRouter) on a different port (default: 11435 to prevent conflicts with e.g. ollama at 11434) 
**without authentication**.  
This is useful when your tooling (e.g. JetBrains AI Assistant) speaks the OpenAI REST API but cannot send an
`Authorization` header.

### Getting started

1. Start Open WebUI:

```shell script
edwh up -s openwebui
```

2. In the Web UI → **Settings → Account → API Keys**, create a key for the same user account you’ll use with
   the proxy.
3. Configure the proxy either through `edwh setup` or by manually changing the `.env` file:

```dotenv
TUNNEL_API_KEY=<paste-your-openwebui-api-key>
TUNNEL_PORT=11435        # host-side port – keep internal if you don’t need external access
TUNNEL_VERBOSITY=0       # 0 (silent) or 1 (logs each request)
```

4. Point your client at `http://hostname-within-tailscale:11435/v1`.  
   *We strongly suggest running Tailscale on each device*: this lets your client machine reach the
   proxy over an encrypted tunnel **without** opening any ports on your firewall.  
   Disable the port on all external interfaces first:

```shell script
sudo ufw deny 11435
```

> **Security reminder:** The proxy intentionally removes the need for an API key. Never expose port 11435 beyond your
> trusted network or Tailscale overlay—keep your firewall rules strict.