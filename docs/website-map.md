# Website map — static-site branch

The web root is the branch root: 26 HTML pages plus `assets/`, `sitemap.xml`, `robots.txt`.

## Page inventory

| Page | Copy document source | Status |
|---|---|---|
| `index.html` | §2 | Built — all 8 sections |
| `about.html` | §3 | Built |
| `services.html` | §4 | Built |
| `business-intelligence-performance-analytics.html` | §5 | Built |
| `economic-commercial-intelligence.html` | §6 | Built |
| `operational-risk-process-controls.html` | §7 | Built |
| `business-data-diagnostic.html` | §8.1 | Built |
| `business-intelligence-dashboard.html` | §8.2 | Built |
| `monthly-performance-reporting.html` | §8.3 | Built |
| `competitor-intelligence-snapshot.html` | §8.4 | Built |
| `pricing-profitability-review.html` | §8.5 | Built |
| `supplier-cost-watch.html` | §8.6 | Built |
| `operational-risk-register.html` | §8.7 | Built |
| `process-controls-diagnostic.html` | §8.8 | Built |
| `compliance-evidence-organiser.html` | §8.9 | Built |
| `research-publications.html` | §9 | Built — catalogue empty state until approved products exist |
| Individual publication pages | §10 | Deferred (rule 19.7) |
| `insights.html` | §11 | Built — empty state until first approved articles |
| `contact.html` | §12 | Built — form validates and confirms client-side |
| `faq.html` | §13 | Built |
| `client-portal.html` | §14.1 only | Built as sign-in stub (noindex, excluded from sitemap) — full portal is a separate interface |
| `privacy-policy.html` | §16.1 | Structure only — final wording pending approval |
| `website-terms.html` | §16.2 | Structure only |
| `client-service-terms.html` | §16.3 | Structure only |
| `publication-licence.html` | §16.4 | Structure only |
| `refund-policy.html` | §16.5 | Structure only |
| Cookie policy page | §16.6 | Not created — only required once cookies/analytics are actually implemented |
| `404.html` | — | Built |

## Navigation model (copy document §1)

- **Header:** brand (links home) · main navigation (Home, About Us, Our Services, Research
  Publications, Insights, FAQ, Contact Us) · Services dropdown on division pages (three divisions
  + popular services) · header CTA "Discuss Your Business Needs" → `contact.html` · "Client Login"
  → `client-portal.html`.
- **Footer:** firm descriptor · Explore (About, Services, Research Publications, Insights,
  Contact) · Our Services (three divisions) · Information (FAQ + five legal pages) · Contact
  (email, telephone, coverage) · copyright line.

## Deferred items

1. Client portal (registration, dashboard, projects, quotations, invoices, documents, information
   requests, research library) — separate authenticated interface; see client-portal-spec.md.
2. Internal administration system — see internal-administration.md; never public.
3. Publication pages — per rule 19.7 only after products are completed and approved.
4. Insights articles — first articles pending approval.
5. Cookie policy — only when cookies/analytics are introduced.
