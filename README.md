# Sphinx-CICD-testing


Initiated with `uv init --lib`

uv add sphinx --optional docs
uv run sphinx-quickstart docs

## Manual sphinx execution:
```bash
uv add sphinx --optional docs
uv run sphinx-quickstart docs
uv run sphinx-build -M html docs/source/ docs/build/
```

## Complex exec (chatgpt):

```bash
mkdir docs
cd docs
uv run sphinx-quickstart -p sphinxcicdtesting -a ER -v 0.1 -r 0.1 -l en --sep --ext-autodoc --makefile
```

- Inside `docs/conf.py`:

```python
import importlib.metadata as md, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
project  = "emrpy"
release  = md.version("emrpy")
html_theme = "furo"
```

Add any `.md` or `.rst` pages you like—`index.rst` is the entry point.

---

## 3 — Create a **docs.yml** workflow

```yaml
# .github/workflows/docs.yml
name: Build & Publish Docs

on:
  push:
    branches: [main]          # build on every push to main
  workflow_dispatch:          # manual trigger
  pull_request:               # verify docs build on PRs (no deploy)

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Re-use your composite action that installs uv + caching
      - uses: ./.github/actions/setup

      # Install doc dependencies
      - run: uv sync --extras docs --locked

      # Build HTML
      - run: sphinx-build -b html docs docs/_build/html

      # Upload the HTML artefact so the deploy job can pick it up
      - uses: actions/upload-pages-artifact@v3
        with:
          path: docs/_build/html

  # Only deploy from the default branch, never from PRs
  deploy-docs:
    needs: build-docs
    if: github.event_name != 'pull_request'
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    permissions:
      pages: write
      id-token: write
    steps:
      - id: deployment
        uses: actions/deploy-pages@v3
```

### Why two jobs?

* **build-docs** verifies that Sphinx can build on every PR (similar to tests).
* **deploy-docs** publishes only from `main`, giving you confidence that docs never break production.

---

## 4 — Where are the docs published?

With the new GitHub Pages infrastructure, the HTML ends up on

```
https://<org—or-user>.github.io/<repo>/
```

When the first deployment finishes, GitHub posts a link in the *Actions → deploy-docs* summary and in **Settings → Pages**. You can also set a custom domain there if you have one.

---

## 5 — Local preview (optional)

Developers can still preview docs locally:

```bash
uv sync --extras docs  # one-off
sphinx-autobuild docs docs/_build/html
# open http://127.0.0.1:8000
```

---

### Integration summary

* **No manual viewing required:** every push to `main` automatically publishes updated docs.
* **Full CI visibility:** PRs fail fast if Sphinx can’t build.
* **UV everywhere:** keeps lock-file fidelity and consistent environments.
* **GitHub Pages:** free hosting, zero extra services.

That’s it—you now have living documentation generated straight from the codebase and served automatically.
