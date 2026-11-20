# Final content and implementation rules — build compliance

Source: copy document §19. These rules govern every page of the public site.

1. **Corporate colours** `#136CFC`, `#152641`, `#C3F84A`, `#E8F4FC` — used throughout `assets/style.css`.
2. **Typography** — Montserrat display & body per the approved system (Baskerville retained as
   a token); no additional typefaces.
3. **Visual direction** — editorial, structured, professional; consistent system, distinct layouts.
4. **No invented identity** — the firm's name, registration details, address and contact
   information are placeholders ([Company Name], [Company Email], [Company Telephone]) until
   confirmed.
5. **No invented clients, testimonials, case studies, awards or credentials** — none appear.
6. **No provisional prices** — no service prices are published anywhere.
7. **No unapproved research products** — catalogue shows the approved empty state.
8. **No fake dashboards, sales figures or performance statistics** — homepage visual is an
   abstract editorial illustration, not data.
9. **No claims outside the firm's actual authority** — copy stays within the approved document.
10. **No generic filler copy** — all copy comes from the approved document.
11. **Distinct editorial layouts** — shared design system, varied page structures.
12. **Every CTA leads to a real destination** — internal links are validated at build time; the
    portal stub keeps only the sign-in form (dead anchor links removed).
13. **Forms validate and confirm** — enquiry and sign-in forms validate client-side with clear
    confirmation or error messages.
14. **Content management** — static build; see deployment.md for the generator workflow. A CMS
    migration can adopt the copy document as the single source of truth.
15. **Authentication and access controls** — portal and admin areas are separate authenticated
    interfaces (client-portal-spec.md, internal-administration.md); the public site has none.
16. **Responsive and accessible** — mobile-first layout, skip link, semantic landmarks, focus
    states, aria-current navigation.
17. **South African English and ZAR formatting** — `lang="en-ZA"`; amounts formatted as
    R2,000 / 50%.
18. **No draft legal documents published as final** — legal pages show structure with a neutral
    review notice only.
