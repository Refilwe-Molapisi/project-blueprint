# [Company Name] — Official Website

Static marketing website for a South African business advisory firm, built from the approved
copy document ("Official Website Copy and Page Content — Business Advisory Firm").

- **Stack:** plain HTML + CSS + a small amount of vanilla JS — no build step, no dependencies.
- **Design:** corporate colours `#136CFC` `#152641` `#C3F84A` `#E8F4FC`; Libre Baskerville
  headlines + Montserrat body; editorial, structured layouts.
- **Hosting:** designed for GitHub Pages (serve from the root of this branch).

## Pages

| Group | Files |
|---|---|
| Core | `index.html`, `about.html`, `services.html`, `research-publications.html`, `insights.html`, `contact.html`, `faq.html` |
| Divisions | `business-intelligence-performance-analytics.html`, `economic-commercial-intelligence.html`, `operational-risk-process-controls.html` |
| Services (9) | `business-data-diagnostic.html`, `business-intelligence-dashboard.html`, `monthly-performance-reporting.html`, `competitor-intelligence-snapshot.html`, `pricing-profitability-review.html`, `supplier-cost-watch.html`, `operational-risk-register.html`, `process-controls-diagnostic.html`, `compliance-evidence-organiser.html` |
| Legal (structure only) | `privacy-policy.html`, `website-terms.html`, `client-service-terms.html`, `publication-licence.html`, `refund-policy.html` |
| Other | `client-portal.html`, `404.html`, `sitemap.xml`, `robots.txt` |

## Before go-live — required replacements

1. **Company name:** the copy document did not provide the firm's name, so every occurrence of
   `[Company Name]` is an explicit placeholder. Find-and-replace it across all HTML files
   (or change `COMPANY_NAME` in the generator and re-run).
2. **Contact details:** replace `[Company Email]` and `[Company Telephone]` in the footer and
   contact page once confirmed.
3. **Legal pages:** the five policy pages intentionally contain only their required section
   structure — no draft legal wording. Final policies must be reviewed and approved before being
   published (per the content rules, §16 and §19.18).
4. **Contact form:** client-side validation works and shows the approved confirmation message;
   the form does not yet transmit to a mailbox or backend. The page states this honestly in
   pre-launch mode. Connect it to your email/backend and remove that note.
5. **Client portal:** `client-portal.html` is a visible stub with a pre-launch notice; the real
   portal is a separate authenticated interface (copy document §14).
6. **Research publications / insights:** both use the approved empty-state copy until real,
   approved products and articles exist.

## Deployment (GitHub Pages)

1. Push this repository to GitHub under `Refilwe-Molapisi/project-blueprint`.
2. Repository → Settings → Pages → Source: "Deploy from a branch" → Branch: `main` / root → Save.
3. The site will be served at `https://refilwe-molapisi.github.io/project-blueprint/`.

## Regenerating the site

The whole site is produced by one script (kept with the working files):

    python3 scripts/build_website.py

Edit page content in the script, re-run, and commit the output.
