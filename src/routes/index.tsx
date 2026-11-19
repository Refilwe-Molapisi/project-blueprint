import { createFileRoute } from "@tanstack/react-router";
import {
  ArrowDownRight,
  ArrowRight,
  BarChart3,
  Boxes,
  Check,
  CircleDot,
  Database,
  FileCheck2,
  FileText,
  Fingerprint,
  Layers3,
  LockKeyhole,
  Mail,
  Map,
  Server,
  ShieldCheck,
  ShoppingBag,
  Workflow,
  type LucideIcon,
} from "lucide-react";

import { Button } from "@/components/ui/button";
import { businessConfig, businessUnits, foundationNavigation } from "@/config/business";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "Business Advisory & Intelligence | Digital Foundation" },
      {
        name: "description",
        content:
          "Explore the planned digital foundation, service structure, access model and delivery roadmap for a South African business advisory firm.",
      },
      { property: "og:title", content: "Business Advisory & Intelligence | Digital Foundation" },
      {
        property: "og:description",
        content:
          "A clear, secure foundation for business advisory, intelligence, research products and future client services.",
      },
      { property: "og:type", content: "website" },
      { name: "twitter:card", content: "summary_large_image" },
    ],
  }),
  component: FoundationHome,
});

type IconType = LucideIcon;

const architectureLayers: { icon: IconType; name: string; detail: string }[] = [
  { icon: Layers3, name: "Public website", detail: "Discover services, insights and publications" },
  { icon: Fingerprint, name: "Identity & access", detail: "Customers, organisations and staff roles" },
  { icon: Workflow, name: "Client operations", detail: "Enquiries, proposals and project delivery" },
  { icon: ShoppingBag, name: "Research commerce", detail: "Orders, licences and secure product access" },
];

const databaseGroups = [
  {
    title: "Identity & relationships",
    items: ["Profiles", "Roles & permissions", "Organisations", "Memberships"],
  },
  {
    title: "Enquiries & engagements",
    items: ["Leads & contacts", "Enquiries", "Quotations & proposals", "Engagements"],
  },
  {
    title: "Service delivery",
    items: ["Divisions & services", "Projects & milestones", "Requests & submissions", "Deliverables"],
  },
  {
    title: "Finance & research",
    items: ["Invoices & payments", "Publications & versions", "Orders & line items", "Purchase entitlements"],
  },
  {
    title: "Administration",
    items: ["Notifications", "Activity & audit records", "Website content", "FAQs & settings"],
  },
];

const integrations: {
  icon: IconType;
  name: string;
  purpose: string;
  status: string;
  state: "ready" | "pending" | "planned";
}[] = [
  {
    icon: Database,
    name: "Supabase",
    purpose: "Database, authentication, access policies and private files",
    status: "Connection unverified",
    state: "pending",
  },
  {
    icon: Mail,
    name: "Resend",
    purpose: "Branded service updates and purchase messages",
    status: "Credentials required",
    state: "planned",
  },
  {
    icon: CircleDot,
    name: "Paystack",
    purpose: "Service payments and digital publication purchases",
    status: "Account & eligibility checks required",
    state: "planned",
  },
  {
    icon: Server,
    name: "Vercel",
    purpose: "Planned deployment target; preview configuration retained",
    status: "Deployment not verified",
    state: "ready",
  },
];

const roadmap = [
  { number: "01", title: "Foundation", detail: "Architecture, business structure, payment rule and deployment target", state: "In place" },
  { number: "02", title: "Public website", detail: "Company pages, service information, publications and enquiries", state: "Next" },
  { number: "03", title: "Sales & payments", detail: "Quotations, secure checkout, receipts and transactional email", state: "Planned" },
  { number: "04", title: "Client workspace", detail: "Organisation-scoped projects, documents and communications", state: "Planned" },
  { number: "05", title: "Administration", detail: "Content management, operations and audit views", state: "Planned" },
];

const sitemapGroups = [
  { title: "Public", paths: ["/", "/about", "/services", "/research-publications", "/insights", "/contact", "/faq"] },
  { title: "Client account · later phase", paths: ["/auth", "/client", "/client/projects", "/client/invoices", "/client/documents"] },
  { title: "Administration · later phase", paths: ["/admin", "/admin/content", "/admin/publications", "/admin/projects", "/admin/audit"] },
];

function StatusTag({ children, state = "planned" }: { children: string; state?: "ready" | "pending" | "planned" }) {
  const style = {
    ready: "bg-accent text-accent-foreground",
    pending: "bg-secondary text-secondary-foreground",
    planned: "border border-border bg-background text-muted-foreground",
  }[state];
  return <span className={`inline-flex items-center gap-1.5 px-2 py-1 text-[11px] font-semibold ${style}`}>{children}</span>;
}

function SectionIntro({
  number,
  title,
  children,
}: {
  number: string;
  title: string;
  children: string;
}) {
  return (
    <div className="mb-8 grid gap-3 border-b border-border pb-5 sm:grid-cols-[7rem_1fr] sm:items-end">
      <span className="font-mono text-xs text-primary">{number} / FOUNDATION</span>
      <div>
        <h2 className="font-serif text-3xl text-foreground sm:text-4xl">{title}</h2>
        <p className="mt-2 max-w-3xl text-sm leading-6 text-muted-foreground">{children}</p>
      </div>
    </div>
  );
}

function FoundationHome() {
  return (
    <div className="min-h-screen bg-background text-foreground">
      <header className="border-b border-border bg-background">
        <div className="mx-auto flex max-w-[1440px] items-center justify-between gap-5 px-5 py-4 sm:px-8 lg:px-12">
          <a href="#overview" className="flex min-w-0 items-center gap-3" aria-label="Go to overview">
            <span className="grid size-10 shrink-0 place-items-center bg-primary text-primary-foreground">
              <BarChart3 size={20} strokeWidth={1.8} />
            </span>
            <span className="min-w-0">
              <span className="block truncate font-serif text-base">{businessConfig.brandNamePlaceholder}</span>
              <span className="block truncate text-[10px] font-medium uppercase tracking-[0.12em] text-muted-foreground">
                {businessConfig.descriptor}
              </span>
            </span>
          </a>
          <div className="hidden items-center gap-3 sm:flex">
            <StatusTag state="ready"><Check size={12} /> Foundation workspace</StatusTag>
            <span className="text-xs text-muted-foreground">South Africa · Remote-first</span>
          </div>
        </div>
      </header>

      <div className="mx-auto grid max-w-[1440px] lg:grid-cols-[250px_minmax(0,1fr)]">
        <aside className="border-b border-border bg-secondary/50 px-5 py-5 lg:min-h-[calc(100vh-73px)] lg:border-b-0 lg:border-r lg:px-7 lg:py-9">
          <p className="mb-4 text-[10px] font-semibold uppercase tracking-[0.16em] text-muted-foreground">Foundation map</p>
          <nav aria-label="Foundation sections" className="flex gap-2 overflow-x-auto pb-1 lg:flex-col lg:overflow-visible">
            {foundationNavigation.map((item, index) => (
              <a
                key={item.href}
                href={item.href}
                className="flex shrink-0 items-center gap-3 border border-transparent px-3 py-2.5 text-sm text-muted-foreground transition-colors hover:border-border hover:bg-background hover:text-foreground lg:w-full"
              >
                <span className="font-mono text-[10px] text-primary">0{index + 1}</span>
                <span>{item.label}</span>
                <ArrowRight className="ml-auto hidden size-3 lg:block" />
              </a>
            ))}
          </nav>
          <div className="mt-8 hidden border-t border-border pt-5 lg:block">
            <p className="text-xs font-semibold">Current stage</p>
            <p className="mt-1 text-xs leading-5 text-muted-foreground">Architecture and foundations</p>
            <div className="mt-4 h-1 bg-border"><div className="h-full w-1/6 bg-primary" /></div>
            <p className="mt-2 text-[10px] text-muted-foreground">Stage 01 of 06</p>
          </div>
        </aside>

        <main className="min-w-0 px-5 pb-20 sm:px-8 lg:px-14">
          <section id="overview" className="scroll-mt-8 border-b border-border py-12 sm:py-16 lg:py-20">
            <div className="flex flex-wrap items-center gap-2">
              <span className="text-[11px] font-semibold uppercase tracking-[0.14em] text-primary">Digital operating environment</span>
              <span className="h-px w-8 bg-primary" />
              <span className="text-xs text-muted-foreground">Foundation / 2026</span>
            </div>
            <h1 className="mt-6 max-w-4xl font-serif text-4xl leading-[1.14] sm:text-5xl lg:text-6xl">
              Clear thinking.<br />
              <span className="text-primary">Sound foundations.</span>
            </h1>
            <p className="mt-6 max-w-2xl text-base leading-7 text-muted-foreground sm:text-lg">
              A considered blueprint for a South African business advisory firm—bringing research,
              commercial insight and practical operations into one secure digital environment.
            </p>
            <div className="mt-8 flex flex-wrap gap-3">
              <Button asChild size="lg" className="rounded-none">
                <a href="#business-units">Explore the business structure <ArrowDownRight /></a>
              </Button>
              <Button asChild variant="outline" size="lg" className="rounded-none">
                <a href="#launch-plan">View the delivery roadmap</a>
              </Button>
            </div>
            <div className="mt-12 grid border-y border-border sm:grid-cols-3">
              {[
                { value: "04", label: "Business units" },
                { value: "01", label: "Central payment policy" },
                { value: "06", label: "Planned delivery stages" },
              ].map((item, index) => (
                <div key={item.label} className={`py-5 ${index > 0 ? "border-t border-border sm:border-l sm:border-t-0 sm:pl-6" : "sm:pr-6"}`}>
                  <span className="font-serif text-3xl">{item.value}</span>
                  <span className="ml-3 text-xs text-muted-foreground">{item.label}</span>
                </div>
              ))}
            </div>
          </section>

          <section id="business-units" className="scroll-mt-8 border-b border-border py-12 sm:py-16">
            <SectionIntro number="01" title="One firm. Four capabilities.">
              A distinct structure for commissioned advisory services and ready-made research products, as supplied in the foundation brief.
            </SectionIntro>
            <div className="grid gap-x-8 md:grid-cols-2">
              {businessUnits.map((unit) => (
                <article key={unit.number} className="border-t border-border py-6 first:border-t-0 md:nth-[n+3]:border-t">
                  <div className="flex items-start justify-between gap-4">
                    <span className="font-mono text-xs text-primary">{unit.number}</span>
                    <span className="text-xs text-muted-foreground">{unit.services.length} focus areas</span>
                  </div>
                  <h3 className="mt-3 max-w-md font-serif text-xl leading-snug">{unit.name}</h3>
                  <p className="mt-2 text-sm leading-6 text-muted-foreground">{unit.summary}</p>
                  <ul className="mt-4 space-y-2">
                    {unit.services.map((service) => (
                      <li key={service} className="flex items-start gap-2 text-xs leading-5 text-foreground/80">
                        <Check className="mt-0.5 size-3.5 shrink-0 text-primary" />{service}
                      </li>
                    ))}
                  </ul>
                </article>
              ))}
            </div>
            <div className="mt-5 flex items-start gap-3 border-l-2 border-primary bg-secondary/70 px-4 py-3 text-xs leading-5 text-secondary-foreground">
              <FileCheck2 className="mt-0.5 size-4 shrink-0" />
              <p>Research publications are developed for multiple buyers; commissioned research remains a separately scoped advisory engagement.</p>
            </div>
          </section>

          <section id="architecture" className="scroll-mt-8 border-b border-border py-12 sm:py-16">
            <SectionIntro number="02" title="A platform built in layers.">
              The structure keeps public discovery, client information, internal operations and research-product sales connected—but clearly separated.
            </SectionIntro>
            <div className="grid gap-px border border-border bg-border sm:grid-cols-2">
              {architectureLayers.map(({ icon: Icon, name, detail }, index) => (
                <div key={name} className="flex gap-4 bg-background p-5 sm:p-6">
                  <span className="grid size-10 shrink-0 place-items-center bg-secondary text-primary"><Icon size={19} /></span>
                  <div>
                    <div className="flex items-center gap-2"><span className="font-mono text-[10px] text-primary">0{index + 1}</span><h3 className="text-sm font-semibold">{name}</h3></div>
                    <p className="mt-1 text-xs leading-5 text-muted-foreground">{detail}</p>
                  </div>
                </div>
              ))}
            </div>
            <div className="mt-6 flex flex-wrap items-center gap-2 text-[11px] text-muted-foreground" aria-label="Architecture flow">
              <span className="border border-border bg-background px-3 py-2">Public discovery</span><ArrowRight className="size-3" />
              <span className="border border-border bg-background px-3 py-2">Enquiry & engagement</span><ArrowRight className="size-3" />
              <span className="border border-border bg-background px-3 py-2">Secure delivery</span><ArrowRight className="size-3" />
              <span className="border border-border bg-background px-3 py-2">Ongoing relationship</span>
            </div>
          </section>

          <section id="data-access" className="scroll-mt-8 border-b border-border py-12 sm:py-16">
            <SectionIntro number="03" title="Connected data. Deliberate access.">
              A relational data model prevents disconnected records. Access is designed around each person’s role and active organisation membership, not hidden interface elements.
            </SectionIntro>
            <div className="grid gap-8 xl:grid-cols-[1.5fr_1fr]">
              <div>
                <div className="mb-3 flex items-center gap-2"><Database className="size-4 text-primary" /><h3 className="text-sm font-semibold">Planned data domains</h3></div>
                <div className="divide-y divide-border border-y border-border">
                  {databaseGroups.map((group) => (
                    <div key={group.title} className="grid gap-2 py-3 sm:grid-cols-[10rem_1fr] sm:gap-5">
                      <h4 className="text-xs font-semibold">{group.title}</h4>
                      <div className="flex flex-wrap gap-1.5">
                        {group.items.map((item) => <span key={item} className="border border-border px-2 py-1 text-[10px] text-muted-foreground">{item}</span>)}
                      </div>
                    </div>
                  ))}
                </div>
                <p className="mt-3 text-[11px] leading-5 text-muted-foreground">Schema and access policies are a later reviewed step; no customer records or tables are represented as live.</p>
              </div>
              <div>
                <div className="mb-3 flex items-center gap-2"><ShieldCheck className="size-4 text-primary" /><h3 className="text-sm font-semibold">Access principles</h3></div>
                <ul className="divide-y divide-border border-y border-border">
                  {[
                    "Public visitors see only approved public content.",
                    "Clients access only permitted records for their organisation.",
                    "Purchases do not grant access to client project records.",
                    "Private files require an authorised, time-limited link.",
                    "Sensitive changes are checked on the server and recorded.",
                  ].map((principle) => (
                    <li key={principle} className="flex gap-2.5 py-3 text-xs leading-5 text-muted-foreground"><LockKeyhole className="mt-0.5 size-3.5 shrink-0 text-primary" />{principle}</li>
                  ))}
                </ul>
              </div>
            </div>
            <div className="mt-7">
              <div className="mb-3 flex items-center gap-2"><Boxes className="size-4 text-primary" /><h3 className="text-sm font-semibold">Planned file storage</h3></div>
              <div className="grid border border-border sm:grid-cols-2 xl:grid-cols-4">
                {[
                  ["Public previews", "Approved sample extracts", "Public"],
                  ["Publication products", "Purchased full reports", "Private"],
                  ["Client documents", "Submissions & deliverables", "Private"],
                  ["Brand assets", "Approved public materials", "Curated"],
                ].map(([title, detail, access]) => (
                  <div key={title} className="border-b border-border p-4 last:border-b-0 sm:odd:border-r xl:border-b-0 xl:border-r xl:last:border-r-0">
                    <p className="text-xs font-semibold">{title}</p><p className="mt-1 text-[11px] text-muted-foreground">{detail}</p>
                    <span className="mt-3 inline-block text-[10px] font-semibold uppercase tracking-wide text-primary">{access} access</span>
                  </div>
                ))}
              </div>
            </div>
          </section>

          <section id="integrations" className="scroll-mt-8 border-b border-border py-12 sm:py-16">
            <SectionIntro number="04" title="Integrations, with honest status.">
              The architecture names the intended services without implying that credentials, accounts, payment flows or production delivery have been verified.
            </SectionIntro>
            <div className="divide-y divide-border border-y border-border">
              {integrations.map(({ icon: Icon, name, purpose, status, state }) => (
                <div key={name} className="grid gap-3 py-4 sm:grid-cols-[2.5rem_10rem_1fr_auto] sm:items-center">
                  <span className="grid size-9 place-items-center bg-secondary text-primary"><Icon size={17} /></span>
                  <h3 className="text-sm font-semibold">{name}</h3>
                  <p className="text-xs leading-5 text-muted-foreground">{purpose}</p>
                  <StatusTag state={state}>{status}</StatusTag>
                </div>
              ))}
            </div>
            <div className="mt-6 grid gap-6 border-t border-border pt-5 md:grid-cols-2">
              <div>
                <div className="flex items-center gap-2"><FileText className="size-4 text-primary" /><h3 className="text-xs font-semibold">Service payment rule</h3></div>
                <p className="mt-2 text-xs leading-5 text-muted-foreground">Under R2,000: full payment upfront. R2,000 and above: 50% deposit and 50% final payment. Exactly R2,000 uses the split arrangement.</p>
                <p className="mt-1 text-[10px] text-muted-foreground">Rule is held centrally and covered by a calculation test. Gateway transactions are not live.</p>
              </div>
              <div>
                <div className="flex items-center gap-2"><Mail className="size-4 text-primary" /><h3 className="text-xs font-semibold">Server-side communications</h3></div>
                <p className="mt-2 text-xs leading-5 text-muted-foreground">Resend templates are planned for enquiries, proposals, invoices, project updates and publication purchases. Sender details, provider credentials and delivery tracking still require setup.</p>
              </div>
            </div>
          </section>

          <section id="website-map" className="scroll-mt-8 border-b border-border py-12 sm:py-16">
            <SectionIntro number="05" title="A clear path through the platform.">
              The sitemap keeps public discovery easy to navigate and reserves protected client and administration areas for later, permission-checked stages.
            </SectionIntro>
            <div className="grid gap-8 md:grid-cols-3">
              {sitemapGroups.map((group) => (
                <div key={group.title}>
                  <h3 className="mb-3 flex items-center gap-2 text-xs font-semibold"><Map className="size-3.5 text-primary" />{group.title}</h3>
                  <ul className="space-y-2 border-t border-border pt-3">
                    {group.paths.map((path) => <li key={path} className="font-mono text-[11px] text-muted-foreground">{path}</li>)}
                  </ul>
                </div>
              ))}
            </div>
            <div className="mt-6 border-l-2 border-accent bg-secondary/70 px-4 py-3 text-xs leading-5 text-secondary-foreground">
              Legal pages, individual service and publication pages, and client/admin sub-pages are included in the documented full sitemap; content awaits approved business information.
            </div>
          </section>

          <section id="launch-plan" className="scroll-mt-8 py-12 sm:py-16">
            <SectionIntro number="06" title="Built in deliberate stages.">
              Start with the architecture, then add each business workflow only when the content, credentials and safeguards are ready.
            </SectionIntro>
            <ol className="border-y border-border">
              {roadmap.map((stage) => (
                <li key={stage.number} className="grid gap-2 border-b border-border py-4 last:border-b-0 sm:grid-cols-[3rem_11rem_1fr_auto] sm:items-center sm:gap-4">
                  <span className="font-mono text-xs text-primary">{stage.number}</span>
                  <h3 className="text-sm font-semibold">{stage.title}</h3>
                  <p className="text-xs leading-5 text-muted-foreground">{stage.detail}</p>
                  <StatusTag state={stage.state === "In place" ? "ready" : stage.state === "Next" ? "pending" : "planned"}>{stage.state}</StatusTag>
                </li>
              ))}
            </ol>
            <div className="mt-8 grid gap-6 border border-border bg-secondary/50 p-5 sm:grid-cols-2 sm:p-6">
              <div>
                <h3 className="text-xs font-semibold">Business details still needed</h3>
                <p className="mt-2 text-xs leading-5 text-muted-foreground">Firm name, approved logo and contact channels; confirmed service scopes and pricing; publication information; legal review.</p>
              </div>
              <div>
                <h3 className="text-xs font-semibold">External setup still needed</h3>
                <p className="mt-2 text-xs leading-5 text-muted-foreground">Supabase access and policy verification; Resend account and sender domain; Paystack merchant and ZAR checks; Vercel project configuration and deployment verification.</p>
              </div>
            </div>
            <div className="mt-8 flex flex-wrap items-center justify-between gap-4 border-t border-border pt-6">
              <p className="text-xs text-muted-foreground">{businessConfig.brandNamePlaceholder} <span className="mx-2">/</span> {businessConfig.descriptor}</p>
              <a href="#overview" className="inline-flex items-center gap-2 text-xs font-semibold text-primary hover:underline">Back to overview <ArrowRight className="size-3" /></a>
            </div>
          </section>
        </main>
      </div>
    </div>
  );
}