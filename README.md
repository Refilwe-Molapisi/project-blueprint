# [Company Name] — Official Website (static build)

Static marketing website for a South African business advisory firm, built from the approved
copy document ("Official Website Copy and Page Content — Business Advisory Firm").

**The public site contains site content only.** Every foundation, process, specification and
build-planning detail lives in [`docs/`](docs/README.md) — not on the website.

- **Stack:** plain HTML + CSS + a small amount of vanilla JS — no build step, no dependencies.
- **Design:** corporate colours `#136CFC` `#152641` `#C3F84A` `#E8F4FC`; Libre Baskerville
  headlines + Montserrat body; editorial, structured layouts.
- **Rendered by:** `generator/build_website.py` — `python3 generator/build_website.py <output-dir>`
  regenerates every page, the sitemap, robots.txt and this documentation.

## Branches

| Branch | Contents | Managed by |
|---|---|---|
| `main` | Default branch — static website + documentation at the root (web root) **and** the Lovable React app source (`src/`, `supabase/`, `public/`, config files) from the original build | Generator (site files) + Lovable editor (React app) |
| `static-site` | Same static website + documentation, generator-managed; merged into `main` | The generator script |

The static site and the Lovable app are built from the same copy document and coexist on
`main`: the site files (`*.html`, `assets/`, `docs/`, `generator/`, `sitemap.xml`,
`robots.txt`) sit at the root, the React app lives in its own files (`src/`, `supabase/`,
`public/`, config). GitHub Pages should deploy from `main`, folder `/`.

## Pages

| Group | Files |
|---|---|
| Core | `index.html`, `about.html`, `services.html`, `research-publications.html`, `insights.html`, `contact.html`, `faq.html` |
| Divisions | `business-intelligence-performance-analytics.html`, `economic-commercial-intelligence.html`, `operational-risk-process-controls.html` |
| Services (9) | `business-data-diagnostic.html`, `business-intelligence-dashboard.html`, `monthly-performance-reporting.html`, `competitor-intelligence-snapshot.html`, `pricing-profitability-review.html`, `supplier-cost-watch.html`, `operational-risk-register.html`, `process-controls-diagnostic.html`, `compliance-evidence-organiser.html` |
| Legal (structure only) | `privacy-policy.html`, `website-terms.html`, `client-service-terms.html`, `publication-licence.html`, `refund-policy.html` |
| Other | `client-portal.html` (sign-in stub, noindex), `404.html`, `sitemap.xml`, `robots.txt`, `docs/`, `generator/` |

## Documentation

| File | Contents |
|---|---|
| `docs/content-source-map.md` | Traceability: every copy-document section → where it lives now |
| `docs/website-map.md` | Page inventory, navigation model, deferred items |
| `docs/client-portal-spec.md` | Client portal specification (§14) — separate authenticated interface |
| `docs/internal-administration.md` | Internal administration specification (§15) — internal only |
| `docs/legal-page-structures.md` | Required policy-page structure (§16) + finalisation requirements |
| `docs/cta-library.md` | Call-to-action library (§17) |
| `docs/seo-content.md` | Search engine titles and descriptions (§18) |
| `docs/implementation-rules.md` | Content and implementation rules (§19) + build compliance |
| `docs/commercial-policy.md` | Payment policy and pricing rules |
| `docs/deployment.md` | Hosting, branches, go-live checklist |

## Before go-live

1. Replace `[Company Name]`, `[Company Email]`, `[Company Telephone]` (constants at the top of
   the generator), per rule 19.4 — never invent these.
2. Connect the contact form to a mailbox/backend (currently client-side validation and the
   approved confirmation only — see `docs/deployment.md`).
3. Finalise the five policy pages after review and approval (`docs/legal-page-structures.md`).
4. Build the client portal as a separate authenticated interface (`docs/client-portal-spec.md`).
5. Publications and insights remain in approved empty states until real, approved content exists.

Deployment: see `docs/deployment.md`.
