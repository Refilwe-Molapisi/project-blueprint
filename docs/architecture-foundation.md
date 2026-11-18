# Business advisory platform — foundation

This plan separates the public website, client records, internal operations and research-product sales. The current implementation is a browsable foundation workspace with a centrally defined company placeholder, the four supplied business units, the approved service payment rule, reusable brand tokens and Vercel build targeting. No customer account, admin console, payment, email, database schema or production connection is represented as finished.

## Proposed application structure

```text
src/
  config/          Company identity, commercial policy and navigation settings
  components/      Shared accessible interface pieces and domain sections
  integrations/    Browser-safe Supabase client and server-only adapters
  lib/             Pure domain rules, validation and formatting
  routes/          Public pages, public callbacks and protected client/admin areas
  server/          Server-only integrations and reusable email/payment handlers
  test/            Business-rule, route and security-focused tests
  styles.css       Approved fonts, semantic brand tokens and global components
docs/
  architecture-foundation.md
  launch-checklist.md
```

Keep protected pages under a shared authenticated layout. Public marketing pages and individual research-publication pages remain shareable routes. Only promote an integration after its credentials, callbacks, access rules and failure states have been verified.

## Relational entity plan

Use separate, related tables; IDs should be UUIDs, ownership foreign keys non-null where required, and records should carry `created_at` / `updated_at`. Add unique constraints for natural identifiers and indexes for owner, organisation, status and foreign-key query paths.

| Area | Initial entities and relationships |
| --- | --- |
| Identity and access | `profiles` → `auth.users`; `roles`; `permissions`; `role_permissions`; `organisations`; `organisation_memberships` linking users and organisations |
| Customer pipeline | `leads`; `contacts`; `enquiries`; `quotations` → leads / organisations; `quote_items` → quotations / services; `proposals`; `engagements` |
| Service catalogue | `service_divisions`; `services` → division; `service_packages` → service |
| Delivery | `projects` → engagement / organisation; `project_milestones`; `tasks`; `information_requests`; `client_submissions`; `deliverables`; `consultations`; `project_messages` |
| Finance | `invoices` → engagement / organisation; `invoice_items`; `payment_transactions`; `payment_status_history`; `refunds`; `receipts` |
| Research commerce | `publication_categories`; `publications`; `publication_versions`; `product_previews`; `product_files`; `product_prices`; `product_licences`; `orders` → customer; `order_items`; `purchase_entitlements` → customer / publication version |
| Administration | `notifications`; `activity_logs`; `audit_records`; `website_content`; `faqs`; `contact_submissions`; `system_settings` |

### Relationship sketch

```text
auth.users ── profiles ──< organisation_memberships >── organisations
organisations ──< enquiries ──< quotations ──< quote_items >── services
organisations ──< engagements ──< projects ──< milestones / tasks / deliverables
engagements ──< invoices ──< invoice_items
invoices ──< payment_transactions ──< status_history
customers ──< orders ──< order_items >── publication_versions ──< entitlements
```

## Initial schema and migration strategy

The database is governed through Lovable's connected Supabase project, so this foundation does not create or apply a migration. In the first reviewed migration, create a small, useful identity and content foundation before adding service delivery, finance and commerce tables in later changes. Make migrations additive, reversible where practical and separately reviewed.

For each public-schema table, follow the required order: `CREATE TABLE`, explicit table `GRANT`s for the intended database roles, enable RLS, then create policies. Include grants in that same migration. Use foreign keys with deliberate delete behavior (`CASCADE` only for true dependents; otherwise prefer `RESTRICT` or `SET NULL`), check constraints for states / amounts, and unique constraints for transaction references and entitlements. Never copy production customer information into sample data.

## Authentication and access model

- Supabase Auth owns email/password registration, verification, login, logout and recovery.
- A `profiles` row is expected for each person; store only needed display and preference data there. Link it to `auth.users(id)` with `ON DELETE CASCADE` and create it on signup.
- Roles attach to organisation membership or internal staff membership rather than trusting a browser-supplied role. A future internal administrator may manage users only after server-validated role checks.
- Public pages have no sign-in gate. Client and admin pages live in separate protected areas. A publication entitlement does not grant access to client projects.
- Sensitive mutations revalidate input and identity on the server. Service-role access is reserved for a verified privileged operation, never normal reads or role checks.

## RLS strategy

Enable RLS on every app-owned table. Public visitors receive read access only to explicitly published catalogue, article and FAQ content. A client can read only their organisation's permitted records, based on active membership. Purchasers can read their own orders and entitlements only. Internal staff access is granted by validated staff-role policies. Owners also need an explicit owner-read policy for hidden/draft rows and records they must update or delete. Deny by default, keep private file metadata behind the same owner checks, and test cross-organisation access and anonymous access before launch.

## File storage

| Bucket | Visibility | Intended contents |
| --- | --- | --- |
| `publication-previews` | Public only for approved previews | Watermarked/sample extracts intentionally published for discovery |
| `publication-products` | Private | Purchased full reports and versioned digital products; short-lived signed download links after entitlement verification |
| `client-documents` | Private | Client submissions and confidential deliverables; organisation-scoped authorization |
| `brand-assets` | Public, curated | Approved logo and public website assets |

Validate file size, type and owner at upload; avoid placing private client or paid files under public URLs. Keep entitlement checks and signed-link generation server-side, expire links, and record sensitive delivery actions.

## Resend and Paystack design

Neither integration is connected yet. Add both through server-side handlers only after credentials and account setup are supplied.

- **Resend:** a shared brand/email template layer; configurable sender and recipient; events for enquiries, quotes, engagements, invoices, payments, project activity and digital orders; record provider message IDs and delivery outcomes where available. Confirm the sender domain before production delivery.
- **Paystack:** create a unique reference and initialise checkout on the server in ZAR; persist a pending transaction; verify the provider transaction server-side and validate webhook signatures; make updates idempotent; record failures, cancellations, refunds and reconciliation history. A browser return URL is never proof of payment. Keep paid product files private and release a purchase entitlement only after server verification.
- **Service payment policy:** below R2,000 is 100% upfront; R2,000 and above is 50% initially and 50% final. The policy is centralised in `src/config/business.ts`; amounts are computed in cents in `src/lib/payment-policy.ts` and covered by tests.
- Verify South African merchant availability, ZAR settlement and currently supported payment methods with Paystack before live transactions. This website does not claim that verification has happened.

## Vercel deployment

The project is a TanStack Start app. Vercel is selected in the existing build wrapper when the Vercel build environment is present; the existing Lovable preview configuration remains intact. Vercel supports TanStack Start through Nitro and Vercel Functions. Connect the repository to Vercel, use its automatic framework detection, configure environment variables for Preview and Production, then verify the homepage, a deep link, server rendering and one server-side secret-backed flow in a Vercel preview before launch.

| Variable | Where | Purpose |
| --- | --- | --- |
| `VITE_SUPABASE_URL` | Browser build | Supabase project URL |
| `VITE_SUPABASE_PUBLISHABLE_KEY` | Browser build | Publishable key; RLS still applies |
| `SUPABASE_URL` | Server | Supabase server endpoint |
| `SUPABASE_PUBLISHABLE_KEY` | Server | Server-side user-scoped Data API access |
| `SUPABASE_SERVICE_ROLE_KEY` | Server only | Restricted privileged operations only; never expose with `VITE_` |
| `RESEND_API_KEY` | Server only | Transactional email after Resend setup |
| `RESEND_FROM_EMAIL` | Server only | Verified sender address |
| `PAYSTACK_SECRET_KEY` | Server only | Payment initialization and verification after Paystack setup |
| `APP_BASE_URL` | Server | Canonical origin for trusted email and payment links |

Local and hosted environment values are managed outside source control. Do not commit `.env` files or secret values.

## Complete website sitemap

```text
Public
  /  Home
  /about
  /services
  /services/business-intelligence
  /services/business-intelligence/business-data-diagnostic
  /services/business-intelligence/business-intelligence-dashboard
  /services/business-intelligence/monthly-business-performance-reporting
  /services/economic-commercial-intelligence
  /services/economic-commercial-intelligence/competitor-intelligence-snapshot
  /services/economic-commercial-intelligence/pricing-profitability-review
  /services/economic-commercial-intelligence/supplier-cost-watch
  /services/operational-risk-process-controls
  /services/operational-risk-process-controls/operational-risk-register
  /services/operational-risk-process-controls/process-controls-diagnostic
  /services/operational-risk-process-controls/compliance-evidence-organiser
  /research-publications  catalogue and category/search filters
  /research-publications/:publicationSlug  product details and preview
  /insights  searchable and categorised articles
  /insights/:articleSlug  article and related content
  /contact
  /faq
  /privacy-policy
  /website-terms
  /client-service-terms
  /publication-licence
  /digital-product-refund-policy
  /cookie-policy  if applicable
Accounts (protected, later phase)
  /auth  registration, login and verification states
  /auth/forgot-password
  /auth/reset-password
  /client  dashboard
  /client/organisation
  /client/projects and /client/projects/:projectId
  /client/quotations, /client/invoices and /client/payments
  /client/documents, /client/requests, /client/messages, /client/meetings
  /client/publications and /client/settings
Administration (protected, later phase)
  /admin  dashboard and configuration
  /admin/content, /admin/services, /admin/publications, /admin/enquiries
  /admin/leads, /admin/clients, /admin/quotes, /admin/projects
  /admin/invoices, /admin/payments, /admin/orders, /admin/users, /admin/audit
```

## Design and reusable interface plan

Use the approved palette (primary blue `#136CFC`, dark blue `#152641`, selective lime `#C3F84A`, pale blue `#E8F4FC` and white) with Libre Baskerville for editorial headlines and Montserrat for navigation, controls and body text. Keep hierarchy editorial, with dark-blue depth, fine rules, compact structured cards, purposeful spacing and restrained motion. Build reusable headers, public and protected shells, breadcrumbs, form fields, status labels, publication cards, empty/error/success states and accessible mobile navigation. Do not invent testimonials, client names, credentials, statistics, address or contact details.

## Roadmap

1. **Foundation (current):** architecture workspace, centralized company/service/payment settings, approved brand tokens, Vercel build target and business-rule test.
2. **Public website:** home, about, service pages, research catalogue and detail pages, insights, contact, FAQs and legal drafts.
3. **Commercial workflows:** enquiry storage, approved account setup, quotes, Paystack transactions, private digital delivery and Resend email.
4. **Client environment:** organisation-scoped projects, payments, files, requests, communications and purchases.
5. **Administration:** content management, customer operations, roles and audit views.
6. **Launch verification:** access tests, external payment/email checks, Vercel deep-link and workflow tests, mobile review, backup/recovery and legal review.

## Current status and decisions required

| Status | What it means |
| --- | --- |
| Implemented | Foundation workspace, approved visual tokens, supplied service structure, centralized placeholder/settings, payment calculation, tests and Vercel-target build configuration |
| Connected but not verified | Supabase environment keys are present in the current preview; data access, authentication, schema and RLS have not been verified |
| Credentials still required | Resend API key and verified sender; Paystack secret key and account setup; Vercel project/repository configuration |
| External verification required | Paystack South African merchant eligibility, ZAR settlement/payment methods; business/legal review of policies and legal drafts |
| Later phases | Public content pages, account flows, admin workspace, database schema/migrations, file buckets, transactional emails, online checkout and client portal |

The final company name and publishable company contact details remain configurable placeholders, not invented values.