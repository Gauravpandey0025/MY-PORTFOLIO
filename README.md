# Portfolio Website — Publish Guide

This repository contains a static portfolio site (HTML/CSS). Below are quick steps to publish it publicly using GitHub Pages. You can also use Netlify/Vercel — instructions included.

## Option A — GitHub Pages (recommended)

1. Create a new GitHub repository (e.g. `portfolio`).
2. From your local project folder run:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo>.git
git push -u origin main
```

3. The repository already contains a GitHub Actions workflow that publishes the repository root to the `gh-pages` branch on every push to `main`. No extra secrets required.

4. After the first successful push, GitHub Pages will serve the site from the `gh-pages` branch. The URL will be:

```
https://<your-username>.github.io/<repo>/
```

5. If your EmailJS integration is used, update the placeholders in `index.html` with your EmailJS public key/service ID/template ID so contact form emails work.

## Option B — Netlify (drag & drop or via Git)

- Drag & drop the project folder in Netlify to publish quickly.
- Or connect the GitHub repo in Netlify and set the build/publish directory to `/` (no build command required).

## Option C — Vercel

- Use `vercel` CLI or connect the GitHub repo. For a static folder, Vercel will deploy automatically.

## Notes

- The contact form is set up to use EmailJS client-side (edit `index.html` and replace `YOUR_PUBLIC_KEY`, `YOUR_SERVICE_ID`, and `YOUR_TEMPLATE_ID`).
- If you want me to finish configuring the EmailJS template or commit any keys, paste them here and I can update the file.

---
If you want, I can push the repo initialization commands for you (I can't push to your GitHub account without credentials). Tell me your preferred host (GitHub Pages / Netlify / Vercel) and I'll continue.
