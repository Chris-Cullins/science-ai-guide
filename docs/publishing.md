# Publishing as a GitHub Page

This repo is set up to publish an MkDocs site (nice theme, sidebar navigation, built-in search).

## Option A: GitHub Actions (recommended)

This repo includes a workflow that builds MkDocs and deploys to the `gh-pages` branch:

- `.github/workflows/deploy-mkdocs.yml`

Steps:

1. Push to a GitHub repo.
2. Ensure your default branch is `main`.
3. In GitHub: Settings -> Pages.
4. Set Source to "Deploy from a branch".
5. Select branch `gh-pages` and folder `/ (root)`.

Every push to `main` will rebuild and redeploy.

## Option B: Plain Markdown from /docs (simpler, fewer features)

If you do not want a build step, GitHub Pages can render Markdown directly from `/docs`, but you lose nice navigation/search.

Steps:

1. In GitHub: Settings -> Pages.
2. Set Source to "Deploy from a branch".
3. Choose your default branch and select the `/docs` folder.
