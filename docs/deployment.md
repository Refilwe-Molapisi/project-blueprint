# Deployment and repository guide

## Repository

GitHub: `Refilwe-Molapisi/project-blueprint` (private).

| Branch | Contents | Managed by |
|---|---|---|
| `main` | Lovable-built React application, built from the same copy document | Lovable editor — changes there commit straight to `main`; avoid hand edits. Note: that app still shows foundation sections (architecture, data & access, integrations, launch plan); remove them via the Lovable editor |
| `static-site` | The complete static website + this documentation (branch root = web root) | `generator/build_website.py` |

## Hosting options for the static site

1. **GitHub Pages** — Settings → Pages → Deploy from a branch → Branch `static-site`, folder
   `/ (root)` → Save. Notes:
   - The automation token used for pushing can create branches and push code but cannot change
     Pages settings (fine-grained PAT permission), so this toggle is a one-time manual step.
   - On a free plan, GitHub Pages cannot serve a private repository — make the repository public
     or use option 2.
   - Expected URL: `https://refilwe-molapisi.github.io/project-blueprint/` — the canonical tags
     on every page already point there. Update the `SITE_URL` constant in the generator when the
     final domain is known and regenerate.
2. **Vercel** — import the repository, framework preset "Other", root directory `/`, production
   branch `static-site`. Works with private repositories. The Lovable app on `main` is intended
   to deploy through Vercel as well, per its own README.

`docs/` is repository documentation: it is not linked anywhere on the site and `robots.txt`
disallows `/docs/`. If it must also be unreachable by direct URL, deploy with a build step that
copies only the web-root files (or keep the repository private and use Vercel).

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
7. Custom domain (optional): point DNS, update `SITE_URL` in the generator, regenerate, re-push.

## Regenerating the site

    python3 generator/build_website.py <output-dir>

Every page, `assets/`, `sitemap.xml`, `robots.txt`, `README.md` and this `docs/` folder are
rewritten from the script. Replace the corresponding files in this branch and commit.
