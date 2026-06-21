# Horizon devcontainer

Reproducible dev environment so the toolchain "just works": Python **3.12** (matches CI), `uv`,
and the GitHub CLI (`gh`).

## What you get

- **Python 3.12** base image (`mcr.microsoft.com/devcontainers/python:1-3.12-bookworm`) — aligned
  with what CI/cron actually run (`requires-python = ">=3.11"`, runners use 3.12). Note the repo
  `Dockerfile` still pins 3.11; that drift is harmless but worth aligning later.
- **uv** installed by `postCreateCommand` (Astral installer, version-pinned for reproducibility),
  then `uv sync` to materialize the base environment from `uv.lock`.
- **`gh`** preinstalled via the `github-cli` devcontainer feature. In **GitHub Codespaces** it is
  **auto-authenticated** — no `gh auth login` step.

## Secrets

This repo reads secrets from the environment (via `python-dotenv`); nothing secret is committed.

**Local devcontainer / Docker:**

```bash
cp .env.example .env      # .env is gitignored
# edit .env and set OPENROUTER_API_KEY (and APIFY_TOKEN if you use Twitter mode)
```

**GitHub Codespaces:** set repository **Codespaces secrets** instead of a `.env` file — they are
injected as environment variables automatically:

- `OPENROUTER_API_KEY` (required)
- `APIFY_TOKEN` (only for Twitter/Apify scraping)

## Optional: Twitter / Playwright mode

The base `uv sync` installs core deps only. For the Twitter extra:

```bash
uv sync --extra twitter
uv run playwright install chromium
```
