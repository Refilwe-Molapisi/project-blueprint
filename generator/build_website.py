#!/usr/bin/env python3
"""Build the Business Advisory Firm website (Refilwe-Molapisi/project-blueprint).

Generates a static multi-page site from the approved copy document
(upload/Official Website Copy and Page Content — Business Advisory Firm.md).

Design: corporate colours #136CFC / #152641 / #C3F84A / #E8F4FC,
Montserrat display & body (Libre Baskerville retained as a token), flat editorial layout.
"""
import os, sys

# ── Single source of truth for placeholder facts (rule 19.4: do not invent) ──
COMPANY_NAME = "[Company Name]"          # ← replace once approved, or find-replace in output
COMPANY_EMAIL = "[Company Email]"        # ← publish once confirmed
COMPANY_PHONE = "[Company Telephone]"    # ← publish once confirmed (or remove)
YEAR = "2026"
SITE_URL = "https://refilwe-molapisi.github.io/project-blueprint/"

OUT = (sys.argv[1] if len(sys.argv) > 1 else
       os.path.join(os.path.dirname(os.path.abspath(__file__)), "site-output"))

# ═══════════════════════════════ CSS ═══════════════════════════════
CSS = r"""
:root{
  /* ── Brand palette (unchanged) ── */
  --blue:#136CFC; --navy:#152641; --lime:#C3F84A; --tint:#E8F4FC;
  --ink:#152641; --muted:#4A5A72; --line:#D7E5F2; --white:#FFFFFF;
  --serif:"Libre Baskerville",Georgia,"Times New Roman",serif;
  --sans:"Montserrat","Segoe UI",Arial,sans-serif;
  /* ── Reusable design tokens (flat editorial system) ── */
  --font-display:var(--sans);          /* headings & display type */
  --font-body:var(--sans);             /* body copy */
  --rule:var(--lime);                  /* hairline rules & cell borders */
  --rule-strong:var(--navy);           /* strong structural rules */
  --frame:var(--navy);                 /* page-frame colour behind the sheet */
  --frame-w:clamp(12px,2.5vw,30px);    /* page-frame width */
  --sheet:var(--white);                /* content sheet background */
  --edge-w:3px;                        /* accent edge line on the sheet */
  --mark:9px;                          /* accent square marker size */
  --radius:0px;                        /* sharp corners everywhere */
  --shadow:none;                       /* flat UI — no elevation */
  --sp-section:clamp(48px,7vw,100px);  /* vertical section rhythm */
  --text-display:clamp(32px,5.2vw,64px); /* display heading size */
}
*{margin:0;padding:0;box-sizing:border-box}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
body{font-family:var(--font-body);color:var(--ink);background:var(--frame);line-height:1.7;
  font-size:clamp(15px,1.05vw + 9px,17px);-webkit-font-smoothing:antialiased}
.sheet{background:var(--sheet);margin:var(--frame-w);
  box-shadow:inset calc(-1 * var(--edge-w)) 0 0 0 var(--rule)}
img,svg{max-width:100%;height:auto}
a{color:var(--blue);text-decoration:none}
a:hover{text-decoration:underline}
a:focus-visible,button:focus-visible,summary:focus-visible,input:focus-visible,
select:focus-visible,textarea:focus-visible{outline:2.5px solid var(--navy);outline-offset:3px;border-radius:4px}
h1,h2,h3,.serif{font-family:var(--font-display);color:var(--navy)}
h1{font-weight:800;text-transform:uppercase;font-size:var(--text-display);
  line-height:.98;letter-spacing:-.015em}
h2{font-weight:600;font-size:clamp(26px,3.4vw,40px);line-height:1.15}
h3{font-weight:700;font-size:clamp(18px,1.6vw,21px);line-height:1.3}
.wrap{max-width:1180px;margin:0 auto;padding:0 clamp(18px,4vw,40px)}
.skip{position:absolute;left:-999px;top:0;background:var(--lime);color:var(--navy);
  padding:10px 16px;font-weight:700;z-index:200;border-radius:0}
.skip:focus{left:0}

/* ── Header ── */
header.site{position:sticky;top:0;z-index:100;background:rgba(255,255,255,.97);
  backdrop-filter:blur(8px);border-bottom:1px solid var(--rule)}
.navrow{display:flex;align-items:center;gap:clamp(12px,1.4vw,16px);min-height:74px}
.brand{display:flex;align-items:center;gap:11px;font-family:var(--font-display);font-weight:800;
  text-transform:uppercase;line-height:1.05;letter-spacing:.01em;
  font-size:clamp(13.5px,1.1vw,17px);color:var(--navy);text-decoration:none;white-space:nowrap}
.brand:hover{text-decoration:none}
.mark{width:38px;height:38px;border-radius:0;background:var(--navy);flex:0 0 38px;
  display:grid;place-items:center}
.brand small{display:block;font-family:var(--font-body);font-weight:600;font-size:9px;
  letter-spacing:.18em;color:var(--muted);text-transform:uppercase;margin-top:3px}
nav.main{margin-left:auto;display:flex;align-items:center;gap:clamp(6px,.8vw,11px)}
nav.main a{color:var(--navy);font-weight:700;font-size:11.5px;text-transform:uppercase;
  letter-spacing:.02em;padding:6px 2px;position:relative;white-space:nowrap}
nav.main a:hover{text-decoration:none;color:var(--blue)}
nav.main a[aria-current="page"]{color:var(--blue)}
nav.main a[aria-current="page"]::after{content:"";position:absolute;left:0;right:0;bottom:-4px;
  height:3px;border-radius:0;background:var(--lime)}
.menu-toggle{display:none;margin-left:auto;background:var(--tint);border:1px solid var(--navy);
  border-radius:0;padding:9px 12px;font:inherit;font-weight:700;text-transform:uppercase;
  letter-spacing:.06em;color:var(--navy);cursor:pointer}
.dropdown{position:relative}
.dropdown>summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:5px}
.dropdown>summary::-webkit-details-marker{display:none}
.dropdown>summary::after{content:"▾";font-size:11px;color:var(--muted)}
.dropdown-menu{position:absolute;top:calc(100% + 10px);left:50%;transform:translateX(-50%);
  background:#fff;border:1px solid var(--rule);border-radius:0;box-shadow:none;
  padding:10px;min-width:300px;display:grid;gap:2px}
.dropdown-menu a{padding:9px 12px;border-radius:0;font-size:13.5px;white-space:nowrap}
.dropdown-menu a:hover{background:var(--tint);text-decoration:none}
.dropdown-menu .all{font-weight:700;color:var(--blue)}
.dropdown-menu .group{font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--muted);padding:8px 12px 2px}
.navcta{display:flex;align-items:center;gap:10px;margin-left:clamp(4px,.8vw,10px)}
.navcta .btn{white-space:nowrap}
.loginlink{font-weight:600;font-size:12px;color:var(--muted)!important;white-space:nowrap}

/* ── Buttons ── */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:9px;font-weight:800;
  font-size:13px;text-transform:uppercase;letter-spacing:.07em;padding:15px 26px;
  border-radius:0;border:2px solid transparent;cursor:pointer;
  font-family:var(--font-body);line-height:1;text-decoration:none;transition:.18s}
.btn:hover{text-decoration:none;transform:translateY(-1px)}
.btn-primary{background:var(--blue);color:#fff}
.btn-primary:hover{background:#0d58d6}
.btn-accent{background:var(--lime);color:var(--navy)}
.btn-accent:hover{background:#d4fb67}
.btn-ghost{border-color:var(--navy);color:var(--navy)}
.btn-ghost:hover{background:var(--navy);border-color:var(--navy);color:#fff}
.btn-outline{border-color:var(--navy);color:var(--navy);background:transparent}
.btn-outline:hover{background:var(--navy);color:#fff}
.btn-sm{padding:9px 13px;font-size:11px}

/* ── Hero ── */
.hero{background:var(--tint);color:var(--ink);border-bottom:1px solid var(--rule);
  padding:clamp(56px,8vw,110px) 0 clamp(52px,7.5vw,96px);position:relative;overflow:hidden}
.hero .eyebrow{color:var(--navy)}
.hero h1{color:var(--navy);max-width:16ch}
.hero p.lead{color:var(--muted);max-width:60ch;font-size:clamp(15.5px,1.3vw,18px)}
.hero .lead+.lead{margin-top:14px}
.hero .cta{display:flex;flex-wrap:wrap;gap:14px;margin-top:32px}
.hero-viz{position:absolute;right:-40px;top:0;bottom:0;width:min(46vw,620px);opacity:.8;
  pointer-events:none}
.crumbs{font-size:12px;color:var(--muted);margin-bottom:20px;letter-spacing:.08em;
  text-transform:uppercase;font-weight:600}
.crumbs a{color:var(--muted)}

/* ── Eyebrow / sections ── */
.eyebrow{display:inline-flex;align-items:center;gap:10px;font-weight:800;font-size:11.5px;
  letter-spacing:.18em;text-transform:uppercase;color:var(--blue);margin-bottom:14px}
.eyebrow::before{content:"";width:26px;height:2px;background:var(--lime)}
section.block{padding:var(--sp-section) 0}
section.tint{background:var(--tint)}
section.dark{background:var(--navy);color:#fff}
section.dark h2,section.dark h3{color:#fff}
section.dark p{color:#C9D8EA}
.sec-head{max-width:720px;margin-bottom:clamp(30px,4.5vw,52px)}
.sec-head p.intro{margin-top:14px;color:var(--muted);font-size:clamp(15px,1.2vw,17px)}
section.dark .sec-head p.intro{color:#C9D8EA}

/* ── Grids & cards: joined hairline-ruled cells ── */
.grid{display:grid;gap:clamp(18px,2.2vw,28px)}
.grid.g2,.grid.g3,.grid.g4{gap:1px;background:var(--rule);border:1px solid var(--rule)}
.grid.g2>*,.grid.g3>*,.grid.g4>*{background:var(--sheet);border:0;border-radius:0;box-shadow:none}
.g2{grid-template-columns:repeat(2,1fr)}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(2,1fr)}
.card{background:var(--sheet);border:1px solid var(--rule);border-radius:0;box-shadow:none;
  padding:clamp(22px,2.4vw,32px);display:flex;flex-direction:column;gap:13px}
.card .num{font-family:var(--font-display);font-weight:800;font-size:clamp(26px,3vw,34px);
  line-height:1;color:var(--navy);background:none;width:auto;height:auto;
  display:inline-flex;align-items:baseline;gap:8px}
.card .num::after{content:"";width:var(--mark);height:var(--mark);background:var(--lime);flex:0 0 auto}
.card h3{font-size:clamp(17px,1.5vw,20px)}
.card p{color:var(--muted);font-size:15px}
.card .tagline{font-weight:700;color:var(--ink);font-size:14.5px}
.cardlink{margin-top:auto;font-weight:700;font-size:12.5px;text-transform:uppercase;
  letter-spacing:.06em;color:var(--blue);display:inline-flex;gap:7px;align-items:center}
.cardlink::after{content:"→";transition:.18s}
.cardlink:hover{text-decoration:none;gap:11px}
.dark .grid.g2,.dark .grid.g3,.dark .grid.g4{background:rgba(195,248,74,.4);border-color:rgba(195,248,74,.4)}
.dark .grid.g2>*,.dark .grid.g3>*,.dark .grid.g4>*{background:transparent}
.on-dark .card{background:rgba(255,255,255,.04);border:1px solid rgba(195,248,74,.4);box-shadow:none}
.on-dark .card h3{color:#fff}
.on-dark .card p{color:#B9C9DD}
.on-dark .card .num{color:#fff}

/* ── Lists ── */
ul.check{list-style:none;display:grid;gap:12px}
ul.check li{padding-left:30px;position:relative;color:var(--ink)}
ul.check li::before{content:"";position:absolute;left:0;top:6px;width:15px;height:15px;
  border-radius:1px;background:var(--lime);
  -webkit-mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='3.4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M4 12l6 6L21 6'/%3E%3C/svg%3E") center/12px no-repeat, linear-gradient(#000,#000);
  -webkit-mask-composite:source-over;mask-composite:add}
ol.steps{list-style:none;counter-reset:st;display:grid;gap:20px}
ol.steps li{counter-increment:st;display:flex;gap:18px;align-items:flex-start}
ol.steps li::before{content:counter(st,decimal-leading-zero);font-family:var(--font-display);
  font-weight:800;font-size:clamp(22px,2.4vw,30px);line-height:1;color:var(--navy);
  background:none;border:0;border-radius:0;min-width:58px;height:auto;
  display:block;flex:0 0 auto;padding-top:2px}
ol.steps li strong{display:block;margin-bottom:3px}

/* ── Feature split ── */
.split{display:grid;grid-template-columns:1.1fr 1fr;gap:clamp(26px,4vw,60px);align-items:center}
.stat-row{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:34px}
.stat{background:transparent;border:0;border-top:2px solid var(--rule);border-radius:0;
  padding:16px 4px 0 0}
.stat b{font-family:var(--font-display);font-weight:800;font-size:clamp(24px,2.6vw,36px);
  color:var(--lime);display:block}
.stat span{font-size:12px;color:#B9C9DD;letter-spacing:.08em;text-transform:uppercase;font-weight:600}

/* ── Callouts ── */
.callout{border-left:4px solid var(--blue);background:var(--tint);border-radius:0;
  padding:20px 24px;color:var(--ink)}
.callout.lime{border-color:var(--lime);background:#F6FCEE}
.callout h3{font-size:15px;margin-bottom:8px;font-family:var(--font-body);
  letter-spacing:.04em;text-transform:uppercase}
.callout p{font-size:14.5px;color:var(--muted)}
.callout p+p{margin-top:8px}

/* ── CTA band ── */
.cta-band{background:var(--lime);color:var(--navy);border-radius:0;box-shadow:none;
  padding:clamp(34px,5vw,60px);display:grid;grid-template-columns:1.4fr auto;
  gap:clamp(20px,3vw,44px);align-items:center}
.cta-band h2{color:var(--navy);font-weight:800;text-transform:uppercase;
  font-size:clamp(24px,3.2vw,38px);line-height:1.02;max-width:22ch}
.cta-band p{color:var(--navy);margin-top:12px;max-width:56ch;opacity:.85}
.cta-band .cta{display:flex;flex-direction:column;gap:12px;min-width:250px}
.cta-band .btn-accent{background:var(--navy);color:#fff}
.cta-band .btn-accent:hover{background:#0F1E35}
.cta-band .btn-outline,.cta-band .btn-ghost{border-color:var(--navy);color:var(--navy)}
.cta-band .btn-outline:hover,.cta-band .btn-ghost:hover{background:var(--navy);color:#fff;border-color:var(--navy)}

/* ── Service / division page pieces ── */
.pagehero{background:var(--tint);color:var(--ink);border-bottom:1px solid var(--rule);
  padding:clamp(52px,7vw,92px) 0}
.pagehero h1{color:var(--navy);max-width:18ch}
.pagehero p.lead{color:var(--muted);max-width:62ch;margin:18px 0 0;font-size:clamp(15px,1.25vw,17.5px)}
.pagehero .eyebrow{color:var(--blue)}
.pagetags{display:flex;flex-wrap:wrap;gap:10px;margin-top:26px}
.pagetags span{background:transparent;border:1px solid var(--navy);color:var(--navy);
  font-size:11.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;
  padding:7px 13px;border-radius:0}
.divlabel{font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;font-weight:800;
  color:var(--navy);margin-bottom:10px;display:flex;gap:10px;align-items:center}
.divlabel::before{content:"";width:22px;height:2px;background:var(--lime)}
.svc-list{display:grid;gap:1px;background:var(--rule);border:1px solid var(--rule)}
.svc-item{display:grid;grid-template-columns:72px 1fr auto;gap:18px;align-items:center;
  background:var(--sheet);border:0;border-radius:0;box-shadow:none;padding:24px 26px}
.svc-item .num{font-family:var(--font-display);font-weight:800;color:var(--navy);background:none;
  border-radius:0;width:auto;height:auto;display:inline-flex;align-items:baseline;gap:8px;
  font-size:clamp(22px,2.4vw,30px);line-height:1}
.svc-item .num::after{content:"";width:var(--mark);height:var(--mark);background:var(--lime);flex:0 0 auto}
.svc-item h3{font-size:clamp(16.5px,1.5vw,19px)}
.svc-item p{color:var(--muted);font-size:14px;margin-top:4px}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,3.4vw,48px)}
.panel{background:var(--sheet);border:1px solid var(--rule);border-radius:0;box-shadow:none;
  padding:clamp(22px,2.6vw,34px)}
.panel h3{margin-bottom:14px}
.panel .kicker{font-size:11px;letter-spacing:.15em;text-transform:uppercase;font-weight:800;
  color:var(--blue);margin-bottom:8px}
.contact-grid{display:grid;grid-template-columns:1.35fr 1fr;gap:clamp(24px,3.4vw,48px)}
@media (max-width:1020px){.contact-grid{grid-template-columns:1fr}}

/* ── FAQ ── */
details.faq{background:var(--sheet);border:0;border-bottom:1px solid var(--rule);
  padding:0;margin-bottom:0;overflow:hidden}
.faq-group details.faq:first-of-type{border-top:1px solid var(--rule)}
details.faq summary{cursor:pointer;font-weight:700;color:var(--navy);
  padding:18px 20px;display:flex;justify-content:space-between;gap:14px;font-size:15px;list-style:none}
details.faq summary::-webkit-details-marker{display:none}
details.faq summary::after{content:"+";font-family:var(--font-display);font-weight:800;
  font-size:22px;color:var(--blue);flex:0 0 auto}
details.faq[open] summary::after{content:"–"}
details.faq .a{padding:0 20px 20px;color:var(--muted);font-size:14.5px}
.faq-group{margin-bottom:34px}
.faq-group h2{font-size:clamp(19px,2vw,25px);margin-bottom:16px}

/* ── Forms ── */
form.enquiry{display:grid;gap:18px}
.frow{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.field{display:grid;gap:7px}
.field label{font-weight:700;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--navy)}
.field label .opt{color:var(--muted);font-weight:500;text-transform:none;letter-spacing:0}
.field input,.field select,.field textarea{font:inherit;font-size:14.5px;color:var(--ink);
  padding:13px 14px;border:1.5px solid var(--line);border-radius:0;background:#fff;width:100%}
.field textarea{min-height:130px;resize:vertical}
.field input:focus,.field select:focus,.field textarea:focus{outline:2px solid var(--blue);
  outline-offset:1px;border-color:var(--blue)}
.field.err input,.field.err select,.field.err textarea{border-color:#D64545;background:#FFF7F7}
.field .msg{display:none;color:#C03A3A;font-size:12.5px;font-weight:600}
.field.err .msg{display:block}
fieldset.radio{border:1.5px solid var(--line);border-radius:0;padding:14px 16px}
fieldset.radio legend{font-weight:700;font-size:12px;letter-spacing:.06em;text-transform:uppercase;
  color:var(--navy);padding:0 6px}
fieldset.radio label{display:flex;gap:9px;align-items:center;font-size:14px;padding:5px 0;color:var(--ink)}
.consent{display:flex;gap:10px;align-items:flex-start;font-size:13.5px;color:var(--muted)}
.consent input{width:18px;height:18px;flex:0 0 18px;margin-top:2px;accent-color:var(--blue)}
.form-note{font-size:12.5px;color:var(--muted)}
.confirm{display:none;background:#F6FCEE;border:1.5px solid #A6E22E;border-radius:0;
  padding:24px 26px;gap:10px}
.confirm.show{display:grid}
.confirm h3{color:var(--navy)}
.confirm p{color:#3E5A34;font-size:14.5px}
.error-summary{display:none;background:#FFF3F3;border:1.5px solid #D64545;border-radius:0;
  padding:16px 20px;color:#8F2B2B;font-size:14px;font-weight:600}
.error-summary.show{display:block}

/* ── Empty states / notices ── */
.empty{background:var(--sheet);border:1.5px dashed var(--blue);border-radius:0;
  padding:clamp(30px,4vw,54px);text-align:center;max-width:680px;margin:0 auto}
.empty .icon{width:52px;height:52px;border-radius:0;background:var(--tint);
  display:grid;place-items:center;margin:0 auto 16px}
.empty h3{margin-bottom:10px}
.empty p{color:var(--muted);font-size:14.5px;max-width:46ch;margin:0 auto 6px}
.notice{background:#FFF8E8;border:1.5px solid #E4C55B;border-radius:0;
  padding:18px 22px;font-size:14px;color:#6B5416}
.notice strong{color:#594509}

/* ── Tables ── */
.tblwrap{overflow-x:auto;border:1px solid var(--rule);border-radius:0;background:var(--sheet)}
table.data{width:100%;border-collapse:collapse;font-size:14px;min-width:520px}
table.data th{background:var(--navy);color:#fff;text-align:left;padding:13px 16px;
  font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;font-weight:700}
table.data td{padding:12px 16px;border-top:1px solid var(--line);color:var(--ink);vertical-align:top}

/* ── Footer ── */
footer.site{background:var(--navy);color:#B9C9DD;margin-top:clamp(56px,8vw,100px);
  border-top:2px solid var(--rule)}
footer.site .top{display:grid;grid-template-columns:1.5fr 1fr 1.2fr 1.2fr;
  gap:clamp(24px,3.4vw,48px);padding:clamp(44px,6vw,72px) 0 34px}
footer.site h4{color:#fff;font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;
  font-family:var(--font-body);font-weight:800;margin-bottom:16px}
footer.site .fbrand{font-family:var(--font-display);color:#fff;font-weight:800;
  text-transform:uppercase;font-size:19px;margin-bottom:12px}
footer.site .fsub{font-size:13px;letter-spacing:.05em;color:var(--lime);font-weight:600;margin-bottom:14px}
footer.site p{font-size:14px;max-width:40ch}
footer.site ul{list-style:none;display:grid;gap:9px}
footer.site ul a{color:#B9C9DD;font-size:13.5px}
footer.site ul a:hover{color:var(--lime);text-decoration:none}
footer.site .base{border-top:1px solid rgba(255,255,255,.14);padding:20px 0 26px;
  display:flex;flex-wrap:wrap;gap:10px;justify-content:space-between;font-size:12.5px;color:#8FA2BC}

/* ── Breadcrumb-ish intro for sub pages ── */
.paper{background:var(--sheet);border:1px solid var(--line);border-radius:0;box-shadow:none;
  padding:clamp(24px,3vw,44px)}
.paper h2{margin-bottom:14px}
.paper p+p{margin-top:10px}
.paper .lede{font-size:clamp(15.5px,1.25vw,17.5px);color:var(--ink)}

/* ── Reveal animation ── */
.no-js .rise{opacity:1;transform:none}
@media (prefers-reduced-motion:no-preference){
  .js .rise{opacity:0;transform:translateY(14px);transition:.6s ease}
  .js .rise.in{opacity:1;transform:none}
}

/* ── Responsive ── */
@media (min-width:1181px) and (max-width:1400px){
  .loginlink{display:none}
}
@media (max-width:1020px){
  .two-col,.split{grid-template-columns:1fr}
  footer.site .top{grid-template-columns:1fr 1fr}
  .g4{grid-template-columns:1fr 1fr}
}
@media (max-width:1180px){
  .g3{grid-template-columns:1fr 1fr}
  .stat-row{gap:14px}
  .stat{padding:14px 16px}
  .stat b{font-size:clamp(19px,3vw,26px)}
}
@media (max-width:1180px){
  .menu-toggle{display:inline-flex}
  nav.main{display:none;position:absolute;top:72px;left:0;right:0;background:#fff;
    border-bottom:1px solid var(--line);flex-direction:column;align-items:stretch;
    padding:14px clamp(18px,4vw,40px) 24px;gap:6px;box-shadow:var(--shadow)}
  nav.main.open{display:flex}
  nav.main a{padding:12px 4px;font-size:15px}
  nav.main a[aria-current="page"]::after{bottom:2px}
  .dropdown-menu{position:static;transform:none;box-shadow:none;border:none;padding:0 0 4px 14px}
  .navcta{flex-direction:column;align-items:stretch;margin-left:0;gap:8px}
  .hero-viz{display:none}
}
@media (max-width:720px){
  .stat-row{grid-template-columns:1fr}
}
@media (max-width:640px){
  .g2,.g3,.g4,.frow{grid-template-columns:1fr}
  .cta-band{grid-template-columns:1fr}
  .cta-band .cta{flex-direction:row;flex-wrap:wrap}
  footer.site .top{grid-template-columns:1fr;gap:30px}
  .svc-item{grid-template-columns:1fr;gap:12px}
  .svc-item .num{width:auto;height:auto}
  section.block{padding:clamp(44px,10vw,60px) 0}
  .pagehero{padding:clamp(44px,9vw,60px) 0}
  .hero{padding:clamp(52px,11vw,72px) 0 clamp(48px,10vw,64px)}
  .crumbs{margin-bottom:16px}
}
@media (max-width:400px){
  .brand small{display:none}
  .wrap{padding:0 16px}
}
"""

# ═══════════════════════════════ JS ═══════════════════════════════
JS = r"""
(function(){
  // Mobile menu
  var t=document.querySelector(".menu-toggle"),nav=document.querySelector("nav.main");
  if(t&&nav){t.addEventListener("click",function(){
    var open=nav.classList.toggle("open");
    t.setAttribute("aria-expanded",open?"true":"false");})}
  // Dropdown (works on touch via <details>)
  document.querySelectorAll("details.dropdown").forEach(function(d){
    d.addEventListener("click",function(e){
      if(d.open&&e.target.closest("a"))d.removeAttribute("open");});
    document.addEventListener("click",function(e){
      if(d.open&&!d.contains(e.target))d.removeAttribute("open");});});
  // Year stamp
  document.querySelectorAll("[data-year]").forEach(function(el){
    el.textContent=new Date().getFullYear();});
  // Scroll reveal
  if("IntersectionObserver" in window){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(en){if(en.isIntersecting){en.target.classList.add("in");io.unobserve(en.target);}});
    },{threshold:.12});
    document.querySelectorAll(".rise").forEach(function(el){io.observe(el);});
  }else{document.querySelectorAll(".rise").forEach(function(el){el.classList.add("in");});}
  // Enquiry form validation
  var form=document.querySelector("form.enquiry");
  if(form){
    var summary=form.querySelector(".error-summary");
    var confirm=form.querySelector(".confirm");
    function need(el,msg){
      var f=el.closest(".field")||el.closest("fieldset");
      if(!f)return true;
      var m=f.querySelector(".msg");
      var bad=!el.value||(el.type==="checkbox"&&!el.checked)||
        (el.tagName==="SELECT"&&!el.value);
      f.classList.toggle("err",bad);
      if(m&&bad)m.textContent=msg||"This field is required.";
      return !bad;
    }
    form.addEventListener("submit",function(e){
      e.preventDefault();
      var ok=true,first=null;
      form.querySelectorAll("[data-req]").forEach(function(el){
        var good=need(el);
        if(!good){ok=false;first=first||el;}
      });
      var email=form.querySelector("input[type=email]");
      if(email&&email.value&&!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)){
        var f=email.closest(".field");f.classList.add("err");
        var m=f.querySelector(".msg");if(m)m.textContent="Please enter a valid email address.";
        ok=false;first=first||email;
      }
      if(summary){summary.classList.toggle("show",!ok);
        if(!ok&&first){first.focus();return;}}
      if(ok){form.style.display="none";if(confirm){confirm.classList.add("show");
        confirm.scrollIntoView({behavior:"smooth",block:"center"});}}
    });
  }
  // Portal stub forms
  var stub=document.querySelector("form.portal-stub");
  if(stub){stub.addEventListener("submit",function(e){
    e.preventDefault();
    var n=stub.querySelector(".portal-note");
    if(n)n.style.display="block";});}
})();
"""

# ═══════════════════════════════ Shared chrome ═══════════════════════════════
LOGO_SVG = """<span class="mark" aria-hidden="true">
<svg width="20" height="20" viewBox="0 0 24 24" fill="none">
<path d="M4 19V11M9.5 19V5M15 19v-6M20 19v-9" stroke="#C3F84A" stroke-width="2.6"
 stroke-linecap="round"/></svg></span>"""

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("services.html", "Services"),
    ("research-publications.html", "Research Publications"),
    ("insights.html", "Insights"),
    ("contact.html", "Contact"),
]

def header(active, with_drop=False):
    links = []
    for f, label in NAV:
        cur = ' aria-current="page"' if f == active else ""
        if f == "services.html" and with_drop:
            links.append(
                f'<details class="dropdown"><summary aria-current="page"><a href="services.html"{cur}>Services</a></summary>'
                f'<div class="dropdown-menu">'
                f'<span class="group">Divisions</span>'
                f'<a href="business-intelligence-performance-analytics.html">01 · Business Intelligence &amp; Performance Analytics</a>'
                f'<a href="economic-commercial-intelligence.html">02 · Economic &amp; Commercial Intelligence</a>'
                f'<a href="operational-risk-process-controls.html">03 · Operational Risk, Process &amp; Controls</a>'
                f'<span class="group">Popular services</span>'
                f'<a href="business-data-diagnostic.html">Business Data Diagnostic</a>'
                f'<a href="competitor-intelligence-snapshot.html">Competitor Intelligence Snapshot</a>'
                f'<a href="operational-risk-register.html">Operational Risk Register</a>'
                f'</div></details>')
        else:
            links.append(f'<a href="{f}"{cur}>{label}</a>')
    return f"""<header class="site">
  <a class="skip" href="#main">Skip to content</a>
  <div class="wrap navrow">
    <a class="brand" href="index.html">{LOGO_SVG}
      <span>{COMPANY_NAME}<small>Business Advisory · Intelligence · Research</small></span></a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="mainnav">Menu</button>
    <nav class="main" id="mainnav" aria-label="Main navigation">
      {''.join(links)}
      <div class="navcta">
        <a class="btn btn-primary btn-sm" href="contact.html">Discuss Your Business Needs</a>
        <a class="loginlink" href="client-portal.html">Client Login</a>
      </div>
    </nav>
  </div>
</header>"""

def footer():
    return f"""<footer class="site">
  <div class="wrap">
    <div class="top">
      <div>
        <div class="fbrand">{COMPANY_NAME}</div>
        <div class="fsub">Business Advisory | Business Intelligence | Research &amp; Analysis</div>
        <p>We help businesses understand their performance, evaluate commercial opportunities and
           strengthen the processes and controls that support their operations.</p>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="about.html">About Us</a></li>
          <li><a href="services.html">Our Services</a></li>
          <li><a href="research-publications.html">Research Publications</a></li>
          <li><a href="insights.html">Insights</a></li>
          <li><a href="contact.html">Contact Us</a></li>
        </ul>
      </div>
      <div>
        <h4>Our Services</h4>
        <ul>
          <li><a href="business-intelligence-performance-analytics.html">Business Intelligence &amp; Performance Analytics</a></li>
          <li><a href="economic-commercial-intelligence.html">Economic &amp; Commercial Intelligence</a></li>
          <li><a href="operational-risk-process-controls.html">Operational Risk, Process &amp; Controls Advisory</a></li>
        </ul>
      </div>
      <div>
        <h4>Information</h4>
        <ul>
          <li><a href="faq.html">Frequently Asked Questions</a></li>
          <li><a href="privacy-policy.html">Privacy Policy</a></li>
          <li><a href="website-terms.html">Website Terms &amp; Conditions</a></li>
          <li><a href="client-service-terms.html">Client Service Terms</a></li>
          <li><a href="publication-licence.html">Research Publication Licence</a></li>
          <li><a href="refund-policy.html">Digital Product Refund &amp; Cancellation Policy</a></li>
        </ul>
        <h4 style="margin-top:22px">Contact</h4>
        <ul>
          <li><a href="mailto:{COMPANY_EMAIL}">Email: {COMPANY_EMAIL}</a></li>
          <li>Telephone: {COMPANY_PHONE}</li>
          <li>Operating coverage: South Africa</li>
        </ul>
      </div>
    </div>
    <div class="base">
      <span>© <span data-year>{YEAR}</span> {COMPANY_NAME}. All rights reserved.</span>
      <span>Business Advisory · South Africa</span>
    </div>
  </div>
</footer>"""

def shell(fname, title, desc, body, active, with_drop=False, extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="en-ZA" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>document.documentElement.classList.replace("no-js","js")</script>
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE_URL}{fname if fname != 'index.html' else ''}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
{extra_head}
</head>
<body>
<div class="sheet">
{header(active, with_drop)}
<main id="main">
{body}
</main>
{footer()}
</div>
<script src="assets/site.js"></script>
</body>
</html>"""

def hero_home():
    viz = """<svg class="hero-viz" viewBox="0 0 560 420" fill="none" aria-hidden="true">
  <g stroke="rgba(21,38,65,.12)"><path d="M0 90h560M0 170h560M0 250h560M0 330h560"/></g>
  <path d="M20 350 L120 300 L220 315 L320 240 L420 200 L520 120" stroke="#C3F84A" stroke-width="3" stroke-linecap="round"/>
  <path d="M20 380 L120 360 L220 340 L320 320 L420 290 L520 250" stroke="rgba(19,108,252,.85)" stroke-width="2.6" stroke-linecap="round"/>
  <g fill="#C3F84A"><circle cx="120" cy="300" r="5"/><circle cx="320" cy="240" r="5"/><circle cx="520" cy="120" r="5"/></g>
  <g fill="rgba(19,108,252,.7)"><circle cx="220" cy="340" r="4"/><circle cx="420" cy="290" r="4"/></g>
  <g stroke="rgba(21,38,65,.18)"><path d="M20 350v30M120 300v80M220 315v65M320 240v140M420 200v180M520 120v260"/></g>
</svg>"""
    return f"""<section class="hero">
  {viz}
  <div class="wrap" style="position:relative">
    <span class="eyebrow">Business Advisory | Intelligence | Research</span>
    <h1>Better business decisions begin with better information.</h1>
    <p class="lead">Businesses make decisions every day about performance, pricing, markets,
    operations and growth. The quality of those decisions depends on how well the underlying
    information is understood.</p>
    <p class="lead">{COMPANY_NAME} provides business intelligence,
    economic and commercial research, performance analysis and operational advisory services
    to help businesses make more informed decisions.</p>
    <div class="cta">
      <a class="btn btn-accent" href="contact.html">Discuss Your Business Needs</a>
      <a class="btn btn-outline" href="services.html">Explore Our Services</a>
    </div>
  </div>
</section>"""

def cta_band(title, text, primary, secondary=None, primary_href="contact.html", secondary_href="services.html"):
    sec = f'<a class="btn btn-outline" href="{secondary_href}">{secondary}</a>' if secondary else ""
    return f"""<section class="block"><div class="wrap">
  <div class="cta-band rise">
    <div><h2>{title}</h2><p>{text}</p></div>
    <div class="cta"><a class="btn btn-accent" href="{primary_href}">{primary}</a>{sec}</div>
  </div>
</div></section>"""

def pagehero(eyebrow, title, lead=None, crumbs=None, tags=None):
    c = f'<div class="crumbs"><a href="index.html">Home</a> / {crumbs}</div>' if crumbs else ""
    t = ""
    if tags:
        t = '<div class="pagetags">' + "".join(f"<span>{x}</span>" for x in tags) + "</div>"
    lead_html = f'<p class="lead">{lead}</p>' if lead else ""
    return f"""<section class="pagehero"><div class="wrap">
  {c}
  <span class="eyebrow">{eyebrow}</span>
  <h1>{title}</h1>
  {lead_html}{t}
</div></section>"""

# ═══════════════════════════════ PAGES ═══════════════════════════════
PAGES = {}   # filename -> (title, description, body_html, active_nav)

def add(fname, title, desc, body, active=None, extra_head=""):
    PAGES[fname] = (title, desc, body, active if active else fname, extra_head)

# ─────────────────────────── HOMEPAGE ───────────────────────────
add("index.html",
    f"{COMPANY_NAME} | Business Advisory Firm South Africa",
    "Business intelligence, economic and commercial research, performance analytics and "
    "operational risk advisory services for businesses across South Africa.",
    hero_home() + f"""

<section class="block"><div class="wrap">
  <div class="split rise">
    <div>
      <span class="eyebrow">What we do</span>
      <h2>We turn business information into practical insight.</h2>
      <p style="color:var(--muted);margin-top:16px">Information is valuable when it helps a
      business understand what is happening, why it matters and what should be considered next.</p>
    </div>
    <div class="panel">
      <p style="font-weight:700;color:var(--navy);margin-bottom:14px">Our work focuses on three
      connected areas:</p>
      <ol class="steps">
        <li><strong>Understand performance</strong>
          We examine business records, operational information and performance indicators to
          help businesses understand trends, identify gaps and monitor results.</li>
        <li><strong>Evaluate the commercial environment</strong>
          We investigate competitors, pricing, suppliers, market conditions and relevant economic
          developments to support commercial decision-making.</li>
        <li><strong>Strengthen business operations</strong>
          We examine processes, operational risks and internal controls to identify weaknesses
          and recommend practical improvements.</li>
      </ol>
    </div>
  </div>
  <p class="rise" style="margin-top:26px;color:var(--muted);max-width:70ch">Our approach is
  evidence-based, structured and focused on producing useful outputs rather than information
  for its own sake.</p>
</div></section>

<section class="block tint"><div class="wrap">
  <div class="sec-head rise">
    <span class="eyebrow">Our business units</span>
    <h2>Four capabilities. One connected advisory approach.</h2>
  </div>
  <div class="grid g2">
    <div class="card rise"><span class="num">01</span>
      <h3>Business Intelligence &amp; Performance Analytics</h3>
      <p class="tagline">Understand the numbers behind your business.</p>
      <p>We help businesses organise and analyse internal information, monitor key performance
      indicators and develop reporting tools that make business performance easier to understand.</p>
      <a class="cardlink" href="business-intelligence-performance-analytics.html">Explore Business Intelligence</a>
    </div>
    <div class="card rise"><span class="num">02</span>
      <h3>Economic &amp; Commercial Intelligence</h3>
      <p class="tagline">Understand the market in which you operate.</p>
      <p>We research competitors, pricing, suppliers, market conditions and commercial developments
      to help businesses assess their position and evaluate opportunities.</p>
      <a class="cardlink" href="economic-commercial-intelligence.html">Explore Economic &amp; Commercial Intelligence</a>
    </div>
    <div class="card rise"><span class="num">03</span>
      <h3>Operational Risk, Process &amp; Controls Advisory</h3>
      <p class="tagline">Understand the weaknesses that affect your operations.</p>
      <p>We examine business processes, operational risks, documentation and internal controls,
      helping businesses identify gaps and establish more structured ways of working.</p>
      <a class="cardlink" href="operational-risk-process-controls.html">Explore Operational Risk Advisory</a>
    </div>
    <div class="card rise"><span class="num">04</span>
      <h3>Research Publications &amp; Intelligence Products</h3>
      <p class="tagline">Access research without commissioning a project.</p>
      <p>Our research publications provide structured analysis of selected economic, industry and
      commercial topics. Publications are developed independently and made available for purchase
      through our website.</p>
      <a class="cardlink" href="research-publications.html">Browse Research Publications</a>
    </div>
  </div>
</div></section>

<section class="block"><div class="wrap">
  <div class="sec-head rise">
    <span class="eyebrow">Who we support</span>
    <h2>Advisory for businesses that want to operate with greater clarity.</h2>
    <p class="intro">Our services are designed for businesses that need a clearer understanding
    of their performance, commercial environment or internal operations.</p>
  </div>
  <div class="two-col rise">
    <ul class="check">
      <li>Established micro and small businesses.</li>
      <li>Growing small and medium-sized enterprises.</li>
      <li>Businesses preparing for expansion or operational change.</li>
    </ul>
    <ul class="check">
      <li>Businesses seeking better management information and reporting.</li>
      <li>Businesses reviewing costs, pricing or commercial opportunities.</li>
      <li>Organisations requiring structured research and analytical support.</li>
    </ul>
  </div>
  <p style="margin-top:26px;color:var(--muted);max-width:74ch">We work with clients across South
  Africa, with engagements delivered remotely, through a hybrid arrangement or at client premises
  where the assignment requires it.</p>
</div></section>

<section class="block tint"><div class="wrap">
  <div class="sec-head rise">
    <span class="eyebrow">How we work</span>
    <h2>Clear questions. Reliable evidence. Useful recommendations.</h2>
    <p class="intro">We approach each assignment through a structured process.</p>
  </div>
  <ol class="steps rise" style="max-width:820px">
    <li><strong>Understand</strong> We establish the business question, the client's requirements
      and the information needed to undertake the work.</li>
    <li><strong>Examine</strong> We review relevant records, data, processes, market information
      or other appropriate evidence.</li>
    <li><strong>Analyse</strong> We organise and assess the information using methods appropriate
      to the assignment.</li>
    <li><strong>Explain</strong> We present the findings in clear, structured documentation,
      highlighting relevant observations, implications and limitations.</li>
    <li><strong>Recommend</strong> Where appropriate, we provide practical recommendations and
      suggested next steps.</li>
  </ol>
  <p style="margin-top:26px;color:var(--muted)">Every assignment is scoped according to its
  purpose, complexity and available evidence.</p>
</div></section>

<section class="block dark on-dark"><div class="wrap">
  <div class="split rise">
    <div>
      <span class="eyebrow" style="color:var(--lime)">Research &amp; intelligence products</span>
      <h2>Research you can access when you need it.</h2>
      <p style="margin-top:16px">Our publications provide researched and structured information
      on selected economic, industry and commercial topics.</p>
      <p style="margin-top:12px">Developed independently by our research team, these products are
      available to businesses, professionals, researchers and other interested users.</p>
      <p style="margin-top:12px">Explore reports, industry analysis, economic briefs and
      data-focused publications.</p>
    </div>
    <div class="card">
      <span class="num">04</span>
      <h3>Research Publications &amp; Intelligence Products</h3>
      <p>Industry performance reports · Economic research reports · Market &amp; commercial
      intelligence · Statistical publications &amp; data products · Intelligence briefs</p>
      <a class="cardlink" href="research-publications.html" style="color:var(--lime)">Explore Research Publications</a>
    </div>
  </div>
</div></section>

<section class="block"><div class="wrap">
  <div class="sec-head rise">
    <span class="eyebrow">Our approach</span>
    <h2>Analysis should be useful beyond the report.</h2>
    <p class="intro">We believe good advisory work should do more than present information. It
    should help a business understand its position, recognise relevant issues and consider its
    available options.</p>
  </div>
  <div class="grid g2 rise">
    <div class="panel"><h3>What our approach is built around</h3>
      <ul class="check">
        <li><strong>Evidence-led work:</strong> findings are based on relevant information and
        identifiable sources.</li>
        <li><strong>Clear documentation:</strong> clients receive structured written outputs
        explaining the work performed and its findings.</li>
        <li><strong>Defined scope:</strong> each engagement has an agreed purpose, scope and set
        of deliverables.</li>
        <li><strong>Practical recommendations:</strong> where appropriate, analysis is translated
        into useful business considerations and action points.</li>
        <li><strong>Flexible delivery:</strong> work can be undertaken remotely or through agreed
        on-site arrangements.</li>
        <li><strong>Professional standards:</strong> confidentiality, accuracy, transparency and
        appropriate review are central to our work.</li>
      </ul>
    </div>
    <div class="panel" style="display:flex;flex-direction:column;justify-content:center">
      <div class="stat-row" style="margin-top:0">
        <div class="stat" style="background:var(--tint);border-color:var(--line)">
          <b style="color:var(--blue)">3</b><span style="color:var(--muted)">Specialist advisory divisions</span></div>
        <div class="stat" style="background:var(--tint);border-color:var(--line)">
          <b style="color:var(--blue)">9</b><span style="color:var(--muted)">Structured service packages</span></div>
        <div class="stat" style="background:var(--tint);border-color:var(--line)">
          <b style="color:var(--blue)">ZA</b><span style="color:var(--muted)">Serving clients across South Africa</span></div>
      </div>
      <p style="margin-top:22px;color:var(--muted);font-size:14.5px">These counts describe our
      published service catalogue — not client claims. We do not display client statistics or
      testimonials on this site.</p>
    </div>
  </div>
</div></section>

""" + cta_band("Make your next business decision with greater clarity.",
    "Whether you need to understand your business performance, investigate a commercial question "
    "or examine an operational challenge, we can help you define the work required.",
    "Discuss Your Business Needs", "View Our Services"))

# ─────────────────────────── ABOUT ───────────────────────────
add("about.html",
    f"About {COMPANY_NAME} | Business Advisory &amp; Research",
    "A South African business advisory firm providing business intelligence, economic and "
    "commercial research, performance analysis and operational risk advisory services.",
    pagehero("About " + COMPANY_NAME,
             "Independent thinking. Structured analysis. Practical business insight.",
             f"{COMPANY_NAME} is a South African Business Advisory Firm providing business "
             "intelligence, economic and commercial research, performance analysis and operational "
             "risk advisory services. We help businesses examine information, understand relevant "
             "challenges and make more informed commercial and operational decisions.") + f"""

<section class="block"><div class="wrap">
  <div class="paper rise">
    <span class="eyebrow">Our purpose</span>
    <h2>Making business information more useful.</h2>
    <p class="lede">Businesses generate and encounter significant amounts of information. However,
    having information does not automatically mean that a business understands its performance, its
    market position or the risks affecting its operations.</p>
    <p>Our purpose is to help bridge that gap.</p>
    <p>We undertake structured research, analysis and advisory assignments that turn relevant
    information into clearer findings, better reporting and practical business considerations.</p>
  </div>
</div></section>

<section class="block tint"><div class="wrap">
  <div class="sec-head rise">
    <span class="eyebrow">What we do</span>
    <h2>Three specialist advisory divisions and a research publications business unit.</h2>
  </div>
  <div class="grid g2">
    <div class="card rise"><span class="num">01</span>
      <h3>Business Intelligence &amp; Performance Analytics</h3>
      <p>We work with internal business information to assess performance, develop reporting tools
      and improve management visibility.</p>
      <a class="cardlink" href="business-intelligence-performance-analytics.html">Explore this division</a></div>
    <div class="card rise"><span class="num">02</span>
      <h3>Economic &amp; Commercial Intelligence</h3>
      <p>We examine external commercial conditions, competitors, suppliers, pricing and relevant
      economic developments.</p>
      <a class="cardlink" href="economic-commercial-intelligence.html">Explore this division</a></div>
    <div class="card rise"><span class="num">03</span>
      <h3>Operational Risk, Process &amp; Controls Advisory</h3>
      <p>We review business processes, operational risks, documentation and controls to identify
      weaknesses and recommend improvements.</p>
      <a class="cardlink" href="operational-risk-process-controls.html">Explore this division</a></div>
    <div class="card rise"><span class="num">04</span>
      <h3>Research Publications &amp; Intelligence Products</h3>
      <p>We independently produce research publications and data-focused products for customers who
      want access to structured analysis without commissioning an individual assignment.</p>
      <a class="cardlink" href="research-publications.html">Browse publications</a></div>
  </div>
</div></section>

<section class="block"><div class="wrap">
  <div class="sec-head rise">
    <span class="eyebrow">Our approach to advisory work</span>
    <h2>Sound business advice begins with a properly understood question.</h2>
    <p class="intro">Before undertaking an assignment, we establish what the client needs to
    understand, what information is available, what work is appropriate and what the final output
    should achieve.</p>
  </div>
  <div class="grid g2 rise" style="max-width:1020px">
    <div class="panel"><h3>Our five guiding principles</h3>
      <ol class="steps">
        <li><strong>Evidence before assumption</strong> We distinguish between verified
        information, interpretation, estimates and matters that cannot be established from the
        available evidence.</li>
        <li><strong>Clarity over complexity</strong> We aim to make findings understandable and
        relevant to the people who need to use them.</li>
        <li><strong>Defined professional boundaries</strong> We communicate the scope of our work
        and do not present advisory outputs as legal opinions, statutory audits, accounting
        assurance or regulated professional services where these are not within our authorised
        scope.</li>
        <li><strong>Documented work</strong> Our engagements are supported by structured working
        methods and written deliverables.</li>
        <li><strong>Responsible use of information</strong> We take confidentiality, data handling,
        source attribution and appropriate access to client information seriously.</li>
      </ol>
    </div>
    <div class="panel">
      <div class="kicker">How we deliver our work</div>
      <h3>Serving clients across South Africa</h3>
      <ul class="check" style="margin-bottom:16px">
        <li>Remote engagements.</li>
        <li>Hybrid engagements.</li>
        <li>Agreed visits to client premises.</li>
        <li>Appropriate field-based assignments.</li>
      </ul>
      <p style="color:var(--muted);font-size:14.5px">The delivery arrangement is determined by the
      nature of the work, the client's requirements and the information or access needed.
      On-site and field-based work is agreed and priced separately where applicable.</p>
      <div class="callout lime" style="margin-top:18px">
        <h3>Our commitment</h3>
        <p>We aim to build a firm recognised for disciplined analysis, professional communication,
        reliable documentation and useful business insight.</p>
        <p>We do not believe every business problem requires a large consulting engagement. We
        believe the right work should be defined around the actual question, the available evidence
        and the value the assignment is expected to provide.</p>
      </div>
    </div>
  </div>
</div></section>

""" + cta_band("Start with the business question.",
    "Tell us what you are trying to understand, investigate or improve, and we will help define "
    "the work required.", "Discuss Your Business Needs"))

# ─────────────────────── SERVICES OVERVIEW ───────────────────────
add("services.html",
    f"Business Advisory Services | {COMPANY_NAME}",
    "Business intelligence, economic and commercial intelligence, and operational risk advisory "
    "services for South African businesses.",
    pagehero("Our services",
             "Understand your business. Evaluate your market. Strengthen your operations.",
             "Our advisory services help businesses examine internal performance, external "
             "commercial conditions and the processes that support daily operations. Explore our "
             "three specialist divisions to identify the service most relevant to your business.",
             tags=["3 Divisions", "9 Service packages", "Delivered across South Africa"]) + f"""

<section class="block"><div class="wrap">
  <div class="grid g3">
    <div class="card rise"><span class="num">01</span>
      <div class="divlabel">Division 01</div>
      <h3>Business Intelligence &amp; Performance Analytics</h3>
      <p class="tagline">Understand what your business information is telling you.</p>
      <p>We help businesses assess internal data, develop management dashboards and produce
      recurring performance reports.</p>
      <p><strong>Included services:</strong><br>
      · Business Data Diagnostic<br>· Business Intelligence Dashboard<br>
      · Monthly Business Performance Reporting</p>
      <a class="cardlink" href="business-intelligence-performance-analytics.html">Explore this division</a>
    </div>
    <div class="card rise"><span class="num">02</span>
      <div class="divlabel">Division 02</div>
      <h3>Economic &amp; Commercial Intelligence</h3>
      <p class="tagline">Make more informed decisions about your commercial environment.</p>
      <p>We investigate competitors, pricing, supplier costs and relevant market information to
      support business planning and commercial decisions.</p>
      <p><strong>Included services:</strong><br>
      · Competitor Intelligence Snapshot<br>· Pricing &amp; Profitability Review<br>
      · Supplier Cost Watch</p>
      <a class="cardlink" href="economic-commercial-intelligence.html">Explore this division</a>
    </div>
    <div class="card rise"><span class="num">03</span>
      <div class="divlabel">Division 03</div>
      <h3>Operational Risk, Process &amp; Controls Advisory</h3>
      <p class="tagline">Identify operational weaknesses and improve the way work is managed.</p>
      <p>We examine business processes, operational risks, controls and supporting documentation.</p>
      <p><strong>Included services:</strong><br>
      · Operational Risk Register<br>· Process &amp; Controls Diagnostic<br>
      · Compliance Evidence Organiser</p>
      <a class="cardlink" href="operational-risk-process-controls.html">Explore this division</a>
    </div>
  </div>
</div></section>

<section class="block tint"><div class="wrap">
  <div class="sec-head rise">
    <span class="eyebrow">How to choose a service</span>
    <h2>Not sure where to begin?</h2>
  </div>
  <div class="grid g3 rise">
    <div class="panel"><div class="kicker">Start with Division 01 if you need to understand</div>
      <p style="color:var(--muted)">Your sales, costs, performance or business records.</p>
      <p style="margin-top:10px"><a class="cardlink" href="business-intelligence-performance-analytics.html">Business Intelligence &amp; Performance Analytics</a></p></div>
    <div class="panel"><div class="kicker">Start with Division 02 if you need to understand</div>
      <p style="color:var(--muted)">Competitors, pricing, suppliers or market conditions.</p>
      <p style="margin-top:10px"><a class="cardlink" href="economic-commercial-intelligence.html">Economic &amp; Commercial Intelligence</a></p></div>
    <div class="panel"><div class="kicker">Start with Division 03 if you need to examine</div>
      <p style="color:var(--muted)">Processes, risks, controls or documentation.</p>
      <p style="margin-top:10px"><a class="cardlink" href="operational-risk-process-controls.html">Operational Risk, Process &amp; Controls Advisory</a></p></div>
  </div>
  <p style="margin-top:24px;color:var(--muted);max-width:78ch">If you are uncertain, submit an
  enquiry explaining the business question you are trying to address. We can help determine whether
  an existing service is suitable or whether a separately scoped engagement is required.</p>
  <p style="margin-top:18px"><a class="btn btn-primary" href="contact.html">Help Me Identify the Right Service</a></p>
</div></section>

""" + cta_band("Every engagement starts with a defined scope.",
    "Tell us the question you need answered and we will propose the work required, the evidence "
    "needed and the deliverables you will receive.", "Discuss Your Business Needs"))

# ─────────────────────── DIVISION PAGES ───────────────────────
def division_page(fname, dnum, name, title, intro, examine_head, examine_items,
                  services, extra_html, cta_label):
    svc = "".join(
        f"""<div class="svc-item rise">
          <span class="num">{s[0]}</span>
          <div><h3>{s[1]}</h3><p>{s[2]}</p></div>
          <a class="btn btn-outline btn-sm" href="{s[3]}">View Service</a>
        </div>""" for s in services)
    body = pagehero(f"Division {dnum}", title, intro, crumbs=f"Services / {name}") + f"""

<section class="block"><div class="wrap">
  <div class="two-col rise">
    <div class="panel">
      <div class="kicker">{name}</div>
      <h3>{examine_head}</h3>
      <ul class="check" style="margin-top:6px">{''.join(f'<li>{x}</li>' for x in examine_items)}</ul>
    </div>
    <div class="panel">
      <div class="kicker">Our services</div>
      <h3>Structured packages within this division</h3>
      <div class="svc-list" style="margin-top:10px">{svc}</div>
    </div>
  </div>
</div></section>

{extra_html}

<section class="block tint"><div class="wrap">
  <div class="callout rise" style="max-width:860px">
    <h3>Important scope note</h3>
    <p id="scope-note"></p>
  </div>
  <div style="margin-top:30px">
    <a class="btn btn-primary" href="contact.html">{cta_label}</a>
  </div>
</div></section>"""
    return body

# Division 01 (copy §5)
body01 = division_page(
    "business-intelligence-performance-analytics.html", "01",
    "Business Intelligence &amp; Performance Analytics",
    "Understand the numbers behind your business.",
    "Business decisions become more difficult when information is incomplete, scattered or "
    "difficult to interpret. Our Business Intelligence &amp; Performance Analytics division helps "
    "businesses examine their internal information, monitor performance and develop clearer "
    "management reporting. We work with relevant business records and datasets to identify trends, "
    "highlight exceptions and present information in a more useful format.",
    "What we help businesses understand",
    ["How revenue and expenses are changing.",
     "Which performance indicators require attention.",
     "Whether business records are sufficiently structured for analysis.",
     "How sales, costs or other selected measures are performing.",
     "Where reporting gaps or data-quality problems exist.",
     "How management information can be presented more clearly."],
    [("01", "Business Data Diagnostic",
      "A structured examination of selected business data to assess its completeness, consistency, "
      "organisation and suitability for analysis.", "business-data-diagnostic.html"),
     ("02", "Business Intelligence Dashboard",
      "A customised dashboard that presents agreed business indicators and performance information "
      "in a structured visual format.", "business-intelligence-dashboard.html"),
     ("03", "Monthly Business Performance Reporting",
      "A recurring reporting service that helps management monitor selected performance indicators, "
      "trends and exceptions over an agreed reporting period.", "monthly-performance-reporting.html")],
    f"""
<section class="block tint"><div class="wrap">
  <div class="sec-head rise">
    <span class="eyebrow">Our typical outputs</span>
    <h2>What clients may receive, depending on the engagement</h2>
  </div>
  <div class="two-col rise">
    <ul class="check">
      <li>Data-quality findings.</li>
      <li>Cleaned or organised datasets within the agreed scope.</li>
      <li>KPI definitions and calculations.</li>
      <li>Performance dashboards.</li>
    </ul>
    <ul class="check">
      <li>Written performance reports.</li>
      <li>Trend analysis and observations.</li>
      <li>Recommendations and action points.</li>
      <li>User guidance or handover documentation.</li>
    </ul>
  </div>
</div></section>""",
    "Discuss Your Business Information Needs")
# Fill the scope note via a replacement token (avoids nested-brace issues)
body01 = body01.replace('<p id="scope-note"></p>',
    "<p>The quality of analysis depends on the quality, completeness and relevance of the "
    "information provided. We identify material limitations rather than presenting incomplete "
    "information as conclusive. Our services do not constitute an audit, independent assurance "
    "engagement or statutory accounting service.</p>")
add("business-intelligence-performance-analytics.html",
    f"Business Intelligence &amp; Performance Analytics | {COMPANY_NAME}",
    "Business data diagnostics, intelligence dashboards and monthly performance reporting for "
    "South African businesses.",
    body01)

# Division 02 (copy §6)
body02 = division_page(
    "economic-commercial-intelligence.html", "02",
    "Economic &amp; Commercial Intelligence",
    "Understand the market beyond your business.",
    "Businesses operate within changing commercial environments. Competitor activity, supplier "
    "costs, pricing decisions and wider economic conditions can all affect business performance. "
    "Our Economic &amp; Commercial Intelligence division investigates relevant external information "
    "to help businesses assess their commercial position and make more informed decisions.",
    "What we help businesses examine",
    ["Competitor products and services.",
     "Publicly available competitor pricing.",
     "Market and industry developments.",
     "Supplier prices and cost changes.",
     "Pricing structures and gross margin information.",
     "Commercial opportunities and constraints.",
     "Relevant economic indicators."],
    [("01", "Competitor Intelligence Snapshot",
      "A structured review of selected competitors using relevant and appropriately sourced "
      "information.", "competitor-intelligence-snapshot.html"),
     ("02", "Pricing &amp; Profitability Review",
      "An examination of supplied pricing and cost information to help a business understand "
      "selected pricing relationships and gross margin implications.", "pricing-profitability-review.html"),
     ("03", "Supplier Cost Watch",
      "A structured comparison and monitoring service focused on selected suppliers, products or "
      "cost categories.", "supplier-cost-watch.html")],
    f"""
<section class="block tint"><div class="wrap">
  <div class="two-col rise">
    <div class="panel">
      <div class="kicker">Our approach</div>
      <h3>Relevant, identifiable information — with stated limitations</h3>
      <p style="color:var(--muted)">We use relevant, identifiable information and explain the
      coverage and limitations of the analysis.</p>
      <p style="color:var(--muted);margin-top:10px">Where information is publicly available, we
      distinguish observed facts from interpretation. Where information is supplied by the client,
      we identify the data used and any limitations affecting the findings.</p>
    </div>
    <div class="panel">
      <div class="kicker">Typical outputs</div>
      <h3>What clients may receive</h3>
      <ul class="check" style="margin-top:6px">
        <li>Competitor comparison tables.</li>
        <li>Pricing comparison schedules.</li>
        <li>Supplier comparison reports.</li>
        <li>Cost movement summaries.</li>
        <li>Gross margin calculations where supported by supplied information.</li>
        <li>Commercial observations.</li>
        <li>Written recommendations and decision considerations.</li>
      </ul>
    </div>
  </div>
</div></section>""",
    "Discuss a Commercial Research Requirement")
body02 = body02.replace('<p id="scope-note"></p>',
    "<p>Where information is publicly available, we do not represent it as a complete view of a "
    "competitor's internal financial position, strategy or confidential operations. Where cost "
    "analysis depends on supplied information, results depend on the accuracy and completeness of "
    "that information.</p>")
add("economic-commercial-intelligence.html",
    f"Economic &amp; Commercial Intelligence | {COMPANY_NAME}",
    "Competitor intelligence, pricing and profitability reviews, and supplier cost monitoring for "
    "South African businesses.",
    body02)

# Division 03 (copy §7)
body03 = division_page(
    "operational-risk-process-controls.html", "03",
    "Operational Risk, Process &amp; Controls Advisory",
    "Stronger operations begin with understanding how work gets done.",
    "A business can experience operational problems when processes are unclear, responsibilities "
    "are poorly defined, records are incomplete or important controls are not consistently applied. "
    "Our Operational Risk, Process &amp; Controls Advisory division helps businesses examine "
    "selected operational activities, identify weaknesses and document practical improvements.",
    "What we help businesses examine",
    ["Operational risks.",
     "Process steps and responsibilities.",
     "Documentation and recordkeeping.",
     "Internal control activities.",
     "Process inconsistencies.",
     "Evidence gaps.",
     "Corrective action requirements."],
    [("01", "Operational Risk Register",
      "A structured register of selected business risks, their assessed significance, proposed "
      "controls and suggested actions.", "operational-risk-register.html"),
     ("02", "Process &amp; Controls Diagnostic",
      "A review of an agreed business process to identify inefficiencies, control weaknesses and "
      "opportunities for improvement.", "process-controls-diagnostic.html"),
     ("03", "Compliance Evidence Organiser",
      "An organised review of selected compliance-related documents and evidence to identify "
      "missing records and improve document organisation.", "compliance-evidence-organiser.html")],
    f"""
<section class="block tint"><div class="wrap">
  <div class="two-col rise">
    <div class="panel">
      <div class="kicker">Our approach</div>
      <h3>Assessment based on evidence made available</h3>
      <p style="color:var(--muted)">We assess the agreed process or operational area using
      information made available by the client, discussions with relevant personnel and other
      appropriate evidence.</p>
      <p style="color:var(--muted);margin-top:10px">We document observations and distinguish
      identified weaknesses from matters requiring further verification. Our recommendations are
      intended to help businesses improve their internal organisation and control practices.</p>
    </div>
    <div class="panel">
      <div class="kicker">Professional boundary</div>
      <h3>What these services are not</h3>
      <p style="color:var(--muted)">These services do not constitute legal advice, statutory
      compliance certification, a statutory audit or an assurance opinion.</p>
      <p style="color:var(--muted);margin-top:10px">Where a matter requires a regulated
      professional or specialist legal opinion, we may recommend that the client obtain appropriate
      external assistance.</p>
    </div>
  </div>
</div></section>""",
    "Discuss an Operational Challenge")
body03 = body03.replace('<p id="scope-note"></p>',
    "<p>The register and diagnostic outputs are advisory working documents, not guarantees that "
    "every risk has been identified or eliminated. Assessments reflect the information made "
    "available during the engagement and matters requiring further verification are clearly "
    "distinguished from established findings.</p>")
add("operational-risk-process-controls.html",
    f"Operational Risk, Process &amp; Controls Advisory | {COMPANY_NAME}",
    "Operational risk registers, process and controls diagnostics, and compliance evidence "
    "organisation for South African businesses.",
    body03)

# ─────────────────── NINE INDIVIDUAL SERVICE PAGES ───────────────────
def service_page(fname, division_label, division_href, title, intro, addr_head, addr_items,
                 do_head, do_items, recv_head, recv_items, need_head, need_items,
                 scope_text, boundary, cta_label):
    addr = ""
    if addr_items:
        addr = f"""<div class="panel rise">
          <div class="kicker">What this service addresses</div>
          <h3>{addr_head}</h3>
          <ul class="check">{''.join(f'<li>{x}</li>' for x in addr_items)}</ul>
        </div>"""
    do = f"""<div class="panel rise">
      <div class="kicker">What we do</div>
      <h3>{do_head}</h3>
      <ol class="steps">{''.join(f'<li><strong>{t}</strong> {d}</li>' if t else f'<li>{d}</li>'
                                 for t, d in do_items)}</ol>
    </div>"""
    recv = f"""<div class="panel rise">
      <div class="kicker">What you receive</div>
      <h3>{recv_head}</h3>
      <ul class="check">{''.join(f'<li>{x}</li>' for x in recv_items)}</ul>
    </div>"""
    need = ""
    if need_items:
        need = f"""<div class="panel rise">
          <div class="kicker">What we need from you</div>
          <h3>Inputs that make the work possible</h3>
          <ul class="check">{''.join(f'<li>{x}</li>' for x in need_items)}</ul>
        </div>"""
    bnd = ""
    if boundary:
        bnd = f"""<div class="callout lime rise">
          <h3>Important professional boundary</h3>
          <p>{boundary}</p>
        </div>"""
    crumbs = f'<a href="services.html">Services</a> / <a href="{division_href}">{division_label}</a> / {title}'
    return pagehero(division_label, title, intro, crumbs=crumbs) + f"""

<section class="block"><div class="wrap">
  <div class="grid g2">{addr}{do}</div>
  <div class="grid g2" style="margin-top:clamp(16px,2vw,26px)">{recv}{need}</div>
</div></section>

<section class="block tint"><div class="wrap">
  <div class="callout rise">
    <h3>Scope considerations</h3>
    <p>{scope_text}</p>
  </div>
  {f'<div style="margin-top:22px" class="rise">{bnd}</div>' if bnd else ''}
  <div style="margin-top:30px">
    <a class="btn btn-primary" href="contact.html">{cta_label}</a>
  </div>
</div></section>"""

# 8.1 Business Data Diagnostic
add("business-data-diagnostic.html",
    f"Business Data Diagnostic | {COMPANY_NAME}",
    "A structured examination of selected business data to assess completeness, consistency and "
    "suitability for analysis.",
    service_page("business-data-diagnostic.html",
        "Business Intelligence &amp; Performance Analytics", "business-intelligence-performance-analytics.html",
        "Before you analyse the numbers, understand the data.",
        "Business analysis is only as reliable as the information supporting it. A Business Data "
        "Diagnostic examines selected business records or datasets to identify problems affecting "
        "their organisation, consistency, completeness and suitability for analysis.",
        "You may have business information but still experience difficulties such as:",
        ["Records stored across multiple spreadsheets.",
         "Inconsistent naming or data formats.",
         "Missing values or incomplete entries.",
         "Duplicate records.",
         "Unclear categories.",
         "Reporting figures that do not reconcile.",
         "Difficulty preparing information for dashboards or analysis."],
        "Depending on the agreed scope, we:",
        [("", "Review the supplied datasets and their structure."),
         ("", "Examine completeness and consistency."),
         ("", "Identify duplicates, missing information and apparent anomalies."),
         ("", "Assess whether the data is suitable for the intended analytical purpose."),
         ("", "Organise or clean a sample or agreed dataset where included in scope."),
         ("", "Document findings and recommended improvements.")],
        "Deliverables for this service",
        ["Data diagnostic report.",
         "Data-quality findings.",
         "Summary of identified issues.",
         "Agreed cleaned or organised dataset, if included.",
         "Recommendations for improving data management.",
         "Suggested next steps for reporting or analysis."],
        "Inputs we ask for",
        ["The relevant business datasets or exports.",
         "An explanation of how the information is currently used.",
         "The business question or reporting objective.",
         "Relevant definitions or explanations of the data fields."],
        "The quotation will identify the datasets, reporting periods, volume and level of data "
        "cleaning included. Extensive reconstruction, system integration or ongoing data management "
        "is not automatically included.",
        None, "Request a Business Data Diagnostic"))

# 8.2 Business Intelligence Dashboard
add("business-intelligence-dashboard.html",
    f"Business Intelligence Dashboard | {COMPANY_NAME}",
    "A customised dashboard presenting agreed business indicators and performance information in a "
    "structured visual format.",
    service_page("business-intelligence-dashboard.html",
        "Business Intelligence &amp; Performance Analytics", "business-intelligence-performance-analytics.html",
        "See your business performance more clearly.",
        "A Business Intelligence Dashboard brings selected business indicators together in a visual "
        "reporting environment. Instead of working through multiple records to understand "
        "performance, management can review agreed indicators in one structured dashboard.",
        "This service is useful when a business experiences:",
        ["Business information spread across multiple files.",
         "Difficulty tracking performance indicators.",
         "Time-consuming manual reporting.",
         "Limited visibility of sales or expense trends.",
         "Difficulty comparing reporting periods.",
         "Inconsistent management reports."],
        "Our working process:",
        [("", "Establish the dashboard's purpose and intended users."),
         ("", "Identify the relevant performance indicators."),
         ("", "Review the available data sources."),
         ("", "Agree the dashboard structure and reporting requirements."),
         ("", "Prepare and organise the relevant data."),
         ("", "Develop the dashboard."),
         ("", "Test calculations and visualisations."),
         ("", "Provide handover guidance.")],
        "Deliverables for this service",
        ["A dashboard built around the agreed requirements.",
         "Agreed KPI definitions.",
         "Selected charts, tables and performance indicators.",
         "Filters or reporting-period selections where included.",
         "Data-source documentation.",
         "User guidance or handover notes."],
        "Inputs we ask for",
        ["Relevant business data or system exports.",
         "Reporting objectives.",
         "Desired performance indicators.",
         "Relevant definitions and business rules.",
         "Intended dashboard users."],
        "The quotation will define the data sources, number of indicators, dashboard complexity, "
        "update arrangements and software requirements. Ongoing automated connections, system "
        "integrations, software licences and continuing maintenance are separate unless expressly "
        "included.",
        None, "Request a Dashboard"))

# 8.3 Monthly Business Performance Reporting
add("monthly-performance-reporting.html",
    f"Monthly Business Performance Reporting | {COMPANY_NAME}",
    "A recurring review of agreed business indicators, KPIs, trends and exceptions over an "
    "established reporting period.",
    service_page("monthly-performance-reporting.html",
        "Business Intelligence &amp; Performance Analytics", "business-intelligence-performance-analytics.html",
        "Keep track of what is changing in your business.",
        "Monthly Business Performance Reporting provides a recurring review of agreed business "
        "indicators over an established reporting period. The objective is to help management "
        "monitor performance, identify important movements and understand areas that may require "
        "attention.",
        "",
        [],
        "What the service includes",
        [("", "Review of agreed monthly business information."),
         ("", "Calculation or updating of selected KPIs."),
         ("", "Revenue and expense trend analysis where data is available."),
         ("", "Comparison against agreed periods or targets."),
         ("", "Identification of notable changes and exceptions."),
         ("", "Written performance observations."),
         ("", "Suggested management action points.")],
        "Your monthly report contains:",
        ["Executive summary.",
         "KPI performance.",
         "Relevant trends and comparisons.",
         "Notable movements or exceptions.",
         "Analytical observations.",
         "Recommended areas for management attention."],
        "Inputs we ask for",
        ["Agreed monthly data submissions.",
         "Reporting period and submission deadlines.",
         "KPI definitions and targets, where applicable.",
         "Explanations of significant business changes.",
         "Any relevant management reporting requirements."],
        "The engagement will specify the number of reporting indicators, data sources, reporting "
        "frequency, submission deadlines and consultation allowance. A dashboard update may be "
        "included where agreed.",
        None, "Discuss Monthly Reporting"))

# 8.4 Competitor Intelligence Snapshot
add("competitor-intelligence-snapshot.html",
    f"Competitor Intelligence Snapshot | {COMPANY_NAME}",
    "A structured review of selected competitors using relevant and appropriately sourced "
    "publicly available information.",
    service_page("competitor-intelligence-snapshot.html",
        "Economic &amp; Commercial Intelligence", "economic-commercial-intelligence.html",
        "Understand the businesses competing for the same customers.",
        "A Competitor Intelligence Snapshot provides a structured review of selected competitors "
        "and relevant publicly available commercial information. It helps a business understand how "
        "selected competitors present their products or services, what they offer and how their "
        "visible commercial positioning compares.",
        "This service is useful when a business has:",
        ["Limited understanding of competitor offerings.",
         "Uncertainty about publicly advertised prices.",
         "Difficulty comparing products or services.",
         "Questions about competitor positioning.",
         "A need for a structured competitor overview."],
        "Our working process:",
        [("", "Define the relevant market or competitor group."),
         ("", "Agree the competitors to be examined."),
         ("", "Identify appropriate information sources."),
         ("", "Review relevant products, services and publicly available prices."),
         ("", "Compare selected features and positioning."),
         ("", "Document findings and commercial observations.")],
        "Deliverables for this service",
        ["Competitor overview.",
         "Comparison tables.",
         "Selected product or service comparisons.",
         "Public pricing observations where available.",
         "Source references.",
         "Key findings and commercial considerations."],
        "Inputs we ask for",
        ["The competitors or market you want examined.",
         "Any commercial questions you want answered.",
         "Relevant internal observations you want compared against public information."],
        "The engagement will define the competitors, geographic coverage, information categories "
        "and research period. We do not represent publicly available information as a complete view "
        "of a competitor's internal financial position, strategy or confidential operations.",
        None, "Request Competitor Intelligence"))

# 8.5 Pricing & Profitability Review
add("pricing-profitability-review.html",
    f"Pricing &amp; Profitability Review | {COMPANY_NAME}",
    "An examination of supplied pricing and cost information to understand pricing relationships "
    "and gross margin implications.",
    service_page("pricing-profitability-review.html",
        "Economic &amp; Commercial Intelligence", "economic-commercial-intelligence.html",
        "Understand the relationship between your prices and costs.",
        "Pricing decisions affect revenue, margins and commercial sustainability. A Pricing &amp; "
        "Profitability Review examines selected pricing and cost information to help a business "
        "understand its current pricing structure and the gross margin implications of alternative "
        "scenarios.",
        "This service is useful when a business has:",
        ["Uncertainty about gross margins.",
         "Difficulty comparing product or service prices.",
         "Changes in input costs.",
         "Questions about the effect of price adjustments.",
         "Limited visibility of product-level or service-level profitability."],
        "Our working process:",
        [("", "Review supplied pricing and cost information."),
         ("", "Identify relevant cost and revenue components."),
         ("", "Calculate gross margins where the information supports this."),
         ("", "Compare selected products, services or pricing arrangements."),
         ("", "Examine agreed pricing scenarios."),
         ("", "Present findings and commercial considerations.")],
        "Deliverables for this service",
        ["Pricing and cost summary.",
         "Relevant gross margin calculations.",
         "Comparative schedules.",
         "Agreed pricing scenarios.",
         "Written findings.",
         "Practical considerations for management."],
        "Inputs we ask for",
        ["Current selling prices.",
         "Relevant direct cost information.",
         "Product or service descriptions.",
         "Discounts or pricing rules relevant to the analysis.",
         "Any specific pricing questions."],
        "Results depend on the accuracy and completeness of supplied cost information.",
        "The review is not a statutory audit, independent valuation, tax opinion or formal "
        "financial assurance engagement.",
        "Request a Pricing Review"))

# 8.6 Supplier Cost Watch
add("supplier-cost-watch.html",
    f"Supplier Cost Watch | {COMPANY_NAME}",
    "A structured comparison and monitoring service focused on selected suppliers, products or "
    "cost categories.",
    service_page("supplier-cost-watch.html",
        "Economic &amp; Commercial Intelligence", "economic-commercial-intelligence.html",
        "Keep a clearer view of supplier costs.",
        "Supplier prices can change over time, affecting purchasing decisions and business costs. "
        "Supplier Cost Watch provides a structured comparison or recurring review of selected "
        "supplier prices and cost categories.",
        "This service is useful when a business has:",
        ["Limited visibility of supplier price movements.",
         "Difficulty comparing supplier quotations.",
         "Uncertainty about changes in purchasing costs.",
         "Inconsistent supplier comparison records.",
         "A need for recurring cost monitoring."],
        "Depending on the agreed engagement, we:",
        [("", "Identify the suppliers and cost categories to monitor."),
         ("", "Review supplied quotations, price lists or other appropriate information."),
         ("", "Compare selected prices and terms."),
         ("", "Record observed price changes."),
         ("", "Identify notable cost movements."),
         ("", "Present a structured comparison and observations.")],
        "Deliverables for this service",
        ["Supplier comparison schedule.",
         "Price baseline.",
         "Cost movement summary.",
         "Relevant supporting source information.",
         "Periodic monitoring report where agreed.",
         "Management observations."],
        "Inputs we ask for",
        ["The suppliers, products or cost categories you want monitored.",
         "Supplied quotations, price lists or purchase records.",
         "Any purchasing rules or thresholds relevant to the comparison."],
        "The quotation will specify the suppliers, items, reporting frequency and sources of "
        "information. We do not guarantee supplier prices, product availability or future price "
        "movements.",
        None, "Discuss Supplier Cost Monitoring"))

# 8.7 Operational Risk Register
add("operational-risk-register.html",
    f"Operational Risk Register | {COMPANY_NAME}",
    "A structured register of selected business risks, their assessed significance, proposed "
    "controls and suggested actions.",
    service_page("operational-risk-register.html",
        "Operational Risk, Process &amp; Controls Advisory", "operational-risk-process-controls.html",
        "Make operational risks visible and easier to manage.",
        "Operational risks can affect service delivery, financial performance, business continuity "
        "and the reliability of everyday activities. An Operational Risk Register helps a business "
        "document selected risks, assess their significance and identify appropriate control "
        "considerations.",
        "This service is useful when a business has:",
        ["Risks that have not been formally documented.",
         "Unclear responsibility for risk management.",
         "Inconsistent operational practices.",
         "Limited visibility of control weaknesses.",
         "Difficulty tracking corrective actions."],
        "Our working process:",
        [("", "Agree the operational areas to be considered."),
         ("", "Gather relevant information through documents and discussions."),
         ("", "Identify selected operational risks."),
         ("", "Assess risks using an agreed rating approach."),
         ("", "Document existing controls where information is available."),
         ("", "Identify possible control improvements."),
         ("", "Prepare an action tracker.")],
        "Deliverables for this service",
        ["Operational Risk Register.",
         "Risk descriptions and categories.",
         "Risk assessment ratings.",
         "Existing control observations.",
         "Proposed control measures.",
         "Suggested risk owners.",
         "Corrective action tracker."],
        "Inputs we ask for",
        ["The operational areas to be considered.",
         "Relevant internal documents and records.",
         "Access to relevant personnel for discussions, where agreed."],
        "The engagement will define the number of risks, business areas and level of assessment. "
        "The register is an advisory working document, not a guarantee that every risk has been "
        "identified or eliminated.",
        None, "Request an Operational Risk Register"))

# 8.8 Process & Controls Diagnostic
add("process-controls-diagnostic.html",
    f"Process &amp; Controls Diagnostic | {COMPANY_NAME}",
    "A review of an agreed business process to identify inefficiencies, control weaknesses and "
    "opportunities for improvement.",
    service_page("process-controls-diagnostic.html",
        "Operational Risk, Process &amp; Controls Advisory", "operational-risk-process-controls.html",
        "Understand the process before trying to improve it.",
        "A business process may appear straightforward but still contain unnecessary steps, unclear "
        "responsibilities, inconsistent practices or weak controls. A Process &amp; Controls "
        "Diagnostic examines an agreed process to identify how work is performed and where "
        "improvements may be appropriate.",
        "This service is useful when a business has:",
        ["Processes that are not properly documented.",
         "Unclear responsibilities.",
         "Repeated administrative work.",
         "Inconsistent approval practices.",
         "Missing supporting records.",
         "Weak or poorly defined control activities."],
        "Our working process:",
        [("", "Agree the process to be examined."),
         ("", "Review relevant documentation."),
         ("", "Discuss the process with appropriate personnel."),
         ("", "Map the existing process where included."),
         ("", "Identify potential weaknesses and control gaps."),
         ("", "Develop practical improvement recommendations."),
         ("", "Prepare an implementation checklist.")],
        "Deliverables for this service",
        ["Process overview or process map.",
         "Diagnostic findings.",
         "Identified process weaknesses.",
         "Control observations.",
         "Recommendations.",
         "Suggested implementation checklist."],
        "Inputs we ask for",
        ["The process to be examined and its boundaries.",
         "Relevant process documents, templates and records.",
         "Access to the personnel who perform the process, where agreed."],
        "The engagement will specify the process, locations, personnel and level of documentation "
        "included. Implementing recommended changes, configuring business software or redesigning "
        "multiple processes requires separate agreement unless included in the quotation.",
        None, "Request a Process Diagnostic"))

# 8.9 Compliance Evidence Organiser
add("compliance-evidence-organiser.html",
    f"Compliance Evidence Organiser | {COMPANY_NAME}",
    "An organised review of selected compliance-related documents and evidence to identify missing "
    "records and improve document organisation.",
    service_page("compliance-evidence-organiser.html",
        "Operational Risk, Process &amp; Controls Advisory", "operational-risk-process-controls.html",
        "Bring structure to your business documentation.",
        "Businesses often need to maintain records and supporting documents for internal "
        "administration, external requirements or professional review. The Compliance Evidence "
        "Organiser helps organise selected documents and identify gaps in the available evidence.",
        "This service is useful when a business has:",
        ["Documents stored across different locations.",
         "Unclear document ownership.",
         "Missing or expired records.",
         "Difficulty locating supporting evidence.",
         "Inconsistent document organisation.",
         "No central document checklist."],
        "Our working process:",
        [("", "Agree the document categories to be reviewed."),
         ("", "Review the records made available."),
         ("", "Develop an agreed document inventory."),
         ("", "Identify missing or incomplete items."),
         ("", "Organise a document and evidence tracker."),
         ("", "Recommend a practical structure for maintaining records.")],
        "Deliverables for this service",
        ["Document inventory.",
         "Evidence checklist.",
         "Missing-document tracker.",
         "Document organisation recommendations.",
         "Suggested recordkeeping structure.",
         "Referral recommendations where specialist advice is needed."],
        "Inputs we ask for",
        ["The document categories to be reviewed.",
         "Access to the records made available for review.",
         "Any internal or external requirements the documents must support."],
        "The engagement will specify the document categories, locations and level of organisation "
        "included. This service helps organise documentation and identify apparent evidence gaps.",
        "It does not certify legal compliance, determine legal obligations or replace advice from "
        "an appropriately qualified legal, tax or regulatory professional.",
        "Request a Compliance Evidence Review"))

# ─────────────────── RESEARCH PUBLICATIONS ───────────────────
add("research-publications.html",
    f"Research Publications &amp; Intelligence Products | {COMPANY_NAME}",
    "Independent research publications on selected economic, industry, market and commercial "
    "topics, developed in South Africa.",
    pagehero("Research publications &amp; intelligence products",
             "Independent research. Structured analysis. Available when you need it.",
             f"Explore research publications developed by {COMPANY_NAME} on selected economic, "
             "industry, market and commercial topics. Our publications bring relevant information "
             "together in a structured format, supported by research, analysis and clearly "
             "identified sources.",
             tags=["Industry Performance Reports", "Economic Research",
                   "Market &amp; Commercial Intelligence", "Statistical Publications",
                   "Intelligence Briefs"]) + f"""

<section class="block"><div class="wrap">
  <div class="two-col rise">
    <div class="paper">
      <span class="eyebrow">Introduction</span>
      <h2>Not every research requirement needs a commissioned engagement.</h2>
      <p style="color:var(--muted)">Our Research Publications unit develops selected reports and
      intelligence products independently, making them available for purchase through our website.</p>
      <p style="color:var(--muted);margin-top:10px">Each publication has a defined subject,
      reporting period, scope and methodology.</p>
    </div>
    <div class="paper">
      <span class="eyebrow">Research standards</span>
      <h2>A structured research process.</h2>
      <p style="color:var(--muted)">We prioritise relevant institutional and primary sources,
      transparent methodology, appropriate data validation and clear explanations of limitations.</p>
      <p style="color:var(--muted);margin-top:10px">Sources may include South African public
      institutions and relevant international organisations, depending on the subject.</p>
    </div>
  </div>
</div></section>

<section class="block tint"><div class="wrap">
  <div class="sec-head rise">
    <span class="eyebrow">Publication categories</span>
    <h2>What our catalogue covers</h2>
  </div>
  <div class="grid g3 rise">
    <div class="panel"><h3>Industry Performance Reports</h3>
      <p style="color:var(--muted)">Research examining developments, trends and performance
      indicators within selected industries.</p></div>
    <div class="panel"><h3>Economic Research Reports</h3>
      <p style="color:var(--muted)">Analysis of selected economic indicators, developments and
      issues affecting the South African economy.</p></div>
    <div class="panel"><h3>Market &amp; Commercial Intelligence</h3>
      <p style="color:var(--muted)">Research examining selected markets, competitive conditions
      and commercial developments.</p></div>
    <div class="panel"><h3>Statistical Publications &amp; Data Products</h3>
      <p style="color:var(--muted)">Structured statistical information, tables, datasets and
      supporting explanatory material.</p></div>
    <div class="panel"><h3>Intelligence Briefs</h3>
      <p style="color:var(--muted)">Focused publications addressing a specific business, industry
      or economic question.</p></div>
  </div>
</div></section>

<section class="block"><div class="wrap">
  <div class="sec-head rise">
    <span class="eyebrow">Publication catalogue</span>
    <h2>Browse available publications</h2>
    <p class="intro">Each listing shows the cover, category, reporting period, publication date,
    short description, price (in ZAR) and a View Publication button.</p>
  </div>
  <div class="empty rise">
    <div class="icon" aria-hidden="true"><svg width="26" height="26" viewBox="0 0 24 24" fill="none"
      stroke="#136CFC" stroke-width="1.8" stroke-linecap="round"><path d="M4 19V5a1 1 0 0 1 1-1h9l6 6v9a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1Z"/><path d="M14 4v6h6M8 13h8M8 16h5"/></svg></div>
    <h3>The catalogue is being developed</h3>
    <p>Our research catalogue is being developed. New publications will be added as they are
    completed and approved for release.</p>
    <p>Please check back for upcoming research products.</p>
  </div>
</div></section>

""" + cta_band("Need research tailored to your business?",
    "If you require research tailored to your business, market or commercial question, explore our "
    "Economic &amp; Commercial Intelligence services for commissioned research.",
    "Explore Commissioned Research Services", "Contact Us", "economic-commercial-intelligence.html",
    "contact.html"))

# ─────────────────── INSIGHTS ───────────────────
add("insights.html",
    f"Business and Economic Insights | {COMPANY_NAME}",
    "Research-led commentary, economic observations, industry analysis and practical business "
    "insights from a South African business advisory firm.",
    pagehero("Insights &amp; commentary",
             "Understanding the developments that affect business.",
             f"Explore research-led commentary, economic observations, industry analysis and "
             f"practical business insights from {COMPANY_NAME}. Our insights are intended to make "
             "relevant information easier to understand and connect it to business and commercial "
             "considerations.",
             tags=["Economic Intelligence", "Industry &amp; Commercial Intelligence",
                   "Business Performance", "Operational Risk &amp; Processes",
                   "Research &amp; Publications"]) + f"""

<section class="block"><div class="wrap">
  <div class="sec-head rise">
    <span class="eyebrow">Latest articles</span>
    <h2>Commentary and research summaries</h2>
    <p class="intro">Each article carries its category, publication date, reading time and a
    short introduction.</p>
  </div>
  <div class="empty rise">
    <div class="icon" aria-hidden="true"><svg width="26" height="26" viewBox="0 0 24 24" fill="none"
      stroke="#136CFC" stroke-width="1.8" stroke-linecap="round"><path d="M4 5h16v14H4z"/><path d="M7 9h10M7 12.5h10M7 16h6"/></svg></div>
    <h3>Our insights library is being developed</h3>
    <p>Published commentary and research summaries will appear here as they become available.</p>
  </div>
</div></section>

""" + cta_band("Looking for analysis on a specific question?",
    "Our commissioned research services examine the commercial and operational questions your "
    "business is facing right now.", "Discuss Your Business Needs", "View Our Services"))

# ─────────────────── CONTACT ───────────────────
PROVINCES = ["Eastern Cape", "Free State", "Gauteng", "KwaZulu-Natal", "Limpopo",
             "Mpumalanga", "North West", "Northern Cape", "Western Cape"]
ENQ_TYPES = ["Business Intelligence & Performance Analytics",
             "Economic & Commercial Intelligence",
             "Operational Risk, Process & Controls Advisory",
             "Research Publications", "General Enquiry"]
add("contact.html",
    f"Contact {COMPANY_NAME} | Business Advisory South Africa",
    "Discuss your business information, commercial research or operational requirements with a "
    "South African business advisory firm.",
    pagehero("Contact us", "Start with the business question.",
             "Tell us what you are trying to understand, investigate or improve. Whether your "
             "requirement relates to business performance, commercial research or operational "
             "processes, we will review your enquiry and determine the appropriate next step.") + f"""

<section class="block"><div class="wrap">
  <div class="contact-grid">
    <div class="panel rise">
      <span class="eyebrow">Enquiry form</span>
      <h2 style="margin-bottom:6px">Tell us about your requirement.</h2>
      <form class="enquiry" novalidate>
        <div class="error-summary" role="alert">Please correct the highlighted fields below and
        submit your enquiry again.</div>
        <div class="frow">
          <div class="field"><label for="f-name">Full name</label>
            <input id="f-name" name="name" type="text" autocomplete="name" data-req>
            <span class="msg"></span></div>
          <div class="field"><label for="f-org">Business or organisation <span class="opt">(optional)</span></label>
            <input id="f-org" name="org" type="text" autocomplete="organization"></div>
        </div>
        <div class="frow">
          <div class="field"><label for="f-email">Email address</label>
            <input id="f-email" name="email" type="email" autocomplete="email" data-req>
            <span class="msg"></span></div>
          <div class="field"><label for="f-tel">Telephone number <span class="opt">(optional)</span></label>
            <input id="f-tel" name="tel" type="tel" autocomplete="tel"></div>
        </div>
        <div class="frow">
          <div class="field"><label for="f-prov">Province</label>
            <select id="f-prov" name="province" data-req>
              <option value="">Select your province…</option>
              {''.join(f'<option>{p}</option>' for p in PROVINCES)}
            </select><span class="msg"></span></div>
          <div class="field"><label for="f-type">Type of enquiry</label>
            <select id="f-type" name="type" data-req>
              <option value="">Select the relevant division…</option>
              {''.join(f'<option>{t}</option>' for t in ENQ_TYPES)}
            </select><span class="msg"></span></div>
        </div>
        <div class="field"><label for="f-desc">Brief description of your requirement</label>
          <textarea id="f-desc" name="description" data-req
            placeholder="What are you trying to understand, investigate or improve?"></textarea>
          <span class="msg"></span></div>
        <fieldset class="radio"><legend>Preferred engagement arrangement</legend>
          <label><input type="radio" name="arr" value="Remote" checked> Remote</label>
          <label><input type="radio" name="arr" value="Hybrid / on-site"> Hybrid / on-site</label>
          <label><input type="radio" name="arr" value="Not sure yet"> Not sure yet</label>
        </fieldset>
        <fieldset class="radio"><legend>Preferred contact method</legend>
          <label><input type="radio" name="pcm" value="Email" checked> Email</label>
          <label><input type="radio" name="pcm" value="Telephone"> Telephone</label>
        </fieldset>
        <div class="field"><div class="consent">
          <input type="checkbox" id="f-consent" data-req>
          <label for="f-consent" style="font-weight:500">I acknowledge the
          <a href="privacy-policy.html">Privacy Policy</a> and consent to {COMPANY_NAME} using the
          information above to respond to my enquiry.</label></div>
          <span class="msg"></span></div>
        <div>
          <button class="btn btn-primary" type="submit">Submit Enquiry</button>
          <p class="form-note" style="margin-top:12px">Do not submit confidential financial
          records, passwords or sensitive personal information through this general enquiry form.</p>
        </div>
        <div class="confirm" role="status">
          <h3>Thank you for contacting {COMPANY_NAME}.</h3>
          <p>Your enquiry has been received. We will review the information provided and respond
          using your preferred contact details.</p>
        </div>
      </form>
    </div>
    <div style="display:grid;gap:18px">
      <div class="panel rise">
        <div class="kicker">Other ways to contact us</div>
        <ul class="check" style="margin-top:8px">
          <li><strong>Email:</strong> {COMPANY_EMAIL}</li>
          <li><strong>Telephone:</strong> {COMPANY_PHONE}</li>
          <li><strong>Coverage:</strong> South Africa</li>
        </ul>
      </div>
      <div class="panel rise">
        <div class="kicker">What happens next?</div>
        <ol class="steps" style="margin-top:8px">
          <li>We review your enquiry.</li>
          <li>We determine whether the requirement falls within our services.</li>
          <li>Where appropriate, we arrange an initial discussion.</li>
          <li>If the work is suitable, we prepare a defined scope and quotation.</li>
        </ol>
        <p style="color:var(--muted);font-size:13.5px;margin-top:16px">An enquiry does not
        automatically create a client engagement or professional relationship.</p>
      </div>
    </div>
  </div>
</div></section>""", active="contact.html")

# ─────────────────── FAQ ───────────────────
FAQ = [
 ("About the firm", [
  ("What does [Company Name] do?",
   "We provide business intelligence, economic and commercial research, performance analysis and "
   "operational risk advisory services. We also develop and sell independent research publications."),
  ("Where do you operate?", "We serve clients throughout South Africa."),
  ("Do you only work with large companies?",
   "No. Our services are designed to support established and growing businesses, including micro, "
   "small and medium-sized enterprises."),
  ("Do you have a physical office?",
   "Our initial operating model is remote-first, with agreed hybrid and on-site engagements at "
   "client premises where required. Any formal office details will be published if and when "
   "applicable."),
 ]),
 ("Services", [
  ("How do I know which service I need?",
   "Start by identifying the question you need answered. Internal performance questions generally "
   "fall under Business Intelligence &amp; Performance Analytics. External market and commercial "
   "questions fall under Economic &amp; Commercial Intelligence. Process, risk and control "
   "questions fall under Operational Risk, Process &amp; Controls Advisory. If you are uncertain, "
   "submit an enquiry."),
  ("Can I request a customised assignment?",
   "Yes. Requirements that fall outside standard service packages may be assessed and separately "
   "scoped."),
  ("Do you work remotely?", "Yes. Remote delivery is available where the nature of the work permits it."),
  ("Can you work at our premises?",
   "Yes. On-site arrangements may be agreed where required. Travel, accommodation and other "
   "applicable fieldwork costs will be disclosed separately."),
  ("Will I receive a written report?",
   "Written documentation is a standard part of our service approach. The specific format and "
   "level of detail depend on the engagement."),
  ("Will you need access to our accounting or business systems?",
   "Not necessarily. We prefer relevant data exports or authorised read-only access where these "
   "are sufficient. Any system access must be agreed, appropriately authorised and limited to the "
   "requirements of the engagement."),
 ]),
 ("Quotations and payments", [
  ("How do I obtain a quotation?",
   "Submit an enquiry describing your requirement. We may arrange an initial discussion before "
   "preparing a quotation."),
  ("What is your payment policy?",
   "Engagements below R2,000 are payable in full upfront. Engagements of R2,000 or more require a "
   "50% deposit and a 50% final payment."),
  ("When does work begin?",
   "Work begins after the quotation and engagement terms have been accepted, required onboarding "
   "information has been received and the applicable initial payment has been confirmed."),
  ("Are travel costs included?",
   "Not automatically. Any applicable travel, accommodation, fieldwork or external specialist "
   "costs will be identified in the quotation."),
 ]),
 ("Research publications", [
  ("What is the difference between a research publication and commissioned research?",
   "A research publication is developed independently and sold as a standard product to multiple "
   "customers. Commissioned research is undertaken for a specific client according to an agreed "
   "scope and requirements."),
  ("How do I purchase a publication?",
   "Select the publication, review its description and licence, and complete the online checkout "
   "process."),
  ("When will I receive my publication?",
   "Secure access is provided after payment has been confirmed and the purchase entitlement has "
   "been created."),
  ("Can I share a purchased publication?",
   "The standard purchase licence does not permit unauthorised redistribution, resale or "
   "republication. Refer to the licence displayed for the specific product."),
  ("Can I request research on a specific topic?",
   "Yes. Submit a commissioned research enquiry through the contact page."),
 ]),
 ("Confidentiality and information", [
  ("How is client information handled?",
   "Client information is handled according to the applicable engagement terms and the firm's "
   "privacy and information-handling procedures."),
  ("Should I send sensitive documents through the contact form?",
   "No. The general enquiry form should not be used for confidential financial records, passwords "
   "or sensitive personal information. Secure document submission arrangements can be established "
   "during onboarding."),
 ]),
]
faq_html = ""
for group, items in FAQ:
    acc = "".join(
        f'<details class="faq"><summary>{q}</summary><div class="a">{a}</div></details>'
        for q, a in items)
    faq_html += f'<div class="faq-group"><h2>{group}</h2>{acc}</div>'
add("faq.html",
    f"Frequently Asked Questions | {COMPANY_NAME}",
    "Answers about our services, quotations and payments, research publications and handling of "
    "client information.",
    pagehero("Frequently asked questions", "Questions about how we work.",
             "Practical answers about our services, quotations, payments, publications and the "
             "handling of client information.", crumbs="FAQ") +
    f'<section class="block" style="padding-top:20px"><div class="wrap" style="max-width:900px">{faq_html}</div></section>'
    + cta_band("Still have a question?",
               "Submit an enquiry describing what you are trying to understand, and we will "
               "point you to the right service or publication.", "Submit an Enquiry"))

# ─────────────────── CLIENT PORTAL ───────────────────
# Public site shows the sign-in stub only (copy document §14.1). The full portal is a separate
# authenticated interface; its specification lives in docs/client-portal-spec.md, not on this site.
add("client-portal.html",
    f"Client Login | {COMPANY_NAME}",
    "Client portal sign-in.",
    pagehero("Client portal", "Welcome back.",
             "Sign in to access your projects, documents, quotations, invoices and purchased "
             "research publications.") + f"""

<section class="block" style="padding-top:44px"><div class="wrap">
  <div class="panel rise" style="max-width:460px;margin:0 auto">
    <span class="eyebrow">Sign in</span>
    <h2 style="margin-bottom:14px">Access your account.</h2>
    <form class="enquiry portal-stub" novalidate>
      <div class="field"><label for="p-email">Email address</label>
        <input id="p-email" type="email" autocomplete="email"><span class="msg"></span></div>
      <div class="field"><label for="p-pass">Password</label>
        <input id="p-pass" type="password" autocomplete="current-password"><span class="msg"></span></div>
      <div><button class="btn btn-primary" type="submit">Sign In</button></div>
      <p class="portal-note" style="display:none;color:#8F2B2B;font-weight:600;font-size:13.5px">
      Sign-in is currently unavailable.</p>
    </form>
  </div>
</div></section>""", active="client-portal.html",
    extra_head='<meta name="robots" content="noindex">')

# ─────────────────── LEGAL PAGES (structure only — not final policies) ───────────────────
LEGAL = [
 ("privacy-policy.html", "Privacy Policy", "How personal information is collected, used and protected.",
  ["Introduction and responsible party", "Personal information collected",
   "How information is collected", "Purposes of processing",
   "Lawful basis and applicable conditions", "Information sharing and service providers",
   "Cross-border processing, where applicable", "Information security",
   "Retention and deletion", "Data subject rights", "Marketing communications",
   "Cookies and analytics", "Contact details for privacy enquiries", "Policy updates"],
  "The company must confirm its legal identity, contact details, actual data practices, retention "
  "arrangements, operators and any cross-border processing before this policy is finalised."),
 ("website-terms.html", "Website Terms &amp; Conditions", "The terms that apply to the use of this website.",
  ["Acceptance of terms", "Website access and permitted use", "Intellectual property",
   "Website content and accuracy", "Third-party services and links", "User submissions",
   "Website availability", "Limitation of liability, subject to applicable law",
   "Changes to the website and terms", "Governing law and dispute handling", "Contact information"],
  None),
 ("client-service-terms.html", "Client Service Terms", "The terms governing advisory engagements with the firm.",
  ["Definitions", "Enquiries and initial discussions", "Quotations and acceptance", "Scope of work",
   "Client responsibilities", "Fees and payment terms", "Commencement of work",
   "Timelines and dependencies", "Changes to scope", "Consultations and communication",
   "Deliverables and revisions", "Confidentiality", "Client information and system access",
   "Intellectual property", "Third-party costs", "Cancellation and termination",
   "Limitation of responsibility", "Dispute resolution", "Applicable law"],
  None),
 ("publication-licence.html", "Research Publication Licence", "The licence granted to purchasers of research publications.",
  ["Licence grant", "Permitted internal use", "Restrictions on redistribution",
   "Restrictions on resale", "Restrictions on republication",
   "Organisational and multi-user licences", "Copyright and attribution",
   "Publication limitations", "Updates and corrections", "Breach of licence", "Contact information"],
  None),
 ("refund-policy.html", "Digital Product Refund &amp; Cancellation Policy",
  "How refunds and cancellations are handled for digital products.",
  ["Scope of policy", "Digital product descriptions", "Purchase confirmation", "Download and access",
   "Technical problems", "Duplicate transactions", "Incorrect charges", "Refund request process",
   "Cancellation conditions", "Applicable consumer rights", "Contact details"],
  "The final policy must be checked against applicable South African consumer law. It will not "
  "state that all digital products are automatically non-refundable."),
]
for fname, ltitle, ldesc, sections, note in LEGAL:
    listed = "".join(f'<li>{s}</li>' for s in sections)
    add(fname, f"{ltitle} | {COMPANY_NAME}", ldesc,
        pagehero("Legal &amp; policies", ltitle, ldesc, crumbs=ltitle) + f"""
<section class="block" style="padding-top:30px"><div class="wrap" style="max-width:860px">
  <div class="notice rise"><strong>About this document.</strong> The final wording is under
  review and will be published here once it has been approved.</div>
  <div class="paper rise" style="margin-top:26px">
    <h2>Required sections</h2>
    <ol class="steps">{listed}</ol>
  </div>
</div></section>""")

# ─────────────────── 404 ───────────────────
add("404.html", "Page not found | " + COMPANY_NAME,
    "The page you requested could not be found.",
    f"""<section class="block" style="padding:110px 0"><div class="wrap">
  <div class="empty">
    <div class="icon" aria-hidden="true"><svg width="26" height="26" viewBox="0 0 24 24" fill="none"
      stroke="#136CFC" stroke-width="1.8" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg></div>
    <h3>That page could not be found</h3>
    <p>The address may have changed, or the page may not exist yet.</p>
    <p style="margin-top:14px"><a class="btn btn-primary" href="index.html">Back to the homepage</a></p>
  </div>
</div></section>""", active="index.html")

# ═══════════════════════════════ BUILD ═══════════════════════════════
FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
<rect width="32" height="32" rx="7" fill="#152641"/>
<path d="M7 24v-6M12.7 24V10M18.4 24v-8M24 24V8" stroke="#C3F84A" stroke-width="3"
 stroke-linecap="round"/></svg>"""

README = f"""# {COMPANY_NAME} — Official Website (static build)

Static marketing website for a South African business advisory firm, built from the approved
copy document ("Official Website Copy and Page Content — Business Advisory Firm").

**The public site contains site content only.** Every foundation, process, specification and
build-planning detail lives in [`docs/`](docs/README.md) — not on the website.

- **Stack:** plain HTML + CSS + a small amount of vanilla JS — no build step, no dependencies.
- **Design:** corporate colours `#136CFC` `#152641` `#C3F84A` `#E8F4FC`; Montserrat display &
  body (Baskerville retained as a token); flat editorial layouts with hairline rules.
- **Rendered by:** `generator/build_website.py` — `python3 generator/build_website.py <output-dir>`
  regenerates every page, the sitemap, robots.txt and this documentation.

## Branches

| Branch | Contents | Managed by |
|---|---|---|
| `main` | Default branch — this static website + documentation (web root) | The generator script |
| `static-site` | Same content, generator-managed mirror of `main` | The generator script |

Deploy on Vercel — configured in the repository (`vercel.json` + `scripts/build-vercel.sh`);
see docs/deployment.md. GitHub Pages also works: deploy from `main`, folder `/`.

## Pages

| Group | Files |
|---|---|
| Core | `index.html`, `about.html`, `services.html`, `research-publications.html`, `insights.html`, `contact.html`, `faq.html` |
| Divisions | `business-intelligence-performance-analytics.html`, `economic-commercial-intelligence.html`, `operational-risk-process-controls.html` |
| Services (9) | `business-data-diagnostic.html`, `business-intelligence-dashboard.html`, `monthly-performance-reporting.html`, `competitor-intelligence-snapshot.html`, `pricing-profitability-review.html`, `supplier-cost-watch.html`, `operational-risk-register.html`, `process-controls-diagnostic.html`, `compliance-evidence-organiser.html` |
| Legal (structure only) | `privacy-policy.html`, `website-terms.html`, `client-service-terms.html`, `publication-licence.html`, `refund-policy.html` |
| Other | `client-portal.html` (sign-in stub, noindex), `404.html`, `sitemap.xml`, `robots.txt`, `docs/`, `generator/`, `vercel.json`, `scripts/build-vercel.sh` (Vercel deployment) |

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
"""

# ═════════════════════════ REPOSITORY DOCUMENTATION ═══════════════════════════════
# Everything here is foundation/process material — it belongs in the repository, never on the
# public website. Content is taken from the approved copy document (§14–§19) plus build facts.

DOCS = {}

DOCS["docs/README.md"] = """# Documentation — project-blueprint (static site)

This folder holds everything that is **not part of the public website**: foundation material,
specifications, policies in preparation, build rules and deployment notes. The public website
(HTML pages at the root of this branch) contains site content only.

| Document | What it covers |
|---|---|
| [content-source-map.md](content-source-map.md) | Traceability: every section of the approved copy document → where it lives now |
| [website-map.md](website-map.md) | Page inventory, navigation model, deferred items |
| [client-portal-spec.md](client-portal-spec.md) | Client portal specification (§14) — separate authenticated interface |
| [internal-administration.md](internal-administration.md) | Internal administration specification (§15) — internal only, never public |
| [legal-page-structures.md](legal-page-structures.md) | Required structure of each policy page (§16) and what must be confirmed before finalisation |
| [cta-library.md](cta-library.md) | Call-to-action library (§17) |
| [seo-content.md](seo-content.md) | Search engine titles and descriptions (§18) |
| [implementation-rules.md](implementation-rules.md) | Final content and implementation rules (§19) and how this build complies |
| [commercial-policy.md](commercial-policy.md) | Payment policy and pricing rules |
| [deployment.md](deployment.md) | Hosting, branch strategy and the go-live checklist |

Source document: "Official Website Copy and Page Content — Business Advisory Firm" (19 sections).
Nothing on the public site may contradict it; nothing from §14 (portal) or §15 (internal
administration) belongs on the public site.
"""

DOCS["docs/content-source-map.md"] = """# Content source map

The approved copy document has 19 sections. This table records where each one is applied.

| § | Content | Where it lives now |
|---|---|---|
| 1 | Global elements (main navigation, footer) | Header/footer of every page |
| 2 | Homepage | `index.html` |
| 3 | About us | `about.html` |
| 4 | Services overview | `services.html` |
| 5 | Division 1 — Business Intelligence & Performance Analytics | `business-intelligence-performance-analytics.html` |
| 6 | Division 2 — Economic & Commercial Intelligence | `economic-commercial-intelligence.html` |
| 7 | Division 3 — Operational Risk, Process & Controls Advisory | `operational-risk-process-controls.html` |
| 8 | Nine individual service pages | One page per service — see [website-map.md](website-map.md) |
| 9 | Research publications page | `research-publications.html` (catalogue empty state until products are approved) |
| 10 | Individual publication template | Deferred — pages are created only when a publication is completed and approved (rule 19.7) |
| 11 | Insights page | `insights.html` (empty state; article structure per copy document) |
| 12 | Contact page | `contact.html` |
| 13 | Frequently asked questions | `faq.html` |
| 14 | Client portal content | **Not on the public site** — sign-in stub only; full spec in [client-portal-spec.md](client-portal-spec.md) |
| 15 | Internal administration content | **Not on the public site** — [internal-administration.md](internal-administration.md) |
| 16 | Legal and policy page structures | Five legal pages (structure only) + [legal-page-structures.md](legal-page-structures.md) |
| 17 | CTA library | Applied across pages; reference in [cta-library.md](cta-library.md) |
| 18 | Search engine content | Applied as page titles/descriptions; reference in [seo-content.md](seo-content.md) |
| 19 | Final content and implementation rules | Applied during the build; recorded in [implementation-rules.md](implementation-rules.md) |

Placeholders on the public site: `[Company Name]`, `[Company Email]`, `[Company Telephone]`,
`[Publication Title]` (template only). They are replaced once the firm confirms the real details
(rule 19.4 — do not invent).
"""

DOCS["docs/website-map.md"] = """# Website map — static-site branch

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
"""

DOCS["docs/client-portal-spec.md"] = """# Client portal specification

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
"""

DOCS["docs/internal-administration.md"] = """# Internal administration specification

Source: copy document §15. The internal administration system uses a professional,
information-dense interface. **It is not a public-facing website** and must never be exposed on
the public site. All client and administrative areas must be protected by appropriate
authentication and access controls (rule 19.15).

## Main navigation

Overview · Enquiries · Leads · Clients · Quotations · Projects · Services · Publications ·
Insights · Invoices · Payments · Orders · Documents · Communications · Users & Permissions ·
Reports · Settings · Audit Logs.

## Dashboard — "Business Overview"

Show relevant operational information: new enquiries; enquiries awaiting review; quotations
awaiting acceptance; active engagements; projects requiring attention; outstanding invoices;
recent payments; research publication sales; recent client activity.

All figures must be generated from actual database records. Do not display invented sample
statistics in production.

## Enquiry management

Administrators can: view enquiries; assign an owner; categorise enquiries; record follow-up
actions; change enquiry status; convert suitable enquiries into leads or clients; record reasons
for declining an enquiry.

## Service management

Administrators can: add and edit services; assign services to divisions; manage service
descriptions; define packages and scope; set internal pricing; manage service availability;
publish or unpublish services.

## Publication management

Administrators can: create publications; add cover images; upload publication files; add
previews; set prices; assign categories; define licences; publish and unpublish products; manage
publication versions; correct or withdraw a publication where necessary.

## Project management

Administrators can: create projects; assign responsible personnel; define milestones; track
tasks; record client requests; upload deliverables; record consultations; maintain project
activity history.

## Finance administration

Administrators can: create invoices; record payment requirements; view confirmed transactions;
reconcile payment records; record refunds; issue receipts; monitor outstanding balances.

Payment confirmation must be based on verified transaction information, not manual assumptions.
"""

DOCS["docs/legal-page-structures.md"] = """# Legal and policy page content structures

Source: copy document §16. Each page must exist as a separate page; final wording must be
reviewed and approved before publication (rule 19.18 — do not publish draft legal documents as
final policies). Until then, the public pages show their required section structure with a short
neutral notice; the finalisation requirements below live here, not on the website.

## 16.1 Privacy Policy — required sections

1. Introduction and responsible party. 2. Personal information collected. 3. How information is
collected. 4. Purposes of processing. 5. Lawful basis and applicable conditions. 6. Information
sharing and service providers. 7. Cross-border processing, where applicable. 8. Information
security. 9. Retention and deletion. 10. Data subject rights. 11. Marketing communications.
12. Cookies and analytics. 13. Contact details for privacy enquiries. 14. Policy updates.

**Before finalisation:** the company must confirm its legal identity, contact details, actual
data practices, retention arrangements, operators and any cross-border processing.

## 16.2 Website Terms & Conditions — required sections

1. Acceptance of terms. 2. Website access and permitted use. 3. Intellectual property.
4. Website content and accuracy. 5. Third-party services and links. 6. User submissions.
7. Website availability. 8. Limitation of liability, subject to applicable law. 9. Changes to the
website and terms. 10. Governing law and dispute handling. 11. Contact information.

## 16.3 Client Service Terms — required sections

1. Definitions. 2. Enquiries and initial discussions. 3. Quotations and acceptance. 4. Scope of
work. 5. Client responsibilities. 6. Fees and payment terms. 7. Commencement of work. 8. Timelines
and dependencies. 9. Changes to scope. 10. Consultations and communication. 11. Deliverables and
revisions. 12. Confidentiality. 13. Client information and system access. 14. Intellectual
property. 15. Third-party costs. 16. Cancellation and termination. 17. Limitation of
responsibility. 18. Dispute resolution. 19. Applicable law.

## 16.4 Research Publication Licence — required sections

1. Licence grant. 2. Permitted internal use. 3. Restrictions on redistribution. 4. Restrictions
on resale. 5. Restrictions on republication. 6. Organisational and multi-user licences.
7. Copyright and attribution. 8. Publication limitations. 9. Updates and corrections.
10. Breach of licence. 11. Contact information.

## 16.5 Digital Product Refund and Cancellation Policy — required sections

1. Scope of policy. 2. Digital product descriptions. 3. Purchase confirmation. 4. Download and
access. 5. Technical problems. 6. Duplicate transactions. 7. Incorrect charges. 8. Refund request
process. 9. Cancellation conditions. 10. Applicable consumer rights. 11. Contact details.

**Before finalisation:** check the policy against applicable South African consumer law. Do not
state that all digital products are automatically non-refundable.

## 16.6 Cookie Policy

Where cookies or similar technologies are used, explain: essential cookies; functional cookies;
analytics cookies; marketing cookies (if applicable); cookie controls; third-party services;
retention periods. Only describe cookies and tracking technologies actually implemented. No
cookie policy page exists yet because no cookies or analytics are implemented — create it when
they are introduced.
"""

DOCS["docs/cta-library.md"] = """# Website call-to-action library

Source: copy document §17. Use clear, relevant calls to action rather than repeating the same
generic button everywhere. Every CTA must lead to a real, functioning destination (rule 19.12).

| Page or context | CTA |
|---|---|
| Homepage | Discuss Your Business Needs |
| Services overview | Explore Our Services |
| BI division | Discuss Your Business Information Needs |
| Data Diagnostic | Request a Business Data Diagnostic |
| Dashboard | Request a Dashboard |
| Monthly Reporting | Discuss Monthly Reporting |
| ECI division | Discuss a Commercial Research Requirement |
| Competitor Intelligence | Request Competitor Intelligence |
| Pricing Review | Request a Pricing Review |
| Supplier Cost Watch | Discuss Supplier Cost Monitoring |
| Risk division | Discuss an Operational Challenge |
| Risk Register | Request an Operational Risk Register |
| Process Diagnostic | Request a Process Diagnostic |
| Evidence Organiser | Request a Compliance Evidence Review |
| Research catalogue | Browse Publications |
| Publication page | Purchase Publication |
| Insights article | Explore Related Research |
| Contact | Submit Enquiry |
"""

DOCS["docs/seo-content.md"] = """# Search engine content

Source: copy document §18. Use unique page titles and descriptions. The generator produces a
unique title and meta description for every page; the homepage values are:

- **Homepage title:** [Company Name] | Business Advisory Firm South Africa
- **Homepage description:** Business intelligence, economic and commercial research, performance
  analytics and operational risk advisory services for businesses across South Africa.

Reference titles for the other core pages:

| Page | Title pattern |
|---|---|
| About | About [Company Name] | Business Advisory & Research |
| Services | Business Advisory Services | [Company Name] |
| BI division | Business Intelligence & Performance Analytics | [Company Name] |
| ECI division | Economic & Commercial Intelligence | [Company Name] |
| Risk division | Operational Risk, Process & Controls Advisory | [Company Name] |
| Research | Research Publications & Intelligence Products | [Company Name] |
| Insights | Business and Economic Insights | [Company Name] |
| Contact | Contact [Company Name] | Business Advisory South Africa |

Each individual service and publication page has its own unique title and description based on
its actual content. Canonical URLs point to the hosting URL (see deployment.md); update the
`SITE_URL` constant when the final domain is known.
"""

DOCS["docs/implementation-rules.md"] = """# Final content and implementation rules — build compliance

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
"""

DOCS["docs/commercial-policy.md"] = """# Commercial policy — reference

This records the commercial rules that govern the website copy. The public statements below are
approved copy (FAQ and Client Service Terms); the build rules keep the site compliant.

## Public statements (approved copy)

- **Payment policy:** engagements below R2,000 are payable in full upfront. Engagements of
  R2,000 or more require a 50% deposit and a 50% final payment.
- **Commencement:** work begins after the quotation and engagement terms are accepted, required
  onboarding information is received and the applicable initial payment is confirmed.
- **Travel and fieldwork costs** are not automatically included; applicable travel,
  accommodation, fieldwork or external specialist costs are identified in the quotation.
- **Integrations, software licences and continuing maintenance** are separate unless expressly
  agreed in the engagement terms.

## Build rules

- No provisional service prices are published anywhere on the public site (rule 19.6).
- ZAR currency formatting and South African English conventions (rule 19.17).
- Research publications are sold with the licence shown per product; access is restricted to the
  purchasing account or organisation (client-portal-spec.md §14.10).
"""

DOCS["docs/deployment.md"] = """# Deployment and repository guide

## Repository

GitHub: `Refilwe-Molapisi/project-blueprint` (private).

| Branch | Contents | Managed by |
|---|---|---|
| `main` | Default branch: this static website + documentation (web root) | `generator/build_website.py` |
| `static-site` | Same content, generator-managed mirror of `main` | `generator/build_website.py` |

## Hosting options for the static site

1. **Vercel (primary — configured in the repository)** — the repository ships
   `vercel.json` and `scripts/build-vercel.sh`, so importing the repo is all the setup there
   is. No environment variables, no framework, no Node build:
   - On Vercel: Add New… → Project → import `Refilwe-Molapisi/project-blueprint`. The
     framework preset "Other" is detected automatically; leave Build & Output Settings on the
     defaults — they are overridden by `vercel.json` (build command `sh scripts/build-vercel.sh`,
     output directory `dist/`). Deploy.
   - The build script assembles only the web-root files into `dist/`: all 26 pages (including
     `index.html` and `404.html` — Vercel serves `404.html` automatically for unknown paths),
     `assets/`, `robots.txt` and `sitemap.xml`.
   - Deliberately NOT deployed: `docs/`, `generator/`, `README.md` and the build script itself.
     `docs/` is internal documentation (implementation rules, internal-administration and
     client-portal specs) — on a public deployment URL, the `robots.txt` disallow alone would
     not keep it from being fetched directly. If the documentation should be online too, add a
     `docs/` copy in `scripts/build-vercel.sh`.
   - `vercel.json` adds security headers to every response (`X-Content-Type-Options`,
     `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy`) and one-day browser caching
     for `/assets/`. Links keep their `.html` form (`cleanUrls` stays off) so the generated
     hrefs, the sitemap and the canonical tags all resolve without redirects.
   - After the first deploy, Vercel assigns a `*.vercel.app` domain. Once the final domain is
     chosen, update `SITE_URL` in the generator and regenerate — see checklist item 7.
2. **GitHub Pages (alternative)** — Settings → Pages → Deploy from a branch → Branch `main`,
   folder `/ (root)` → Save. Notes:
   - The automation token used for pushing can create branches and push code but cannot change
     Pages settings (fine-grained PAT permission), so this toggle is a one-time manual step.
   - Pages serves every file in the branch — including `docs/` and `generator/` — so this
     option would publish the repository documentation at direct URLs as well.
   - Expected URL: `https://refilwe-molapisi.github.io/project-blueprint/` — the canonical tags
     on every page currently point there. Update the `SITE_URL` constant in the generator when
     the final domain is known and regenerate.

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
7. Domain: after the Vercel project exists, set `SITE_URL` in the generator to the final
   address (the `*.vercel.app` domain or a custom domain), regenerate and re-push — canonical
   tags, Open Graph URLs and the sitemap derive from it. For a custom domain, also add it under
   the Vercel project's Settings → Domains and point DNS.

## Regenerating the site

    python3 generator/build_website.py <output-dir>

Every page, `assets/`, `sitemap.xml`, `robots.txt`, `README.md`, this `docs/` folder,
`vercel.json` and `scripts/build-vercel.sh` are rewritten from the script. Replace the
corresponding files in this branch and commit.
"""

VERCEL_JSON = """{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "outputDirectory": "dist",
  "buildCommand": "sh scripts/build-vercel.sh",
  "cleanUrls": false,
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "X-Frame-Options", "value": "SAMEORIGIN" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" },
        { "key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()" }
      ]
    },
    {
      "source": "/assets/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=86400" }
      ]
    }
  ]
}
"""

VERCEL_BUILD = """#!/bin/sh
# Vercel build step: assembles the deployable web root into dist/.
#
# The repository root also holds repository-only files — docs/ (internal
# documentation), generator/ (site source), README.md and this script. Those
# are deliberately NOT deployed; only the website itself goes into dist/.
# See docs/deployment.md. To publish the docs too, add a docs/ copy below.
set -eu

rm -rf dist
mkdir -p dist

cp ./*.html dist/          # all pages, including index.html and 404.html
cp ./robots.txt ./sitemap.xml dist/
cp -R ./assets dist/       # style.css, site.js, favicon.svg
"""


def main():
    os.makedirs(f"{OUT}/assets", exist_ok=True)
    os.makedirs(f"{OUT}/docs", exist_ok=True)
    with open(f"{OUT}/assets/style.css", "w") as f: f.write(CSS)
    with open(f"{OUT}/assets/site.js", "w") as f: f.write(JS)
    with open(f"{OUT}/assets/favicon.svg", "w") as f: f.write(FAVICON)
    with open(f"{OUT}/.gitignore", "w") as f:
        f.write(".DS_Store\nThumbs.db\nsite-output/\ndist/\n*.log\n")
    os.makedirs(f"{OUT}/scripts", exist_ok=True)
    with open(f"{OUT}/vercel.json", "w") as f: f.write(VERCEL_JSON)
    with open(f"{OUT}/scripts/build-vercel.sh", "w") as f: f.write(VERCEL_BUILD)
    os.chmod(f"{OUT}/scripts/build-vercel.sh", 0o755)
    for fname, (title, desc, body, active, extra_head) in PAGES.items():
        with open(f"{OUT}/{fname}", "w") as f:
            f.write(shell(fname, title, desc, body, active, extra_head=extra_head))
    with open(f"{OUT}/README.md", "w") as f: f.write(README)
    for path, content in DOCS.items():
        with open(f"{OUT}/{path}", "w") as f: f.write(content)
    # sitemap (public pages only — portal stub and 404 excluded) + robots
    urls = ["" if f == "index.html" else f for f in PAGES
            if f not in ("404.html", "client-portal.html")]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in sorted(urls):
        sm.append(f"  <url><loc>{SITE_URL}{u}</loc></url>")
    sm.append("</urlset>")
    with open(f"{OUT}/sitemap.xml", "w") as f: f.write("\n".join(sm))
    with open(f"{OUT}/robots.txt", "w") as f:
        f.write("User-agent: *\nAllow: /\nDisallow: /docs/\n\n"
                f"Sitemap: {SITE_URL}sitemap.xml\n")
    print(f"built {len(PAGES)} pages + assets into {OUT}")

    # ── validation: internal links must resolve ──
    import re
    targets = set(PAGES) | {"assets/style.css", "assets/site.js", "assets/favicon.svg",
                            "sitemap.xml", "robots.txt"}
    broken = []
    for fname in PAGES:
        html = open(f"{OUT}/{fname}").read()
        for href in re.findall(r'(?:href|src)="([^"#?]+)[^"]*"', html):
            if href.startswith(("http", "mailto:", "data:", "tel:")):
                continue
            if href not in targets:
                broken.append(f"{fname} → {href}")
    print("broken internal links:", broken if broken else "none")
    leftover = []
    for fname in PAGES:
        html = open(f"{OUT}/{fname}").read()
        for bad in ("TODO", "undefined", "NaN", "{{", "}}"):
            if bad in html:
                leftover.append(f"{fname}: {bad}")
    print("leftover markers:", leftover if leftover else "none")
    if broken:
        raise SystemExit("fix broken links before shipping")

if __name__ == "__main__":
    main()
