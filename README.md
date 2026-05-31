# Jarvis Alpha Research LP public-site

Static landing page for MT5 EA AI診断.

## Files

- `index.html`: public landing page
- `netlify.toml`: Netlify config
- `vercel.json`: Vercel config
- `_headers`, `_redirects`: Cloudflare Pages/Netlify-style headers and redirect
- `wrangler.toml`: Cloudflare Pages project hint

## Before publishing

Replace every `FORM_URL_PLACEHOLDER` with the actual Google Form URL.

```bash
python3 scripts/set_form_url.py "https://forms.gle/..."
```

## Netlify

Drag this folder into Netlify Drop or connect a git repo. Publish directory: `.`

## Vercel

Import this folder/repo as a static project. Build command: empty. Output directory: `.`

## Cloudflare Pages

Create Pages project. Framework preset: None. Build command: empty. Output directory: `.`
