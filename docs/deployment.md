# Deployment and repository guide

## Repository

GitHub: `Refilwe-Molapisi/project-blueprint` (private).

| Branch | Contents | Managed by |
|---|---|---|
| `main` | Default branch: this static website + documentation (web root) | `generator/build_website.py` |
| `static-site` | Same content, generator-managed mirror of `main` | `generator/build_website.py` |

## Hosting options for the static site

1. **Vercel (primary — configured in the repository)** — the repository ships
   `vercel.json` and `scripts/build-vercel.sh`, so importing the repo is all the setup there
   is. No environment variables, no framework, no Node build:
   - On Vercel: Add New… → Project → import `Refilwe-Molapisi/project-blueprint`. The
     framework preset "Other" is detected automatically; leave Build & Output Settings on the
     defaults — they are overridden by `vercel.json` (build command `sh scripts/build-vercel.sh`,
     output directory `dist/`). Deploy.
   - The build script assembles only the web-root files into `dist/`: all 26 pages (including
     `index.html` and `404.html` — Vercel serves `404.html` automatically for unknown paths),
     `assets/`, `robots.txt` and `sitemap.xml`.
   - Deliberately NOT deployed: `docs/`, `generator/`, `README.md` and the build script itself.
     `docs/` is internal documentation (implementation rules, internal-administration and
     client-portal specs) — on a public deployment URL, the `robots.txt` disallow alone would
     not keep it from being fetched directly. If the documentation should be online too, add a
     `docs/` copy in `scripts/build-vercel.sh`.
   - `vercel.json` adds security headers to every response (`X-Content-Type-Options`,
     `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy`) and one-day browser caching
     for `/assets/`. Links keep their `.html` form (`cleanUrls` stays off) so the generated
     hrefs, the sitemap and the canonical tags all resolve without redirects.
   - After the first deploy, Vercel assigns a `*.vercel.app` domain. Once the final domain is
     chosen, update `SITE_URL` in the generator and regenerate — see checklist item 7.
2. **GitHub Pages (alternative)** — Settings → Pages → Deploy from a branch → Branch `main`,
   folder `/ (root)` → Save. Notes:
   - The automation token used for pushing can create branches and push code but cannot change
     Pages settings (fine-grained PAT permission), so this toggle is a one-time manual step.
   - Pages serves every file in the branch — including `docs/` and `generator/` — so this
     option would publish the repository documentation at direct URLs as well.
   - Expected URL: `https://refilwe-molapisi.github.io/project-blueprint/` — the canonical tags
     on every page currently point there. Update the `SITE_URL` constant in the generator when
     the final domain is known and regenerate.

## Go-live checklist

1. Replace `[Company Name]`, `[Company Email]`, `[Company Telephone]` (constants at the top of
   the generator) — rule 19.4.
2. Finalise the five policy pages after review and approval — see legal-page-structures.md.
3. Connect the contact form to a mailbox or backend. Current state: client-side validation and
   the approved confirmation message work; nothing is transmitted yet. There is deliberately no
   build notice on the public page — the status is recorded here instead of on the website.
4. Build the client portal as a separate authenticated interface — client-portal-spec.md. The
   public sign-in stub stays noindex and out of the sitemap until the portal exists.
5. Publications and insights stay in approved empty states until real, approved content exists —
   rules 19.7 and 19.8.
6. Analytics and cookies: none implemented; add a cookie policy only when technologies are
   introduced.
7. Domain: after the Vercel project exists, set `SITE_URL` in the generator to the final
   address (the `*.vercel.app` domain or a custom domain), regenerate and re-push — canonical
   tags, Open Graph URLs and the sitemap derive from it. For a custom domain, also add it under
   the Vercel project's Settings → Domains and point DNS.

## Regenerating the site

    python3 generator/build_website.py <output-dir>

Every page, `assets/`, `sitemap.xml`, `robots.txt`, `README.md`, this `docs/` folder,
`vercel.json` and `scripts/build-vercel.sh` are rewritten from the script. Replace the
corresponding files in this branch and commit.
