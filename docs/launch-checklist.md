# Launch and setup checklist

## Business information

- [ ] Confirm the firm's name, public logo and approved contact email / telephone / channels.
- [ ] Supply service descriptions, engagement scope, delivery terms and approved pricing.
- [ ] Supply the real contact details for each enquiry path.
- [ ] Review draft privacy, website, client-service, publication licence, refund/cancellation and cookie text with appropriate advisers.

## Supabase

- [ ] Review the first proposed schema and RLS policies before applying database changes.
- [ ] Confirm the signup profile fields and permitted organisation membership model.
- [ ] Add only required environment values to Vercel; keep the service-role key server-only.
- [ ] Verify anonymous/public reads and cross-organisation isolation with dedicated security tests.
- [ ] Create private storage buckets and test expiry and authorization of signed file links.

## Resend

- [ ] Create or connect the Resend account and verify the sending domain.
- [ ] Add `RESEND_API_KEY` and `RESEND_FROM_EMAIL` to hosted server environment settings.
- [ ] Test a confirmation email, failure path, delivery status and non-production recipient.

## Paystack

- [ ] Confirm South African merchant eligibility, supported settlement currency and payment methods directly with Paystack.
- [ ] Complete account onboarding; begin in test mode.
- [ ] Add `PAYSTACK_SECRET_KEY` only to server-side environment settings.
- [ ] Verify webhook signature checks, idempotency, failure/cancellation handling and reconciliation before live use.
- [ ] Test both the under-R2,000 upfront path and the R2,000-or-more split path; never use a redirect as proof of payment.

## Vercel and production

- [ ] Connect the intended source repository to a Vercel project.
- [ ] Set Preview and Production environment values separately; do not commit local environment files.
- [ ] Deploy a Preview and verify `/`, a deep page refresh, server rendering and secret-backed requests.
- [ ] Verify mobile navigation/forms, keyboard accessibility, user-scoped access and actual payment/email workflows.
- [ ] Complete POPIA/privacy, legal copy, backup/recovery and monitoring reviews before declaring production readiness.