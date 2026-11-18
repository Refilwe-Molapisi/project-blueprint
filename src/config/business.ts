/** Company-owned details and commercial rules live here until content management is introduced. */
export const businessConfig = {
  brandNamePlaceholder: "Your firm name",
  descriptor: "Business Advisory & Intelligence",
  operatingCurrency: "ZAR",
  servicePaymentPolicy: {
    thresholdCents: 200_000,
    depositPercent: 50,
  },
} as const;

export const businessUnits = [
  {
    number: "01",
    slug: "business-intelligence",
    name: "Business Intelligence & Performance Analytics",
    summary: "A clearer view of business performance and the information behind it.",
    services: [
      "Business Data Diagnostic",
      "Business Intelligence Dashboard",
      "Monthly Business Performance Reporting",
    ],
  },
  {
    number: "02",
    slug: "economic-commercial-intelligence",
    name: "Economic & Commercial Intelligence",
    summary: "Evidence on markets, competitors, pricing and supplier costs.",
    services: [
      "Competitor Intelligence Snapshot",
      "Pricing & Profitability Review",
      "Supplier Cost Watch",
    ],
  },
  {
    number: "03",
    slug: "operational-risk",
    name: "Operational Risk, Process & Controls Advisory",
    summary: "Practical visibility into operational risks, processes and controls.",
    services: [
      "Operational Risk Register",
      "Process & Controls Diagnostic",
      "Compliance Evidence Organiser",
    ],
  },
  {
    number: "04",
    slug: "research-publications",
    name: "Research Publications & Intelligence Products",
    summary: "Ready-made research publications, distinct from commissioned advisory work.",
    services: [
      "Industry performance reports",
      "Economic and market intelligence reports",
      "Commercial, statistical and data publications",
    ],
  },
] as const;

export const foundationNavigation = [
  { label: "Overview", href: "#overview" },
  { label: "Business units", href: "#business-units" },
  { label: "Architecture", href: "#architecture" },
  { label: "Data & access", href: "#data-access" },
  { label: "Integrations", href: "#integrations" },
  { label: "Website map", href: "#website-map" },
  { label: "Launch plan", href: "#launch-plan" },
] as const;