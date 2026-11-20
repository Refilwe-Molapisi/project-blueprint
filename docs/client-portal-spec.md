# Client portal specification

Source: copy document §14. The client portal must be a **separate interface from the public
website**, protected by appropriate authentication and access controls (rule 19.15). The public
site exposes only the sign-in stub (`client-portal.html`, noindex, excluded from the sitemap);
everything below is the build target for that separate interface.

## 14.1 Login page — "Welcome back."

Sign in to access your projects, documents, quotations, invoices and purchased research
publications.

- Fields: Email address; Password.
- Buttons: Sign In; Forgot Password; Create Account.

## 14.2 Registration page — "Create your client account."

Register to manage your engagements, access documents and view your purchased research products.

- Fields: Full name; Email address; Password; Confirm password; Organisation name (where
  applicable); Acceptance of applicable terms and privacy notice.

## 14.3 Client dashboard — "Your account overview."

Welcome, [First Name]. Access your current engagements, outstanding actions and recent account
activity. Dashboard cards: Active Projects; Pending Actions; Outstanding Invoices; Recent
Documents; Upcoming Consultations; Purchased Publications.

## 14.4 Projects — "Your Projects"

View the status and details of current and completed engagements. Each project displays:
project reference; project name; service division; project status; start date; expected
completion date (where applicable); project contact; recent activity.

## 14.5 Project detail page — "[Project Name]"

Sections: Overview; Scope and deliverables; Project progress; Milestones; Information requests;
Documents; Consultations; Communications; Invoices and payments.

## 14.6 Quotations & Proposals

Review quotations and proposals issued by [Company Name]. Actions: view; download; accept;
request clarification (where enabled).

## 14.7 Invoices & Payments

View invoices, payment requirements and payment history. Display: invoice reference; issue date;
due date; total amount; amount paid; outstanding balance; payment status. Actions: view invoice;
download invoice; pay invoice; view receipt.

## 14.8 Your Documents

Access documents and deliverables shared with your organisation. Display: document name; related
project; document type; upload date; version; availability.

## 14.9 Information Required

View information and documents requested by your service team. Each request includes: request
description; related project; required information; due date (where applicable); submission status.

## 14.10 Your Research Library

Access research publications purchased through the account. Each item displays: publication
title; purchase date; licence; available file formats; secure download action.

Access must be restricted to the purchasing account or organisation as defined by the product
licence.
