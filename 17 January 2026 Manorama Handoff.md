# UI/UX DESIGNER HANDOFF DOCUMENT
### Freight & Logistics Website — Full Site Specification
> **Reference brand:** Maersk (maersk.com) — match their authority, clarity, and visual weight.
> **Status:** Designer-ready. Every section below is actionable.

---

# PART A — DESIGN SYSTEM (GLOBAL)

## Colors

| Token | HEX | Usage |
|---|---|---|
| Primary Navy | `#00315B` | Headings, footer bg, dark sections |
| Primary Blue | `#0358A0` | Icons, links, accents, card highlights |
| Blue Light | `rgba(3,88,160,0.10)` | Icon container bg, hover tints |
| Accent Orange | `#E8450A` | Primary CTA buttons only |
| Accent Orange Hover | `#C93A07` | CTA hover state |
| Background | `#FFFFFF` | Page background |
| Surface | `#F8F9FB` | Alternate section bg, card bg |
| Border | `#F3F4F6` | Card borders, dividers |
| Text Primary | `#00315B` | Headings |
| Text Body | `#474646` | Body copy |
| Text Muted | `#8A8F98` | Captions, meta, labels |
| Text White | `#FFFFFF` | On dark sections |
| Success | `#1A7A4A` | Form success state |
| Error | `#D93025` | Validation errors |
| Overlay Dark | `rgba(0,49,91,0.72)` | Hero image overlay |

---

## Typography

| Role | Font | Weight | Size (desktop) | Size (mobile) | Line Height | Letter Spacing |
|---|---|---|---|---|---|---|
| Display / Hero H1 | Inter | Black (900) | 52px | 32px | 1.1 | -0.02em |
| Section Heading H2 | Inter | Bold (700) | 38px | 26px | 1.15 | -0.01em |
| Subsection Heading H3 | Inter | SemiBold (600) | 22px | 18px | 1.5 | 0 |
| Body Large | Inter | Regular (400) | 17px | 16px | 1.65 | 0 |
| Body | Inter | Regular (400) | 15px | 15px | 1.5 | 0 |
| Caption / Meta | Inter | Light (300) | 13px | 12px | 1.4 | 0.01em |
| Button | Instrument Sans | Bold (700) | 15px | 15px | 1 | 0.02em |
| Eyebrow / Tag | Instrument Sans | Regular (400) | 12px | 12px | 1 | 0.1em UPPERCASE |
| Stat Number | Inter | Black (900) | 48px | 36px | 1 | -0.02em |
| Nav Link | Inter | Medium (500) | 14px | 15px | 1 | 0 |

---

## Spacing System

Base unit: **8px**

| Token | Value | Usage |
|---|---|---|
| xs | 4px | Icon gaps, tight internal |
| sm | 8px | Between inline elements |
| md | 16px | Card padding unit |
| lg | 24px | Between form fields, small gaps |
| xl | 32px | Card padding, section internal |
| 2xl | 48px | Between content groups |
| 3xl | 64px | Section top/bottom padding (mobile) |
| 4xl | 96px | Section top/bottom padding (desktop) |
| 5xl | 128px | Hero vertical padding |

---

## Border Radius

| Context | Radius |
|---|---|
| Cards | 14px |
| Buttons | 8px |
| Icon containers | 10px |
| Inputs / fields | 8px |
| Image crops | 12px |
| Pill tags | 999px |

---

## Shadows

| Name | Value |
|---|---|
| Card | `0px 1px 1.5px rgba(0,0,0,0.10), 0px 1px 1px rgba(0,0,0,0.10)` |
| Card hover | `0px 8px 24px rgba(0,49,91,0.12)` |
| Modal | `0px 20px 60px rgba(0,0,0,0.20)` |
| Button | none (flat) |

---

## Icons

- Library: Lucide Icons (stroke style)
- Style: Outlined / stroke, NO fill
- Stroke width: 2px
- Default color: `#0358A0`
- Standard sizes: 20px (inline), 24px (card), 32px (feature)
- Icon containers: 48×48px, `bg rgba(3,88,160,0.10)`, `border-radius 10px`

---

## Buttons

### Primary CTA
- Background: `#E8450A`
- Text: white, Instrument Sans Bold, 15px, uppercase
- Padding: 14px 28px
- Radius: 8px
- Hover: `#C93A07`, slight lift (`translateY(-1px)`)
- Active: `#A83205`
- Disabled: 40% opacity, cursor not-allowed
- Loading: spinner icon replaces label, disabled state

### Secondary (Outlined)
- Border: 1.5px `#0358A0`
- Text: `#0358A0`, Instrument Sans Bold, 15px
- Background: transparent
- Hover: `bg rgba(3,88,160,0.06)`

### Ghost / Text Link
- Text: `#0358A0`
- Underline on hover
- No background, no border

---

## Global Layout

| Property | Value |
|---|---|
| Max content width | 1280px |
| Page horizontal margins | 80px (desktop), 40px (tablet), 20px (mobile) |
| Grid | 12 columns, 24px gutter |
| Navbar height | 72px |
| Section padding top/bottom | 96px desktop, 64px mobile |

---

## Breakpoints

| Name | Width |
|---|---|
| Mobile | ≤ 639px |
| Tablet | 640px – 1023px |
| Desktop | ≥ 1024px |
| Wide | ≥ 1280px |

---

# PART B — GLOBAL COMPONENTS

## Navbar

### Contents (left → right)
1. Logo (left-aligned) — company wordmark/logo SVG, height 36px
2. Nav links (centered): Services ▾ | About | Tracking | Contact
3. Right: Phone/contact icon | **"Request a Quote"** button (Primary CTA, orange)

### "Services" Mega-dropdown
- Triggered on hover/click of "Services" nav link
- Full-width dropdown panel, white bg, 1px border bottom `#F3F4F6`, shadow below
- Grid: 4 columns — one per service
- Each column: icon (24px, blue) + service name (Inter SemiBold 14px, navy) + one-line description (Inter Regular 12px, muted)
- Hover state on each item: blue tint background `rgba(3,88,160,0.05)`

### Scrolled State
- Default: transparent bg over hero image
- After 60px scroll: white bg, `box-shadow 0 2px 16px rgba(0,0,0,0.08)`, smooth 200ms transition
- Logo: always visible in full color

### Mobile Menu
- Hamburger icon (right side, 24px)
- Full-screen drawer slides from right
- Accordion for Services (taps to expand list)
- CTA button full width at bottom of drawer

---

## Footer

### Layout (4 columns on desktop, stacked on mobile)
1. **Column 1 — Brand:** Logo, company tagline (2 lines max), social icons (LinkedIn, Twitter/X, Facebook)
2. **Column 2 — Services:** Sea Freight | Transportation | Warehouse | CFS & Projects | Air Freight | Customs Clearance
3. **Column 3 — Company:** About Us | Our Team | Projects & Updates | Careers | Contact
4. **Column 4 — Support:** Request a Quote | Track Your Request | FAQ | Privacy Policy | Terms of Service

### Bottom bar
- Left: © 2024 [Company Name]. All rights reserved.
- Right: Privacy | Terms

### Background: `#00315B` (navy). All text white or `rgba(255,255,255,0.6)` for muted.

---

## Value Cards (Reusable component — seen in designs)

```
┌─────────────────────────────────┐
│  [Icon container 48×48]         │  ← top-left, 32px from edges
│                                 │
│  [Heading — Inter SemiBold 22px]│  ← 96px from top
│                                 │
│  [Body copy — 15px, 3 lines max]│  ← 137px from top
└─────────────────────────────────┘
```

- Card: white bg, `border 0.667px #F3F4F6`, `border-radius 14px`, card shadow
- Width: 388px (desktop), fluid on tablet/mobile
- Min-height: 220px

---

# PART C — SITE STRUCTURE

```
NAVBAR (sticky, global)
│
├── HOME (Landing Page — existing)
│
├── SERVICES
│   ├── Sea Freight
│   ├── Transportation
│   ├── Warehouse & Storage
│   ├── CFS & Projects
│   ├── Air Freight            ← suggested addition
│   └── Customs Clearance      ← suggested addition
│
├── TRACKING (Request status lookup)
│
├── ABOUT US
│
├── PROJECTS & UPDATES (Blog/News)
│
└── CONTACT
```

---

---

# PART D — SERVICE PAGES

> All service pages share the same **page template** with service-specific content swapped in.
> Design one master template in Figma then duplicate and fill per service.

---

## SERVICE PAGE TEMPLATE STRUCTURE

```
NAVBAR
↓
HERO BAND (service-specific)
↓
WHAT WE OFFER
↓
HOW IT WORKS (process steps)
↓
STRONG POINTS / VALUE PROPS
↓
MAJOR CUSTOMERS (logos + quote)
↓
WHY CHOOSE US FOR THIS SERVICE
↓
QUOTE REQUEST CTA BAND
↓
FOOTER
```

---

## SECTION: SERVICE HERO BAND

### Purpose
Immediately orient the visitor to which service they're on. Establish authority.

### Layout
- Full-width image band, height: 480px desktop / 320px mobile
- Dark overlay `rgba(0,49,91,0.68)` over service-specific photography
- Content: left-aligned, vertically centered

### Content
```
[Eyebrow — 12px, uppercase, Inter Regular, white 70% opacity]
e.g., "OUR SERVICES / SEA FREIGHT"

[H1 — Inter Black, 52px desktop / 32px mobile, white]
e.g., "Global Sea Freight Solutions"

[Subheadline — Inter Regular, 18px, white 85% opacity, max 420px wide]
e.g., "End-to-end ocean freight from origin to destination,
with full visibility every step of the way."

[Primary CTA — orange button]
"Request a Quote →"

[Secondary CTA — ghost button, white border]
"Learn How It Works"
```

### Important
- Photography must show the specific service (container ships for sea freight, trucks for transport, etc.)
- Never use the same hero image across two service pages
- H1 is the SEO heading — must be text, never baked into image

---

## SECTION: WHAT WE OFFER

### Purpose
Concrete breakdown of what's included in this service. No vague language.

### Layout
- White background section
- Left: heading + intro paragraph (5-col)
- Right: feature grid (7-col), 2×3 grid of feature items

### Feature Item structure (no card border — clean grid)
```
[Icon 24px, blue]  [Feature name — Inter SemiBold 16px, navy]
                   [One-line description — Inter Regular 14px, muted]
```

### Content structure
**Section eyebrow:** "WHAT WE OFFER"
**H2:** Service-specific (see per-service below)
**Intro paragraph:** 2–3 sentences, no jargon

---

## SECTION: HOW IT WORKS

### Purpose
Reduce anxiety. Show the process is clear, managed, and predictable.

### Layout
- Surface background `#F8F9FB`
- Centered, max 900px wide
- Horizontal step flow (desktop) / vertical accordion (mobile)

### Step component
```
[Step number — circular badge, #0358A0 bg, white text, 36px]
        |
        | (connector line between steps)
        |
[Step title — Inter SemiBold 16px]
[Step description — Inter Regular 14px, 2–3 lines]
```

### Steps: 4–5 steps per service (see per-service content below)

---

## SECTION: STRONG POINTS / VALUE PROPS

### Purpose
Three value cards reinforcing why this company is excellent specifically at this service.

### Layout
- White background
- 3-column grid, each column is a Value Card (the component defined in Part B)
- Desktop: side by side | Tablet: 2 col + 1 below | Mobile: stacked

---

## SECTION: MAJOR CUSTOMERS

### Purpose
Social proof — show recognizable brands that trust this service.

### Layout
- Navy dark bg (`#00315B`)
- Top: "Trusted by industry leaders" — centered, H2 white
- Logo grid: 6 customer logos, grayscale white-tinted, 2 rows of 3 (desktop) or scrollable marquee (mobile)
- Below logos: one featured testimonial card

### Testimonial card
```
┌──────────────────────────────────────────────────────┐
│  " [Quote text — Inter Light 20px, white, max 540px] "│
│                                                      │
│  [Client photo 48px circle] [Name — SemiBold white]  │
│                             [Title — muted white]    │
└──────────────────────────────────────────────────────┘
```

---

## SECTION: WHY CHOOSE US (per service)

### Purpose
Service-specific differentiators. NOT generic "we care about quality" filler.

### Layout
- White left half (text) / Image right half (service photo) — 50/50 split, full bleed to edges
- Image: real operational photography, no stock clichés
- Content area left-aligned, vertically centered, 80px padding

### Content
```
[Eyebrow — "WHY CHOOSE US FOR [SERVICE NAME]"]
[H2 — specific claim, 2 lines max]
[Body — 2 sentences max]

[Differentiator list — 3–4 items]
  ✓ [Point — Inter SemiBold 15px, navy]
    [Supporting sentence — Inter Regular 14px, muted]

[CTA — "Request a Quote"]
```

---

## SECTION: QUOTE REQUEST CTA BAND

### Purpose
Final push — every service page ends with a direct CTA to the form.

### Layout
- Dark blue band (`#0358A0`), full width, 96px padding vertical
- Centered text + single CTA button

### Content
```
[H2 — white, Inter Bold]
"Ready to move your cargo?"

[Subtext — white 80% opacity, Inter Regular 17px]
"Tell us what you need and we'll get back to you within 24 hours."

[CTA — orange button, large]
"Request a Quote →"
```

---
---

# SERVICE 1 — SEA FREIGHT

## Hero
**Eyebrow:** OUR SERVICES / SEA FREIGHT
**H1:** Global Sea Freight Solutions
**Subheadline:** Full container, groupage, and breakbulk ocean shipping across major global trade lanes, with door-to-door visibility.
**Photo direction:** Aerial of container port or container ship at sea, warm afternoon light. High contrast. Blue and orange tones.

---

## What We Offer
**H2:** Complete Ocean Freight, Managed End-to-End

| Feature | Description |
|---|---|
| FCL (Full Container Load) | Dedicated containers for large shipments — 20ft, 40ft, 40ft HC |
| LCL (Less than Container Load) | Groupage service for smaller volumes — pay only for what you use |
| Breakbulk & Out-of-Gauge | Oversized and heavy cargo handled with specialized equipment |
| Reefer Containers | Temperature-controlled shipping for perishables and pharma |
| Hazardous Cargo | IMO-certified handling for dangerous goods |
| Port-to-Port & Door-to-Door | Flexible delivery terms: EXW through DDP |

---

## How It Works (Steps)
1. **Submit Your Request** — Tell us your origin, destination, cargo type, and volume
2. **Receive Your Quote** — We send a detailed quote within 24 hours
3. **Booking Confirmation** — We secure your container space and confirm the schedule
4. **Cargo Pickup & Loading** — Our team coordinates collection and port delivery
5. **Real-Time Tracking** — Monitor your shipment from departure to arrival
6. **Final Delivery** — Door delivery or port pickup — your choice

---

## Strong Points (3 Value Cards)
1. **Global Port Coverage** — Direct service to 120+ ports across 60 countries with established carrier partnerships
2. **Competitive Rates** — Volume-based pricing and consolidation options that reduce cost per unit
3. **Full Cargo Visibility** — Live container tracking from booking to delivery, no blind spots

---

## Major Customers (Sector focus)
- FMCG / Consumer Goods brands
- Manufacturing companies
- Agricultural exporters
- Retail chains with import operations
- Mining and resources sector
*(Replace with actual client logos when available)*

---

## Why Choose Us — Sea Freight
**H2:** A sea freight partner that moves at the speed of trade
**Differentiators:**
- 99.2% on-time vessel booking across all routes
- Direct contracts with top 10 global carriers — no broker markups
- Dedicated documentation team — BL, certificates of origin, customs paperwork handled
- 24/7 operations center for urgent shipments and rerouting

---
---

# SERVICE 2 — TRANSPORTATION (LAND / ROAD)

## Hero
**H1:** Inland & Cross-Border Transportation
**Subheadline:** Road freight solutions connecting ports, warehouses, and your customers — reliably, on time.
**Photo direction:** Convoy of branded trucks on highway, golden hour, wide open road. Blue sky.

---

## What We Offer
**H2:** Road Freight Built for Reliability at Scale

| Feature | Description |
|---|---|
| Full Truckload (FTL) | Dedicated truck for your cargo — faster, direct |
| Partial / Groupage (LTL) | Cost-share with other shippers on the same route |
| Last-Mile Delivery | Urban delivery coordination to your end customer |
| Port Drayage | Container transport from port to warehouse or client |
| Oversized & Heavy Haul | Permits, escorts, and specialized low-loaders |
| Cross-Border Freight | Documentation, customs, and border clearance managed |

---

## How It Works
1. **Request Submitted** — Origin, destination, weight, dimensions, timeline
2. **Quote in 24h** — Transparent pricing, no hidden fees
3. **Vehicle Assigned** — Right truck for your cargo, tracked GPS from dispatch
4. **Pickup** — Driver coordination and cargo verification
5. **In-Transit Updates** — Real-time location shared via tracking link or portal
6. **Delivered & POD Issued** — Proof of delivery sent immediately on completion

---

## Strong Points
1. **GPS-Tracked Fleet** — Every vehicle tracked live. You always know where your cargo is.
2. **Experienced Drivers** — Vetted, licensed, and trained for freight — not just package delivery
3. **Port-to-Anywhere** — Seamless handoff from our sea freight operations to road delivery

---

## Major Customers
- Importers needing port-to-warehouse last mile
- FMCG distributors
- Construction and infrastructure project operators
- Retailers needing replenishment runs

---

## Why Choose Us — Transportation
**H2:** From port gate to your warehouse door, without gaps
**Differentiators:**
- Owned fleet + vetted partner network — no blind subcontracting
- Average transit time 18% faster than industry benchmark on key corridors
- Single point of contact from sea booking through to last-mile delivery
- No minimum volume — FTL or a single pallet, same service standard

---
---

# SERVICE 3 — WAREHOUSE & STORAGE

## Hero
**H1:** Strategic Warehousing & Distribution
**Subheadline:** Secure, managed storage facilities positioned close to ports and key trade corridors — with inventory management built in.
**Photo direction:** Wide-angle interior of modern warehouse. Tall racking, clean floors, forklift in mid-frame. Cool industrial lighting.

---

## What We Offer
**H2:** More Than Storage — A Distribution Hub

| Feature | Description |
|---|---|
| Short-Term Storage | Flexible space for overflow, project cargo, or seasonal stock |
| Long-Term Storage | Contracted space with dedicated zone, inventory system access |
| Pick & Pack | Order fulfillment — pick, pack, label, and dispatch |
| Cross-Docking | Direct transfer from inbound to outbound — minimal storage time |
| Inventory Management | Real-time stock levels via our WMS (Warehouse Management System) |
| Bonded Warehouse | Duty-deferred storage for goods awaiting customs clearance |
| Cold Chain Storage | Temperature-controlled zones for food, pharma, and chemicals |

---

## How It Works
1. **Storage Inquiry** — Tell us cargo type, volume (CBM or pallets), duration
2. **Space Allocated** — We assign a zone in the nearest facility
3. **Inbound Receiving** — Cargo received, counted, and entered into WMS
4. **Storage & Monitoring** — 24/7 CCTV, access control, regular inventory reports
5. **Outbound Dispatch** — Pick, pack, label, load — per your instructions
6. **Reporting** — Monthly inventory report emailed to your operations team

---

## Strong Points
1. **Port-Adjacent Locations** — Facilities within 15km of major ports — reduces drayage cost and time
2. **Real-Time Inventory Access** — Client portal showing live stock levels, inbound/outbound history
3. **Flexible Terms** — Weekly, monthly, or annual contracts — scale up or down without penalty

---

## Major Customers
- Importers holding stock before distribution
- E-commerce businesses needing fulfillment centers
- Agricultural traders managing seasonal volumes
- Pharmaceutical companies requiring compliant cold chain storage

---

## Why Choose Us — Warehousing
**H2:** Your stock, visible and secure — always
**Differentiators:**
- Bonded + general warehouse under one roof — no need for multiple providers
- Integrated with our transportation fleet — seamless outbound coordination
- ISO-compliant facilities with fire suppression and 24/7 monitoring
- Dedicated account manager for inventory queries — not a call center

---
---

# SERVICE 4 — CFS & PROJECTS

## Hero
**H1:** Container Freight Station & Project Cargo
**Subheadline:** LCL consolidation, deconsolidation, and complex project logistics managed with precision.
**Photo direction:** Busy CFS facility — forklifts moving cargo, containers open, workers in hi-vis. Daytime, industrial.

---

## What We Offer
**H2:** Specialized Handling for Complex Cargo

| Feature | Description |
|---|---|
| LCL Consolidation (Stuffing) | Combine small shipments into one container — cost-efficient export |
| LCL Deconsolidation (Destuffing) | Break down incoming containers and sort per consignee |
| Project Cargo Management | End-to-end logistics for large, complex, or out-of-gauge shipments |
| Cargo Inspection & Verification | Third-party and pre-shipment inspection coordination |
| Repackaging & Labelling | Cargo repack, relabel, and compliance marking within the CFS |
| Fumigation & Treatment | Phytosanitary treatment, fumigation, and certification |
| Cargo Insurance Coordination | Coverage arranged per shipment value and risk profile |

---

## How It Works
1. **Cargo Arrival at CFS** — Received, verified, and logged on arrival
2. **Sorting & Staging** — Organized by consignee or consolidation group
3. **Stuffing / Destuffing** — Loaded into or extracted from containers efficiently
4. **Documentation** — Packing lists, cargo manifests, and certificates prepared
5. **Onward Dispatch** — Released to transport or stored per instruction
6. **Report Issued** — Full outturn report to shipper/consignee

---

## Strong Points
1. **In-House CFS Facility** — Not outsourced. Our team, our equipment, our responsibility.
2. **Project Cargo Expertise** — Handled mining equipment, industrial plant machinery, and government infrastructure cargo
3. **Complete Documentation** — Every consolidation comes with full manifest, packing list, and compliance certs

---

## Major Customers
- SME importers and exporters using LCL
- Mining and infrastructure project operators
- Government procurement agencies
- Aid and humanitarian organizations shipping mixed cargo

---

## Why Choose Us — CFS & Projects
**H2:** The partner for cargo too complex for standard freight
**Differentiators:**
- Project cargo team with 15+ years combined experience in out-of-gauge logistics
- CFS linked directly to our warehouse — seamless flow from destuff to storage
- Transparent per-CBM pricing on LCL — no surprise fees
- 48-hour outturn reports as standard — no chasing for updates

---
---

# SERVICE 5 — AIR FREIGHT *(Suggested addition)*

## Hero
**H1:** Express Air Freight Solutions
**Subheadline:** Time-critical shipments delivered to any global airport within your required window.
**Photo direction:** Cargo aircraft on tarmac at dusk, loading in progress. Dramatic lighting.

---

## What We Offer

| Feature | Description |
|---|---|
| Express Air (Next Flight Out) | Urgent, time-critical cargo on the next available flight |
| Standard Air Freight | Scheduled consolidation on established air routes |
| Airport-to-Airport | Basic airside service for freight-forwarding clients |
| Door-to-Door Air | Full pickup, airside handling, customs, and final delivery |
| Pharmaceutical & Cold Chain Air | Temperature-monitored airside handling and GDP-compliant transit |
| Charter Flights | Full aircraft charter for extremely urgent or oversized cargo |

---

## How It Works
1. **Request Quote** — Cargo dimensions, weight, origin/destination, required date
2. **Flight Selection** — We identify best routing and carrier for your timeline
3. **Pickup & Export Clearance** — Cargo collected, AWB issued, customs export handled
4. **In-Flight Tracking** — Airway bill tracking available from departure
5. **Import Clearance at Destination** — Handled by our in-country partner
6. **Final Delivery** — Airport pickup or door delivery

---

## Strong Points
1. **Speed as a Feature** — Next-flight-out capability on major corridors
2. **Pharma & Perishables Certified** — Temperature-controlled handling, chain of custody documentation
3. **No Cargo Left Behind** — Guaranteed space on confirmed bookings — no bumping

---

## Why Choose Us — Air Freight
**H2:** When time is the cargo
**Differentiators:**
- Priority relationships with major cargo carriers — not relying on passenger belly space
- Integrated customs clearance — one call, not five vendors
- 24/7 operations desk for overnight and emergency requests
- Full insurance cover arranged per shipment

---
---

# SERVICE 6 — CUSTOMS CLEARANCE *(Suggested addition)*

## Hero
**H1:** Customs Clearance & Compliance
**Subheadline:** Fast, accurate customs declarations that keep your cargo moving and your business compliant.
**Photo direction:** Customs officer reviewing documents at port gate, or close-up of official stamps on paperwork.

---

## What We Offer

| Feature | Description |
|---|---|
| Import Customs Clearance | Full declaration, classification, and duty payment on your behalf |
| Export Customs Clearance | Export entries, certificates of origin, and licensing compliance |
| Tariff Classification (HS Codes) | Expert classification to minimize duty and avoid compliance risk |
| Duty & Tax Consulting | Pre-import duty assessment and optimization |
| Customs Bond Management | Manage your customs bond portfolio and renewals |
| Trade Compliance Audits | Review your import/export activity for compliance gaps |
| Permit & License Management | Handle restricted, controlled, and licensed goods |

---

## How It Works
1. **Document Submission** — You send us commercial invoice, packing list, BL/AWB
2. **Classification Review** — We classify and verify HS codes and applicable duties
3. **Declaration Filing** — We file with the relevant customs authority electronically
4. **Duty Payment** — Duties and taxes paid on your behalf (reimbursed per agreement)
5. **Customs Release** — Cargo released and cleared for delivery
6. **Compliance Record** — Full entry documents issued and archived

---

## Strong Points
1. **Licensed Customs Brokers** — All declarations handled by certified, licensed personnel
2. **Zero Detention Policy** — Our accuracy rate means virtually no cargo held for re-examination
3. **Trade Lane Expertise** — Deep familiarity with regulations in your key import/export markets

---

## Why Choose Us — Customs
**H2:** Compliant. Fast. No surprises.
**Differentiators:**
- 99.1% first-submission clearance rate — your cargo doesn't wait for rework
- Proactive duty advice before you book — know your landed cost upfront
- Single integrated provider — customs is part of your freight booking, not a separate vendor
- Full digital record keeping — all entries searchable by clients in their portal

---
---

# PART E — QUOTE REQUEST FORM (FULL UX FLOW)

## Overview
A quote request is the **primary conversion** on this website. It must feel effortless, trustworthy, and professionally managed. The experience must communicate: *"A real expert is going to read this and respond."*

## Entry Points (All trigger the same form)
| CTA Location | CTA Text |
|---|---|
| Navbar (global, always visible) | "Request a Quote" |
| Hero — every service page | "Request a Quote →" |
| Quote CTA band — every service page | "Request a Quote →" |
| Home page hero | "Ask for Quotation" |
| Home page CTA band | "Get Started" |
| Footer | "Request a Quote" |

---

## Form UX: Open in Modal (Recommended)

**Why modal:** User stays on the page they came from. Context is preserved. Feels lightweight and fast. Consistent with Maersk's approach.

### Modal dimensions
- Desktop: 620px wide, centered, max-height 90vh with internal scroll
- Mobile: Full-screen, slides up from bottom (drawer pattern)
- Overlay: `rgba(0,0,0,0.50)` blur backdrop
- Close: × in top-right corner, clicking backdrop also closes

---

## FORM STRUCTURE

### Step 1 of 2 — Shipment Details

**Section header:** "Tell us about your shipment"
**Subheader (muted):** "We'll review and respond within 24 hours."

| Field | Type | Required | Placeholder | Validation |
|---|---|---|---|---|
| Service Type | Select / Toggle | Yes | "Select a service" | Must select one |
| Origin (Port / City) | Text | Yes | "e.g. Mombasa, Kenya" | Min 2 chars |
| Destination (Port / City) | Text | Yes | "e.g. Rotterdam, Netherlands" | Min 2 chars |
| Cargo Description | Textarea | Yes | "e.g. 2x 40ft containers of bagged maize" | 10–500 chars |
| Estimated Weight (KG) | Number | No | "e.g. 24,000" | Positive number |
| Estimated Volume (CBM) | Number | No | "e.g. 42" | Positive number |
| Incoterms | Select | No | "e.g. FOB, CIF, EXW" | — |
| Preferred Shipment Date | Date picker | No | "Select date" | Not in past |
| Additional Notes | Textarea | No | "Any special requirements..." | 0–500 chars |

**Service Type options (rendered as selectable chip buttons, not a dropdown):**
Sea Freight | Transportation | Warehouse | CFS & Projects | Air Freight | Customs Clearance | Not Sure

**"Next →"** button (primary, orange) — validates Step 1 before proceeding

---

### Step 2 of 2 — Your Contact Details

**Section header:** "How should we reach you?"

| Field | Type | Required | Placeholder | Validation |
|---|---|---|---|---|
| Full Name | Text | Yes | "Your full name" | Min 2 chars |
| Company Name | Text | No | "Company (optional)" | — |
| Email Address | Email | Yes | "your@email.com" | Valid email format |
| Phone Number | Tel | Yes | "+254 700 000 000" | Min 8 digits, allow + |
| Country | Select | Yes | "Select your country" | Must select |
| How did you hear about us? | Select | No | "Optional" | — |

**Submit CTA:** "Submit Request →" (primary orange, full width on mobile)
**Below CTA:** *"By submitting, you agree to our Privacy Policy. We will only use your details to respond to this request."*

---

## Progress Indicator
- Top of modal: Step indicator
```
[●]─────────[○]
Step 1        Step 2
Shipment    Contact
Details     Details
```
- Active step: `#0358A0` filled circle
- Inactive: hollow circle, muted
- Connector line: `#F3F4F6`

---

## Field Design States

### Empty
- Border: `1px #E5E7EB`
- Background: white
- Label: 12px Inter Medium, navy, above field
- Placeholder: 15px Inter Regular, `#8A8F98`

### Focus
- Border: `2px #0358A0`
- Light blue shadow: `0 0 0 3px rgba(3,88,160,0.12)`
- Label: shifts to blue `#0358A0`

### Filled
- Border: `1px #9CA3AF`
- Text: `#00315B` Inter Regular

### Error
- Border: `2px #D93025`
- Error message below field: 12px Inter Regular, red `#D93025`, with ⚠ icon
- Shake animation (150ms) on failed submit attempt

### Disabled
- Background: `#F3F4F6`
- Text: `#8A8F98`

---

## Validation Behavior
- **When:** On blur per field (immediate) + on submit (full form scan)
- **Error display:** Inline below each field — never a generic toast
- **On submit failure:** Scroll to first error field automatically, fields shake once
- **Success:** No per-field confirmation shown (avoid over-engineering)

---

## Submission Flow (Complete Lifecycle)

```
User clicks "Submit Request →"
↓
Client-side validation runs
  └─ If errors → highlight fields, scroll to first, stop here
↓
Submit button: disabled + shows spinner + text changes to "Submitting..."
↓
POST request sent to backend
↓
[BACKEND PROCESSING]
  ├── Generate unique Request ID (format: FRQ-YYYYMMDD-XXXX, e.g. FRQ-20240315-4821)
  ├── Record request in database with status: PENDING
  ├── Send notification email to ops team
  └── Return: { requestId, submittedAt, status }
↓
UI receives success response
↓
SHOW: SUCCESS STATE (see below)
```

---

## SUCCESS STATE

Modal content replaces form content (no navigation — stays in modal).

### Visual Design
```
┌─────────────────────────────────────────────┐
│                                             │
│        [✓ icon — large, #1A7A4A, 64px]      │
│                                             │
│   Request Submitted Successfully            │
│   [Inter Bold 22px, navy]                   │
│                                             │
│   Your Request ID:                          │
│   [FRQ-20240315-4821]                       │
│   [Inter Black 28px, #0358A0, monospace]    │
│   [Copy icon next to ID]                    │
│                                             │
│   ─────────────────────────────────────     │
│                                             │
│   Our team will review your request and     │
│   contact you within 24 hours on:           │
│   [user's email — bold]                     │
│                                             │
│   [!] This is a request, not a confirmed    │
│   booking. We will contact you to confirm.  │
│   [amber info banner, Inter Regular 13px]   │
│                                             │
│   ─────────────────────────────────────     │
│                                             │
│   [⬇ Download Your Request Receipt]         │
│   [Secondary outlined button, full width]   │
│                                             │
│   [Track Your Request Status →]             │
│   [Ghost text link, #0358A0, center]        │
│                                             │
└─────────────────────────────────────────────┘
```

---

## RECEIPT DOWNLOAD

### Trigger
User clicks "Download Your Request Receipt" — immediately downloads a PDF. No second click, no email required.

### Receipt PDF Layout (A4, portrait)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[COMPANY LOGO — left]           [DATE — right]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FREIGHT QUOTE REQUEST RECEIPT

Request ID:       FRQ-20240315-4821
Status:           PENDING — Awaiting Review
Submitted:        15 March 2024, 14:32 UTC

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SHIPMENT DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Service:          Sea Freight
Origin:           Mombasa, Kenya
Destination:      Rotterdam, Netherlands
Cargo:            2x 40ft containers of bagged maize
Weight:           48,000 KG
Volume:           84 CBM
Incoterms:        FOB
Preferred Date:   01 April 2024
Notes:            Requires fumigation certificate

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONTACT DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Name:             John Kamau
Company:          Kamau Agro Exports Ltd
Email:            john@kamauagro.co.ke
Phone:            +254 722 123 456
Country:          Kenya

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT HAPPENS NEXT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Our freight team will review your request within 24 hours.
2. You will receive a detailed quotation at john@kamauagro.co.ke
3. Once you accept the quote, we will confirm your booking.

This receipt is NOT a booking confirmation.
Your booking is confirmed only when you accept our formal quotation.

To track your request at any time, visit:
[COMPANY WEBSITE URL]/tracking
And enter your Request ID: FRQ-20240315-4821

For urgent enquiries: [OPS EMAIL] | [PHONE]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Footer: Company name | Address | Website | Registration No.]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### PDF styling
- Company letterhead colors (navy header band)
- Monospaced Request ID in blue
- Clean table-style layout — not a wall of text
- Generated client-side using a PDF library (e.g. jsPDF or react-pdf — developer decision)

---

## REQUEST TRACKING PAGE

### URL: `/tracking`

### Purpose
Allow any user to check the status of their request using their Request ID. No login required.

### Page Layout
```
NAVBAR
↓
[Hero band — navy, modest height 240px]
  "Track Your Request"
  "Enter your Request ID to check the status of your quote request."

↓
[Lookup form — centered card, white, max 480px wide]
  ┌─────────────────────────────────────┐
  │  Request ID                         │
  │  [Input: FRQ-XXXXXXXX-XXXX    ] [→] │
  └─────────────────────────────────────┘

↓ [After valid ID submitted]

[Status card — white, shadow, max 640px centered]
  ┌─────────────────────────────────────────────────┐
  │  Request ID: FRQ-20240315-4821                  │
  │  Submitted: 15 March 2024                       │
  │                                                 │
  │  STATUS TIMELINE                                │
  │  ●──────────●──────────○──────────○             │
  │  Received   Under      Quote      Confirmed     │
  │             Review     Sent                     │
  │                                                 │
  │  Current: Under Review                          │
  │  "Our team is preparing your quotation."        │
  │                                                 │
  │  Service: Sea Freight                           │
  │  Route: Mombasa → Rotterdam                     │
  │  Contact email on file: j***@kamau***.co.ke     │
  │  (email partially masked for privacy)           │
  │                                                 │
  │  [⬇ Re-download Receipt]  [Contact Us]          │
  └─────────────────────────────────────────────────┘
```

### Status States (4 stages)

| Status Key | Display Label | Description shown to user |
|---|---|---|
| `PENDING` | Received | "Your request has been received. We'll begin reviewing shortly." |
| `IN_REVIEW` | Under Review | "Our team is preparing your quotation." |
| `QUOTED` | Quote Sent | "We've sent a quote to your email. Please check your inbox." |
| `CONFIRMED` | Confirmed | "Your booking has been confirmed. Our team will be in touch." |
| `CLOSED` | Closed | "This request has been closed. Contact us if you need assistance." |

### Not Found State
```
[Icon: search with X]
"We couldn't find that Request ID."
"Double-check the ID on your receipt, or contact us directly."
[Button: "Contact Us"]
```

---

## EMAIL COMMUNICATION (for backend developer)

### Email 1: Sent to CLIENT on form submission

**To:** User's submitted email
**From:** `noreply@[company-domain].com`
**Subject:** `Your Quote Request — FRQ-20240315-4821`

**Body:**
- Company logo header
- "Hi [Name], we've received your freight quote request."
- Request summary (service, route, cargo)
- **Request ID prominently displayed**
- "Our team will review and respond within 24 hours."
- Tracking link: `[Website]/tracking?id=FRQ-20240315-4821`
- Contact details for urgent queries

### Email 2: Sent to OPS TEAM on form submission

**To:** `ops@[company-domain].com` (or configured recipient)
**From:** `noreply@[company-domain].com`
**Subject:** `New Quote Request — FRQ-20240315-4821 — Sea Freight — Mombasa→Rotterdam`

**Body:**
- Full form submission dump in table format
- Direct link to update status in admin panel (if built)
- Reply-to set to client's email address

---

## FAILURE STATES

### Validation Error (client-side)
- Fields highlighted in red, inline error messages
- Submit button stays disabled
- No toast — errors live on the form

### Backend Failure (5xx)
```
[Error banner inside modal, amber/red]
"Something went wrong on our end. Your request was not submitted."
[Retry button] [Contact us directly →]
```

### Network Failure
```
"Check your connection and try again."
[Retry button]
```

### Duplicate Submission Protection
- Submit button disabled immediately on first click
- If same email + same route submitted within 30 minutes: backend should return a specific error
- UI shows: "It looks like you may have already submitted a similar request. Check your email for your Request ID."

---

---

# PART F — ABOUT US PAGE

## Page Structure

```
NAVBAR
↓
ABOUT HERO
↓
COMPANY STORY
↓
MISSION & VALUES
↓
THE TEAM
↓
BY THE NUMBERS (Stats)
↓
WHAT WE REPRESENT (Values deep-dive)
↓
CERTIFICATIONS & MEMBERSHIPS
↓
LOCATIONS
↓
FOOTER
```

---

## SECTION: ABOUT HERO

**H1:** Moving the World's Cargo Since [Year]
**Subheadline:** A freight and logistics company built on reliability, expertise, and a genuine commitment to our clients' supply chains.
**Photo:** Team photo at port or company facility — real people, professional but human.
- Dark overlay same as service heroes

---

## SECTION: COMPANY STORY

### Layout
- 2-column: left text (6-col), right image (6-col)
- Image: founder or early operations photo, corner radius 12px

### Content
**Eyebrow:** OUR STORY
**H2:** Built from the ground up in [Country/Region]

3–4 paragraphs telling the founding story. Must answer:
- Who founded it and when
- What problem they were solving
- How the company has grown
- Where the company operates today

**Designer note:** This section must feel warm and human — NOT a Wikipedia-style corporate bio. Use 17px body text with generous line height. No bullet points. Pure narrative paragraphs.

---

## SECTION: MISSION & VALUES

### Layout
- White background, centered, max 800px wide
- Mission statement in large pull-quote style (24px, navy, italic)
- Values below as 3-column cards (reuse Value Card component)

### Content
**Eyebrow:** WHAT DRIVES US
**Mission:** *"[Company mission — one clear sentence. E.g., 'To make global trade accessible, transparent, and reliable for every client, regardless of size.']*"

**Values (3 cards):**
- Excellence (existing card — reuse)
- Reliability (existing card — reuse)
- Customer Focus (existing card — reuse)

---

## SECTION: THE TEAM

### Layout
- Surface background `#F8F9FB`
- Grid: 4 columns (desktop), 2 col (tablet), 1 col (mobile)
- Each team member card:

```
┌───────────────────────┐
│  [Photo — square crop,│
│   border-radius 12px, │
│   aspect 1:1]         │
│                       │
│  [Name — SemiBold]    │
│  [Title — Regular,    │
│   muted, 14px]        │
│  [LinkedIn icon link] │
└───────────────────────┘
```

**Designer note:** Photos must be consistent — same background style, same crop. No mixing of styles.

---

## SECTION: BY THE NUMBERS

### Layout
- Navy dark bg (`#00315B`)
- 4 stats in a row (desktop), 2×2 grid (mobile)

| Stat | Description |
|---|---|
| 70+ | Years of Combined Experience |
| 90+ | Global Partner Ports |
| 500+ | Active Clients |
| 98% | On-Time Performance |

**Designer note:** Stats must use Inter Black 48px, white. Descriptions in Inter Light 14px, white 70% opacity. No unnecessary decoration.

---

## SECTION: WHAT WE REPRESENT

### Layout (as seen in Figma designs)
- Split sections alternating: text left / image right, then image left / text right
- Each split: 50/50, full bleed images

### Sub-sections (suggested 3):
1. **Our Commitment to Clients** — dedicated teams, custom solutions
2. **Our Operational Standards** — compliance, safety, certifications
3. **Our Global Network** — port coverage, partnerships, reach

---

## SECTION: CERTIFICATIONS & MEMBERSHIPS

### Layout
- White bg, centered
- Logo grid: certification logos at grayscale, 100px height each, spaced generously
- Examples: ISO certification, FIATA, IATA, local customs authority registration

---

## SECTION: LOCATIONS

### Layout
- Surface bg
- If multiple offices: card per location with address, phone, email, map pin icon
- If single location: single centered card with embedded map (or map placeholder image)

---

---

# PART G — ADDITIONAL PAGES SUGGESTED

## Pages to Build (Prioritized)

| Priority | Page | Purpose |
|---|---|---|
| 1 | Service pages (×6) | Convert visitors per service |
| 1 | Quote form + tracking | Primary conversion |
| 1 | About Us | Trust and credibility |
| 2 | Contact Page | Direct enquiries |
| 2 | Projects & Updates | Blog / news / SEO |
| 3 | FAQ | Reduce pre-sale friction |
| 3 | Careers | Talent acquisition |
| 4 | Client Portal | Advanced — login-gated tracking |

---

## Contact Page

### Sections
- Header band: "Get In Touch"
- Two columns: left — contact form (Name, Email, Subject, Message), right — contact details (office address, phone, email, hours, map)
- Form submission: same backend infrastructure as quote form but simpler

---

## FAQ Page

### Sections
- Hero band: "Frequently Asked Questions"
- Category filter tabs: All | Sea Freight | Transportation | Customs | Payments | General
- Accordion list of Q&A items per category
- Bottom CTA: "Didn't find your answer? Contact us"

### Suggested FAQ categories per service:
- What are your payment terms?
- How long does sea freight take to [region]?
- Do you handle customs clearance?
- Can I track my shipment?
- What cargo do you NOT handle?
- What is the minimum shipment size for LCL?

---

---

# PART H — MOTION & INTERACTIONS

| Element | Trigger | Effect | Duration | Easing |
|---|---|---|---|---|
| Navbar scroll | Page scrolled >60px | bg fades from transparent to white | 200ms | ease-out |
| Section content | Enters viewport | Fade up (translateY 24px → 0, opacity 0→1) | 400ms | ease-out |
| Value cards | Enters viewport | Staggered fade up, 80ms between each | 400ms | ease-out |
| Cards hover | Mouse enter | Box shadow deepens, translateY(-2px) | 150ms | ease-out |
| CTA hover | Mouse enter | translateY(-1px), slight color deepen | 120ms | ease-out |
| Form modal | CTA click | Overlay fades in, modal scales from 95%→100% | 200ms | ease-out |
| Form modal close | × or backdrop | Reverse of open | 150ms | ease-in |
| Success state | Submit success | Form fades out, ✓ icon bounces in | 300ms | spring |
| Step transition | "Next" click | Slide left: Step 1 exits left, Step 2 enters right | 250ms | ease-in-out |
| Status timeline | Page load | Dots fill left to right, 200ms stagger | 600ms | ease-out |
| Service chips | Select | Fill with blue bg, white text | 120ms | ease |
| Navbar mega-menu | Hover | Fade down with slight translateY | 180ms | ease-out |

**Reduced motion:** All animations disabled when `prefers-reduced-motion: reduce`. States change instantly.

---

---

# PART I — RESPONSIVE BEHAVIOR

| Section | Desktop (≥1024) | Tablet (640–1023) | Mobile (≤639) |
|---|---|---|---|
| Navbar | Full horizontal with links | Logo + hamburger | Logo + hamburger |
| Service hero | 2-col (text left, image full bleed bg) | Text centered, image bg | Text centered, image bg, shorter height |
| What We Offer | Left text 5-col / right grid 7-col | Stacked: heading then grid | Stacked, single column |
| Feature grid | 2 col × 3 rows | 2 col × 3 rows | 1 col |
| How It Works steps | Horizontal row, 5 steps | 2-col wrap | Vertical accordion |
| Value cards | 3 columns | 2 + 1 below | 1 column, full width |
| Customers logos | 3 × 2 grid | 3 × 2 grid | Horizontal scroll marquee |
| Why Choose Us | 50/50 split | Stacked: image top, text below | Stacked |
| Stats row | 4 in a row | 2 × 2 | 2 × 2 |
| Quote form modal | 620px centered modal | 90vw modal | Full screen drawer from bottom |
| Form fields | Standard layout | Standard layout | Full width stacked |
| Receipt | PDF only — not affected | PDF only | PDF only |
| Tracking lookup | Centered card 480px | 90% width | Full width |
| About team grid | 4 columns | 2 columns | 1 column |
| Footer | 4 columns | 2 columns | 1 column, stacked |

---

# PART J — COPY STANDARDS

## Tone of Voice
- **Authority without arrogance** — Maersk-style: direct, confident, not boastful
- **Specific over vague** — "99.2% on-time" not "highly reliable"
- **Human not corporate** — "We'll review your request" not "Your submission will be processed"
- **Clear for non-freight people** — Avoid unexplained jargon (define LCL, FCL on first use)

## Content Labels
All copy in this document is: **PLACEHOLDER COPY** — must be replaced with actual company copy before launch.

Specifically needs real content:
- Company name (appears everywhere as [Company Name])
- Founding year
- Company story / narrative
- Real statistics (years, client count, on-time rate)
- Team member names, photos, titles
- Real client logos
- Real certification logos
- Office address, phone, email
- Operational email (ops@...)
- Website domain

---

# PART K — OPEN QUESTIONS FOR CLIENT

| # | Question | Affects |
|---|---|---|
| 1 | What is the company name and domain? | Navbar, footer, emails, receipt PDF |
| 2 | What year was the company founded? | About page hero H1 |
| 3 | Are there real customer logos to use? | All "Major Customers" sections |
| 4 | Do we add Air Freight and Customs Clearance, or are these not services offered? | Site structure, nav |
| 5 | What certifications/memberships does the company hold? | About page certifications section |
| 6 | What email should quote requests be sent to? | Backend — ops notification email |
| 7 | Where is the office / are there multiple locations? | Contact page, footer |
| 8 | Are there real team member photos and bios? | About page team section |
| 9 | Is there an existing logo file (SVG)? | Navbar, footer, PDF receipt |
| 10 | Should the tracking page be public (no login) or gated? | Tracking page architecture |
| 11 | Should the form be a modal, drawer, or separate page? | Quote form UX |
| 12 | Are real project/news articles available for the blog? | Projects & Updates section |

---

# PART L — AI ASSUMPTIONS LOG

| Assumption | Evidence | Confidence |
|---|---|---|
| 6 services offered (incl. Air + Customs) | 4 visible in designs; 2 added as common-in-sector | STRONG INFERENCE for 4 / UNCERTAIN for 2 added |
| Maersk is the visual reference | User stated explicitly | EXPLICIT |
| Orange is the primary CTA color | Visible in designs | EXPLICIT |
| Inter is primary typeface | Font list in imports | EXPLICIT |
| Instrument Sans used for buttons/eyebrows | Font list suggests display/UI role | STRONG INFERENCE |
| Request ID format FRQ-YYYYMMDD-XXXX | Invented — not specified by user | UNCERTAIN — confirm with developer |
| 24-hour quote response time | Common industry standard | UNCERTAIN — confirm with ops |
| Form is a modal, not a page | Best practice for conversion, Maersk pattern | STRONG INFERENCE |
| PDF generated client-side | No backend PDF system mentioned | UNCERTAIN — developer to confirm |
| Email partially masked on tracking page | Privacy best practice | STRONG INFERENCE |
| 4 status stages: PENDING/IN_REVIEW/QUOTED/CONFIRMED | Logical workflow inference | STRONG INFERENCE |
| Stats: 70+, 1500+, 98% | Visible in designs | EXPLICIT |

---

*Document version: 1.0 — August 2026*
*Designer: Continue from this document. Flag anything marked UNKNOWN or UNCERTAIN before building.*
