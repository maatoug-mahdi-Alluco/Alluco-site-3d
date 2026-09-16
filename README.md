# ALLUCO 3D Website — Flat Version

This version is intentionally flat: no `app/`, `components/`, or build system.

## Files

- `index.html` — website markup
- `styles.css` — visual design
- `script.js` — Three.js 3D scenes and camera scroll
- `vercel.json` — Vercel static configuration

## GitHub upload

Upload all files directly to the root of your repository. The repository should show:

```text
index.html
styles.css
script.js
vercel.json
README.md
```

## Vercel

- Import the GitHub repository
- Framework Preset: Other
- Root Directory: `./`
- Build Command: leave empty
- Output Directory: leave empty
- Deploy

No Main File Path is required.

## Local test

Because `script.js` imports Three.js as an ES module, use a small local HTTP server instead of double-clicking the HTML file.

Python:

```bash
python -m http.server 8080
```

Then open:

```text
http://localhost:8080
```

## Important

Replace contact placeholders in `index.html` before production use:

- `[ALLUCO_EMAIL]`
- `[ALLUCO_PHONE]`
- `[ALLUCO_WHATSAPP]`
- `[ALLUCO_ADDRESS]`

The 3D environment is procedural and does not require external GLB/STL models.
