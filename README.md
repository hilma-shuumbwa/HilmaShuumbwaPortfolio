# Hilma Shuumbwa - Computer Programming I Portfolio Showcase

## Overview
This repository contains Hilma Shuumbwa's static portfolio showcase for Computer Programming I.

## Live Site
The GitHub Pages URL will use the student's GitHub username and repository name after deployment.

## Project
Project: SiteSpy

## Student Contribution
The contribution evidence focuses on Firebase-backed app support, data workflow review, configuration checks, and delivery documentation.

## Tech Stack
- Static HTML, CSS, and JavaScript
- GitHub Pages
- GitHub Actions
- Preserved source materials where applicable

## Static Deployment Architecture
GitHub Pages serves the static site in `site/`. The Flet/Python source is preserved where applicable, but it is not used as the live GitHub Pages runtime.

## Local Preview
```bash
python -m http.server 8000 --directory site
```

Open:

```text
http://localhost:8000
```

## Evidence Assets
- `src/services/firebaseConfig.js`
- `app.config.js`
- `.env.example`

The prepared evidence assets live in `site/assets/screenshots/`.

## Certificates
Certificate files, when available, live in `site/assets/certificates/` and are listed by `site/certificates.json`.

## Contribution Video Section
The static site includes an Individual Contribution Video section for the 1 minute 30 second showcase recording.

## GitHub Pages Deployment
GitHub Actions uploads the `site/` folder. Pages source must be GitHub Actions. Do not use branch/root deployment for Flet/Python.

## Maintenance Notes
- Keep private role documents out of Git.
- Keep tokens in local terminal environment variables only.
- Do not deploy the Flet/Python runtime to GitHub Pages.
