# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains planning and concept documentation for a **Hospital Reform Dashboard** for Schleswig-Holstein, Germany. The dashboard will monitor and track the implementation of the Krankenhausreform (hospital reform) that must be completed by January 1, 2027.

**Key Stakeholders:**
- Ministry of Justice and Health (strategic oversight)
- Regional conferences (operational planning)
- Hospital administrators and quality managers

**Primary Goals:**
- Track assignment of 61 service groups (Leistungsgruppen) to hospitals
- Monitor quality criteria fulfillment at all hospital locations
- Identify healthcare coverage gaps
- Track transformation fund usage
- Ensure comprehensive emergency and basic care coverage

## Repository Structure

Currently, this is a **documentation-only repository** containing:

- `kh-reform-dashboard-konzept.md` - Complete dashboard concept including:
  - 5 main dashboard views (Overview, Regional, Locations, Quality, Planning)
  - KPIs and success metrics
  - Data requirements and sources
  - Technical architecture recommendations
  - Implementation roadmap (3 phases)

- `kh-reform-fachlicher-hintergrund.md` - Background on reform success criteria and information requirements (bilingual DE/EN)

## Key Domain Concepts

**Leistungsgruppen (LG)**: Service groups - defined sets of diagnoses/procedures a hospital is permitted to perform. There are 61 defined service groups that must be assigned to all hospitals by 01.01.2027.

**Qualitätskriterien**: Quality criteria including staffing (Personalausstattung), equipment (Sachausstattung), and related service group requirements.

**Mindestvorhaltezahl**: Minimum volume requirements - minimum number of patients/procedures per year per service group.

**Transformationsfonds**: Federal transformation fund providing financial support for hospital restructuring.

**Regionalkonferenzen**: 5 regional conferences that coordinate planning in their respective areas:
- Region Flensburg
- Region Kiel
- Region Lübeck
- Region Neumünster
- Region Rendsburg

**Versorgungsstufen**: Care levels ranging from "begrenzte Regelversorgung" (limited standard care) to "Maximalversorgung" (maximum care).

## Technology Stack (Recommended)

When implementing the dashboard:

**Frontend:**
- React + TypeScript
- UI Components: shadcn/ui or Material-UI
- Maps: Mapbox or Leaflet (OpenStreetMap)
- Data Visualization: Recharts, Plotly, or Apache Echarts

**Backend:**
- Python FastAPI or Node.js Express
- Database: PostgreSQL with TimescaleDB for time-series data
- ETL Pipeline: Python/Airflow for data processing

**Infrastructure:**
- Docker + Kubernetes
- EU-compliant hosting (Hetzner Cloud or OVH)

## Data Sources

**Primary Sources:**
- Service group applications/approvals (Ministry, manual entry) - monthly
- Hospital master data (State health insurance association) - ongoing
- Quality criteria (External audits/MDK) - annual
- Routine data (billing data §21 KHEntgG) - monthly
- Patient satisfaction (PREMs surveys) - semi-annual
- Staffing data (hospital reporting) - quarterly

**Secondary Sources:**
- Geographic data (OpenStreetMap, BKG)
- Population forecasts (Statistikamt Nord)
- Emergency service data (anonymized aggregated)
- Cooperation agreements

## Key Performance Indicators (KPIs)

**Structural KPIs:**
- Service groups approved: Target 100% by 01.01.2027
- Quality criteria fulfilled: Target 95%+
- Coverage gaps identified: All known
- Transformation fund allocated: Target 100%

**Quality KPIs:**
- Complication rates per service group
- Patient satisfaction ≥ 3.5/5.0
- Readmission rates
- Bed occupancy 75-85%

**Coverage KPIs:**
- Emergency care accessible within 30 min: 100%
- Specialized services accessible within 60 min: 95%+
- Patient migration balanced

## Dashboard Views

1. **Overview (Landesebene)**: State-level reform progress with progress bars, regional map, critical alerts, KPI scoreboard

2. **Regional**: Detailed view per regional conference with hospital lists, coverage analysis, timelines

3. **Locations (Standorte)**: Individual hospital profiles with service group status, quality indicators, cooperation agreements

4. **Quality**: Clinical quality indicators with trend charts, location comparisons, heatmaps

5. **Planning**: Timeline view with milestones, deadlines, and reform steps

## Color Coding System

- 🟢 Green: On track / Successful
- 🟡 Yellow: Warning / Deviation
- 🔴 Red: Critical / Action required
- ⚪ Gray: Not relevant / Data pending

## Security & Access Control

**Role-based access:**
- Admin (Ministry): Full access to all data
- Regional conference lead: Access to own region
- Hospital management: Access to own location

**Privacy:** Aggregation at hospital level only (no patient-level data)

## Implementation Phases

**Phase 1: MVP (Jan-Feb 2026)**
- Overview view (state level)
- Regional view (prototype)
- Location view (basic)
- Basic KPI tracking

**Phase 2: Expansion (Mar-Apr 2026)**
- Quality view (complete)
- Timeline/Planning view
- Export functions
- Mobile optimization

**Phase 3: Optimization (May-Jun 2026)**
- Real-time updates
- Predictive analytics
- Automated alerting
- Stakeholder feedback integration

## Working with This Repository

When developing the dashboard:

1. **Refer to concept documents** for detailed requirements, mockups, and user journeys
2. **Follow the recommended tech stack** for EU compliance and data privacy requirements
3. **Implement data aggregation** at hospital level to protect patient privacy
4. **Use the color coding system** consistently across all views
5. **Design for accessibility** with target load time < 3 seconds
6. **Implement LDAP/AD integration** for authentication
7. **Create audit trails** for all changes

## German Healthcare Context

This project operates within Germany's federal healthcare system and specifically implements the Krankenhausreform mandated at the federal level. Key compliance requirements include:

- EU GDPR compliance for health data
- German hospital financing laws (KHEntgG)
- Federal quality criteria for service groups
- State-level hospital planning authority
