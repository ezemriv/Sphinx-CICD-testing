# Sphinx-CICD-testing

[See Deployed Documentation in Github Pages](https://ezemriv.github.io/Sphinx-CICD-testing/)

Note: Project initiated with `uv init --lib`

---

## 📚 Local Setup with Sphinx

This project uses **Sphinx** + **uv** for building and serving documentation.

### 🔧 1. Install Docs Dependencies

Use [uv](https://github.com/astral-sh/uv) to sync the `docs` extra from `pyproject.toml`:

```bash
uv sync --extra docs
```

Your `pyproject.toml` should include:

```toml
[project.optional-dependencies]
docs = [
  "sphinx>=7",
  "sphinx-rtd-theme",
  "sphinx-autodoc-typehints",
  "sphinx-copybutton",
  "sphinx-autobuild"
]
```

---

### 🏗️ 2. Create the `docs/` Folder (if starting fresh)

If this is a new project:

```bash
mkdir docs
cd docs
uv run sphinx-quickstart -p sphinxcicdtesting -a ER -v 0.1 -r 0.1 -l en --sep --ext-autodoc --makefile
```

Then manually create:

* `docs/source/getting-started.rst`
* `docs/source/api/modules.rst`

---

### ⚙️ 3. Minimal `conf.py` Configuration

Located at `docs/source/conf.py`:

```python
import os, sys, importlib.metadata as md
sys.path.insert(0, os.path.abspath('../../src'))

project = 'your_project_name'
author = 'Your Name'
release = md.version("your_project_name")  # requires project to be installable

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints"
]

autosummary_generate = True
autodoc_default_options = {
    "members": True,
    "undoc-members": False,
}

html_theme = "sphinx_rtd_theme"
```

---

### 🧱 4. Minimal Structure for Pages

#### `index.rst`

```rst
your_project_name documentation
===============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting-started
   api/modules
```

#### `getting-started.rst`

```rst
Getting Started
===============

Install:

.. code-block:: bash

   pip install your_project_name

Usage:

.. code-block:: python

   from your_project_name import something
```

#### `api/modules.rst`

```rst
API Reference
=============

.. autosummary::
   :toctree: _generated
   :recursive:

   your_project_name
```

---

### 🚀 5. Build Docs Locally

```bash
uv run sphinx-build -b html docs/source docs/_build/html
```

Open `docs/_build/html/index.html` in your browser to view the output.

---

### 🔁 6. Live Preview with Auto-Reload

```bash
uv run sphinx-autobuild docs/source docs/_build/html --open-browser --port 8000
```

---

## 🚀 Deploying Documentation via GitHub Actions

This project auto-builds and deploys Sphinx docs to **GitHub Pages** on every push to `main`.

---

### ✅ 1. Required GitHub Setup

#### 🔒 Enable GitHub Pages

1. Go to your repo’s **Settings → Pages**
2. Under **Build and deployment**, set:

   * **Source**: `GitHub Actions`

3. Click **Save** even if it looks correct.

---

### 🛠️ 2. GitHub Actions Workflow

Save this file as `.github/workflows/docs.yml`:

```yaml
name: Publish Sphinx Docs

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write     # allow Pages deployment
  id-token: write  # allow OIDC token for deploy

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: ./.github/actions/setup         # installs Python + uv
      - run: uv sync --locked --extra docs    # install doc deps
      - run: |
          uv run sphinx-build -b html docs/source docs/_build/html
      - uses: actions/upload-pages-artifact@v3 # upload built HTML to Pages Artifact
        with:
          path: docs/_build/html

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4 # deploy to GitHub Pages
```

---

### 📘 3. After Your First Push

* A deployment will trigger automatically.
* The documentation will be available at:

  ```
  https://<your-username>.github.io/<your-repo>/
  ```

You’ll also see the live URL under **Settings → Pages** after the first deployment.
