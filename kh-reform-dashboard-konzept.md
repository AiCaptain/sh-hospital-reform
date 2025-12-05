# Krankenhausreform Schleswig-Holstein: Dashboard-Konzept

## 1. Executive Summary

Dieses Konzeptdokument beschreibt die Anforderungen und das Design für ein interaktives Dashboard zur Umsetzung und Monitoring der Krankenhausreform in Schleswig-Holstein. Das Dashboard soll Mitarbeitern des Ministeriums und der Regionalkonferenzen ermöglichen, den Reformfortschritt zu überwachen, Entscheidungen datenbasiert zu treffen und die Versorgungsqualität für Bürger zu sichern.

**Zielgruppen:**
- Mitarbeiter des Ministeriums für Justiz und Gesundheit (strategische Steuerung)
- Teilnehmer der Regionalkonferenzen (operative Planung)
- Krankenhausplaner und Qualitätsmanager

---

## 2. Ziele des Dashboards

### 2.1 Übergeordnete Ziele

1. **Transparenz**: Schaffung eines einzigen "Source of Truth" für Reformfortschritt und Versorgungsstatus
2. **Datengestützte Entscheidungen**: Befähigung der Entscheidungsträger mit aktuellen, verlässlichen Informationen
3. **Frühwarnung**: Schnelle Identifikation von Problemen und Abweichungen vom Plan
4. **Koordination**: Unterstützung der Kommunikation zwischen Ministerium und Regionalkonferenzen
5. **Rechenschaftspflicht**: Dokumentation des Reformfortschritts für Stakeholder und Öffentlichkeit

### 2.2 Spezifische Ziele

- Verfolgung der Leistungsgruppen-Zuweisung bis zum 01.01.2027
- Monitoring der Qualitätskriterien-Erfüllung an allen Standorten
- Identifikation von Versorgungslücken in Regionen
- Überwachung der Transformationsfonds-Nutzung
- Sicherung der flächendeckenden Grund- und Notfallversorgung

---

## 3. Erfolgsmetriken (KPIs)

### 3.1 Strukturelle KPIs

| KPI | Zielwert | Frequenz | Verantwortung |
|-----|----------|----------|---------------|
| Leistungsgruppen genehmigt (%) | 100% bis 01.01.2027 | monatlich | Ministerium |
| Qualitätskriterien erfüllt (%) | 95%+ | monatlich | Krankenhäuser |
| Versorgungslücken identifiziert | alle bekannt | quartalsweise | Regionalkonferenzen |
| Transformationsfonds allokiert (%) | 100% | quartalsweise | Ministerium |

### 3.2 Qualitäts-KPIs

| KPI | Zielwert | Frequenz | Quelle |
|-----|----------|----------|--------|
| Komplikationsrate (je LG) | < Baseline | halbjährlich | Routinedaten |
| Patientenzufriedenheit | ≥ 3.5/5.0 | halbjährlich | PREMs |
| Wiedereinlieferungsrate | < Baseline | halbjährlich | Routinedaten |
| Bettenauslastung (stationär) | 75-85% | monatlich | Routinedaten |

### 3.3 Versorgungssicherungs-KPIs

| KPI | Zielwert | Frequenz | Messung |
|-----|----------|----------|---------|
| Notfallversorgung erreichbar (%) | 100% in <30 min | quartalsweise | Fahzeitanalyse |
| Spezialisierte Leistungen erreichbar (%) | 95%+ in <60 min | quartalsweise | Fahzeitanalyse |
| Patientenwanderungen (in/out SH) | ausgeglichen | halbjährlich | Routinedaten |

---

## 4. Datenbedarf und Quellen

### 4.1 Primärdatenquellen

| Datenbereich | Quelle | Frequenz | Format |
|--------------|--------|----------|--------|
| Leistungsgruppen-Anträge & Genehmigungen | Ministerium (manuelle Erfassung) | monatlich | CSV/API |
| Krankenhausstammdaten | Landesverband der Krankenkassen | laufend | CSV/XML |
| Qualitätskriterien | Externe Audits / MDK | jährlich | Audit-Report |
| Routinedaten (Fälle, Verweildauer, etc.) | Abrechnungsdaten (§21 KHEntgG) | monatlich | CSV |
| Patientenzufriedenheit | PREMs-Umfragen | halbjährlich | JSON |
| Personalausstattung | Krankenhausmeldung | quartalsweise | CSV |

### 4.2 Sekundärdatenquellen

| Datenbereich | Quelle |
|--------------|--------|
| Geographische Daten | OpenStreetMap, BKG |
| Bevölkerungsprognosen | Statistikamt Nord |
| Rettungsdienst-Daten | Leitstellen (anonym aggregiert) |
| Kooperationsvereinbarungen | Ministerium, Verbände |

---

## 5. Dashboard-Struktur und -Komponenten

### 5.1 Hauptnavigation

Das Dashboard gliedert sich in **5 Hauptansichten**:

1. **Überblick**: Landesweite Reformmetriken auf einen Blick
2. **Regional**: Detailansicht für die 5 Regionalkonferenzen
3. **Standorte**: Einzelkrankenhaus-Profile mit Leistungsgruppen
4. **Qualität**: Klinische Qualitätsindikatoren und Trends
5. **Planung**: Zeitstrahl, Meilensteine, Termine

---

## 6. Dashboard-Ansichten (Detailed Design)

### 6.1 Ansicht "Überblick" (Landesebene)

**Zweck:** Schneller Überblick über Reformfortschritt und kritische Kennzahlen

**Komponenten:**

#### A. Reform-Fortschrittsanzeige (oben)

```
┌─────────────────────────────────────────────────────────────┐
│ KRANKENHAUSREFORM SCHLESWIG-HOLSTEIN                        │
│ Stand: 05.12.2025                                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ LEISTUNGSGRUPPEN-ZUWEISUNG                                  │
│ Genehmigt: 47/61 (77%) ████████░░ Ziel: 100% bis 01.01.27  │
│                                                             │
│ QUALITÄTSKRITERIEN-ERFÜLLUNG                                │
│ Erfüllt: 156/164 Standorte (95%) ██████████ Ziel: 95%+     │
│                                                             │
│ TRANSFORMATIONSFONDS                                        │
│ Allokiert: €48M / €60M (80%) ████████░░ Ziel: 100%         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### B. Regionale Übersicht (Karten-Widget)

- **Karte von Schleswig-Holstein** mit 5 Regionalkonferenz-Bereichen
- Farbcodierung nach Status:
  - 🟢 Grün: Alle KPIs im Plan
  - 🟡 Gelb: Warnungen / teils nicht im Plan
  - 🔴 Rot: Kritische Probleme
- Klick auf Region → Übergang zu Ansicht 6.2 "Regional"

#### C. Kritische Alerts (rechts)

```
⚠️  OFFENE PUNKTE

🔴 Region Lübeck: 
    - Kardiologie-LG noch nicht genehmigt (erwartet 31.12.25)
    
🟡 Region Kiel:
    - Pneumologie: 2 Standorte unter Mindestmenge
    
🔴 UKSH Campus Lübeck:
    - Personalausstattung Chirurgie nicht ausreichend
    - Audit erforderlich bis 15.01.26
```

#### D. KPI-Scoreboard (unten)

| Metrik | Aktuell | Ziel | Trend |
|--------|---------|------|-------|
| LG genehmigt (%) | 77% | 100% | ↗ +3pp |
| Qualität erfüllt (%) | 95% | 95% | → stabil |
| Fonds allokiert (%) | 80% | 100% | ↗ +5pp |
| Notfallversorgung erreichbar (%) | 98% | 100% | → stabil |
| Bettenauslastung (Ø) | 78% | 75-85% | ↗ +2pp |

---

### 6.2 Ansicht "Regional" (Pro Regionalkonferenz)

**Zweck:** Detaillierte Ansicht für eine einzelne Region mit Versorgungsanalyse

**Layout:** 3-spaltiges Grid

#### Linke Spalte: Krankenhäuser in der Region

```
📍 REGION LÜBECK (5 Standorte)

UKSH Campus Lübeck ⭐
├─ Status: Maximalversorgung
├─ Genehmigt: 12/15 LG (80%)
├─ Qualität: ✓ Erfüllt
└─ Warnung: Personalausstattung Chirurgie

Sana-Klinik Lübeck
├─ Status: Regelversorgung
├─ Genehmigt: 8/8 LG (100%)
├─ Qualität: ✓ Erfüllt
└─ Status: ✓ Alle KPIs im Plan

... [weitere Kliniken]
```

#### Mittlere Spalte: Versorgungsanalyse

- **Versorgungslücken-Matrix**: Welche Leistungsgruppen in welchen Teilregionen fehlen
- **Patientenwanderung**: Wohin wandern Patienten ab (Trend)
- **Erreichbarkeitskarte**: Fahzeitanalyse zu spezialisierten Zentren
- **Demografische Daten**: Bevölkerung, Alter, prognostizierter Bedarf

#### Rechte Spalte: Maßnahmen & Timeline

```
GEPLANTE LEISTUNGSGRUPPEN-ZUWEISUNG

🗓️  Dezember 2025
├─ 20.12: UKSH Lübeck - Kardiologie-Audit
├─ 22.12: Sana - Pneumologie-Audit
└─ Ziel: 15/15 LG genehmigt

🗓️  Januar 2026
├─ 10.01: Regionalkonferenz
├─ 15.01: Deadline Personalausstattung
└─ Ziel: 100% Qualitätskriterien erfüllt

OFFENE PROBLEME:
🔴 UKSH: Chirurgie-Personal fehlt (2 Stellen)
🟡 Sana: Pneumologie unter Mindestmenge
```

---

### 6.3 Ansicht "Standorte" (Krankenhausprofile)

**Zweck:** Detailansicht für einzelnes Krankenhaus mit Leistungsgruppen-Übersicht

**Layout:** 2-Spalten

#### Linke Spalte: Krankenhausstammdaten

```
UKSH Campus Lübeck

Allgemein:
├─ Träger: Universitätsklinikum Schleswig-Holstein
├─ Bundesland: Schleswig-Holstein
├─ Planungsbereich: Lübeck
├─ Versorgungsstufe: Maximalversorgung
├─ Planbetten: 650
└─ Mitarbeiter: 3.450

Kontakt:
├─ Geschäftsführer: [Name]
├─ Qualitätsmanager: [Name]
└─ Tel: [Nummer]

Kooperationen:
├─ ✓ mit Sana Lübeck (Notfall)
├─ ✓ mit Lübeck Hospital (Radiologie)
└─ ⊗ geplant: mit Eutin Hospital
```

#### Rechte Spalte: Leistungsgruppen & Qualität

```
LEISTUNGSGRUPPEN-STATUS: 12/15 (80%)

Genehmigt (12):
✓ Innere Medizin (Kardiologie)
✓ Innere Medizin (Pneumologie)
✓ Chirurgie (Allgemein)
✓ Unfallchirurgie
... [weitere 8]

In Bearbeitung (2):
🕐 Kardiologie - Spezialisierung
    Status: Audit geplant 20.12.2025
    Bewertung: ⟳ Ausstehend
    
🕐 Radiologie - Neuroradiologie
    Status: Audit abgeschlossen
    Bewertung: ⚠️  Mangel: Personal

Abgelehnt (1):
✗ Urologie - Roboterassistierte Chirurgie
    Grund: Mindestmenge nicht erreichbar
    Alternative: Kooperation mit Bremen angeboten

QUALITÄTSKRITERIEN

Personalausstattung: ⚠️  Chirurgie: 2 Ärzte fehlen (5 geplant)
Sachausstattung: ✓ Alle Anforderungen erfüllt
Verwandte LG: ✓ Alle vorhanden

Qualitätsindikatoren (letzte 6 Monate):
├─ Komplikationsrate: 2.3% (Target: <2.5%) ✓
├─ 30-Tage-Sterberate: 1.1% (Target: <1.5%) ✓
└─ Patientenzufriedenheit: 4.2/5.0 (Target: ≥3.5) ✓
```

---

### 6.4 Ansicht "Qualität" (Klinische Indikatoren)

**Zweck:** Monitoring von Qualitätsmetriken über Zeit und Vergleiche zwischen Standorten

**Layout:** Dashboard mit mehreren Widgets

#### Widget A: Qualitätsindikatoren pro Leistungsgruppe

- **Auswahl-Dropdown**: Leistungsgruppe wählen (z.B. "Innere Medizin - Kardiologie")
- **Kennzahlen-Cards**:
  ```
  INNERE MEDIZIN - KARDIOLOGIE (Region: gesamt)
  
  ┌─────────────────┬─────────────────┬─────────────────┐
  │ Komplikationen  │ 30-Tage Mortal.  │ Verweildauer    │
  │ 2.3%            │ 1.1%            │ Ø 5.2 Tage      │
  │ Target: <2.5%   │ Target: <1.5%   │ Target: 5±1 Tag │
  │ ✓ Im Plan       │ ✓ Im Plan       │ ✓ Im Plan       │
  └─────────────────┴─────────────────┴─────────────────┘
  ```

#### Widget B: Trend-Diagramme

- **Line Chart**: Zeigt Verlauf von Indikatoren über 12 Monate
- **Vergleichslinie**: Bundesweit / anderer Bundesländer / Baseline
- Beispiel:
  ```
  Komplikationsrate Kardiologie über Zeit
  
  3.0% │     ↘
  2.8% │    ╱ ╲
  2.6% │   ╱   ╲─────  ← Schleswig-Holstein
  2.4% │  ╱         ╲
  2.2% │ ╱           ╲____
       │ ─────────────────── ← Bundesweit Baseline
       └─────────────────────
        Jan  Feb  Mär  Apr  Mai  Jun
  ```

#### Widget C: Standort-Vergleich

- **Heatmap**: Qualitätsindikatoren aller Standorte für eine LG
- Farbcodierung:
  - 🟢 Grün: Über Ziel
  - 🟡 Gelb: Im Plan
  - 🔴 Rot: Unter Ziel / Intervention erforderlich

```
INNERE MEDIZIN - KARDIOLOGIE: Vergleich Standorte

             Komplik. | Mortal. | Zufried. | Verweildauer
UKSH Lübeck    🟢      🟡       🟢         🟢
UKSH Kiel      🟢      🟢       🟡         🟢
Sana Lübeck    🟡      🟢       🟢         🟢
... [weitere]
```

---

### 6.5 Ansicht "Planung" (Zeitstrahl & Meilensteine)

**Zweck:** Übersicht über Reformschritte, Termine und Meilensteine

**Layout:** Vertikaler Zeitstrahl mit Meilensteinen und Ereignissen

```
KRANKENHAUSREFORM SCHLESWIG-HOLSTEIN: ZEITSTRAHL

2025
│
├─ 01.12.2025 ✓ Abgeschlossen
│  └─ Frist: Leistungsgruppen-Anträge eingereicht
│     Status: 61/61 Anträge eingegangen
│
├─ 15.12.2025 🕐 In Bearbeitung (aktuell)
│  └─ Audits Qualitätskriterien
│     Status: 3/5 abgeschlossen
│
├─ 31.12.2025 ⏳ Kommend
│  └─ Frist: Qualitätskriterien-Erfüllung
│     Warnung: 4 Standorte im kritischen Bereich
│
├─ 10.01.2026 📅 Geplant
│  └─ Regionalkonferenzen (5 Regionen)
│     Agenda: Endgültige LG-Zuweisung
│
└─ 01.01.2027 🎯 Ziel
   └─ Alle Leistungsgruppen in Kraft
      Status: 77% der LG genehmigt

2026
│
├─ Q1 2026
│  └─ Evaluation 1. Reformphase
│     Metriken: Qualität, Erreichbarkeit, Kosten
│
├─ Q2-Q4 2026
│  └─ Refinement & Adjustments
│     Basis: Daten aus Q1 & Stakeholder-Feedback
│
└─ Q1 2027
   └─ Vollständige Umsetzung & Monitoring
      Nächste Schritte: Vorbereitung Bundesweit-Standardisierung
```

---

## 7. Darstellungs- und Interaktions-Prinzipien

### 7.1 Visuelle Hierarchie

1. **Top Priority**: KPIs mit Status-Ampeln (Rot/Gelb/Grün)
2. **Medium Priority**: Trend-Diagramme und Vergleiche
3. **Low Priority**: Detailinformationen (ausklappbar/scrollbar)

### 7.2 Farbcodierung

| Farbe | Bedeutung | Beispiele |
|-------|-----------|----------|
| 🟢 Grün | Im Plan / Erfolgreich | KPI erfüllt, Audit bestanden |
| 🟡 Gelb | Warnung / Abweichung | KPI zu 80% erfüllt, Audit mit Auflagen |
| 🔴 Rot | Kritisch / Nicht im Plan | KPI verfehlt, Audit nicht bestanden, Handlung erforderlich |
| ⚪ Grau | Nicht relevant / Daten ausstehend | Noch nicht geplant, noch kein Audit |

### 7.3 Interaktionsparadigmen

- **Klickbar**: Karten-Regionen, Krankenhäuser-Listen → Drill-Down
- **Hover**: Tooltips mit Zusatzinformationen
- **Filter**: Nach Region, Leistungsgruppe, Status
- **Export**: Tabellen und Diagramme als PDF/CSV
- **Responsive**: Desktop, Tablet, Mobile

### 7.4 Typische Nutzer-Journeys

**Journey 1: Ministerium - Tägliches Monitoring**
1. Öffnet Dashboard → Überblick-Ansicht
2. Sieht Ampel mit Status-Übersicht
3. Klickt auf rote Warnung (z.B. Region Lübeck)
4. Navigiert zu Regional-Ansicht → sieht Details
5. Exportiert Report für Ministerrats-Sitzung

**Journey 2: Regionalkonferenz - Vorbereitung**
1. Öffnet Dashboard 1 Woche vor Konferenz
2. Navigiert zu Regional-Ansicht (eigene Region)
3. Prüft Krankenhäuser-Status und offene Probleme
4. Bereitet Agenda für Konferenz vor
5. Teilt Report mit Konferenz-Teilnehmern

**Journey 3: Krankenhausmanagement - Selbstevaluierung**
1. Öffnet Dashboard
2. Navigiert zu Standort-Ansicht (eigene Klinik)
3. Prüft Leistungsgruppen-Status
4. Überprüft Qualitätsindikatoren
5. Plant nächste Schritte basierend auf Audits und Anforderungen

---

## 8. Technische Anforderungen

### 8.1 Performance & Verfügbarkeit

- **Ladezeit**: < 3 Sekunden für alle Ansichten
- **Verfügbarkeit**: 99.5% uptime
- **Datenfriskie**: 
  - Strukturdaten (LG-Status): täglich
  - Qualitätsdaten: monatlich
  - Routinedaten: wöchentlich
  - Real-time KPIs: täglich 17:00 Uhr

### 8.2 Sicherheit & Datenschutz

- **Authentifizierung**: LDAP / AD-Integration
- **Rollen-basierter Zugriff**:
  - Admin (Ministerium): Zugriff auf alle Daten
  - Regionalkonferenz-Lead: Zugriff auf eigene Region
  - Krankenhausmanagement: Zugriff auf eigenen Standort
- **Datenschutz**: Aggregation auf Kliniken-Ebene (keine Patientendaten)
- **Audit-Trail**: Alle Änderungen werden protokolliert

### 8.3 Technologie-Stack (Empfehlung)

- **Frontend**: React + TypeScript mit shadcn/ui oder Material-UI
- **Maps**: Mapbox oder OpenStreetMap (Leaflet)
- **Datenvisualisierung**: Recharts, Plotly oder Apache Echarts
- **Backend**: Python FastAPI / Node.js Express
- **Datenbank**: PostgreSQL mit TimescaleDB für Zeitreihen
- **Hosting**: Hetzner Cloud oder OVH (gemäß EU-Anforderungen)
- **Containerisierung**: Docker + Kubernetes

### 8.4 Daten-Pipeline

```
CSV/API-Quellen
     ↓
ETL-Prozess (Python/Airflow)
     ↓
PostgreSQL Data Warehouse
     ↓
React Dashboard (Frontend)
```

---

## 9. Implementierungs-Roadmap

### Phase 1: MVP (Januar - Februar 2026)
- ✓ Überblick-Ansicht (Landesebene)
- ✓ Regional-Ansicht (proto-Typ)
- ✓ Standort-Ansicht (basis)
- ✓ Basis-KPI-Tracking

### Phase 2: Ausbau (März - April 2026)
- ✓ Qualitäts-Ansicht (vollständig)
- ✓ Zeitstrahl / Planung
- ✓ Export-Funktionen
- ✓ Mobile-Optimierung

### Phase 3: Optimierung (Mai - Juni 2026)
- ✓ Real-time-Updates
- ✓ Predictive Analytics
- ✓ Automatisierte Alerting
- ✓ Stakeholder-Feedback Integration

---

## 10. Erfolgsmetriken für das Dashboard selbst

| Metrik | Ziel | Messung |
|--------|------|---------|
| Nutzung | 80%+ der Stakeholder nutzen Dashboard wöchentlich | Analytics |
| Entscheidungsqualität | 90%+ Entscheidungen basieren auf Dashboard-Daten | Umfrage |
| Fehlerreduktion | 50% weniger Dateninkonsistenzen | Error Logs |
| Zeitersparnis | 5h/Woche Dokumentation gespart pro Nutzer | Umfrage |
| Zufriedenheit | 4.0+/5.0 Nutzerzufriedenheit | NPS |

---

## 11. Glossar

| Begriff | Erklärung |
|---------|-----------|
| **Leistungsgruppe (LG)** | Definierte Gruppe von Diagnosen/Prozeduren, die ein KH erbringen darf |
| **Qualitätskriterien** | Personalausstattung, Sachausstattung, verwandte LG-Anforderungen |
| **Mindestvorhaltezahl** | Minimale Anzahl Patienten/Eingriffe pro Jahr je LG |
| **Transformationsfonds** | Bundesförderung für Krankenhausreformen |
| **Regionalkonferenz** | Koordinierungsgremium je Planungsregion |
| **PREM** | Patient Reported Experience Measure (Patientenerleben) |
| **PROM** | Patient Reported Outcome Measure (Patientenergebnis) |
| **Case-Mix-Index** | Gewichtung der Krankheitsschwere |
| **Versorgungsstufe** | Level des KH (begrenzte Regelversorgung bis Maximalversorgung) |

---

## 12. Anhang: Mockup-Beschreibungen für Entwicklung

### A. Überblick-Ansicht (Mockup-Details)

```
HEADER
┌─────────────────────────────────────────────────────────────────┐
│ Logo  | Krankenhausreform SH Dashboard | [Nutzer] [Sprache] [?] │
└─────────────────────────────────────────────────────────────────┘

HAUPTBEREICH (3 Spalten)

┌───────────────────┬───────────────────┬───────────────────┐
│   LINKE SPALTE    │   MITTLERE SPALTE │   RECHTE SPALTE   │
│                   │                   │                   │
│  KPI-SCOREBOARD   │   KARTE + REGIONEN│   ALERTS / OFFENE │
│  (Cards)          │   (Interaktiv)    │   PUNKTE          │
│                   │                   │                   │
│  Alle Metriken    │   5 Regionen,     │   Priority 1, 2, 3│
│  mit Status-      │   farbcodiert     │   mit Zeitleisten │
│  Ampeln           │                   │                   │
│                   │                   │                   │
└───────────────────┴───────────────────┴───────────────────┘

FOOTER
├─ Letzte Aktualisierung: 05.12.2025 17:00 Uhr
├─ Nächste Auto-Refresh: 06.12.2025 17:00 Uhr
└─ Datenquellen: Ministerium, LVK, MDK, Routinedaten
```

### B. Regional-Ansicht (Mockup-Details)

```
HEADER: Region: [Dropdown: Lübeck] | [← Zurück] [Print] [Export]

┌──────────────────────────────────────────────────────────────────┐
│ 🗺️  REGION LÜBECK - ÜBERSICHT                                    │
│                                                                  │
│ Bevölkerung: 180.000 | Forecast 2030: -5% | Durchschnittsalter: │
└──────────────────────────────────────────────────────────────────┘

INHALT (3-Spalten-Layout)

┌────────────────┬──────────────────┬──────────────────┐
│  KRANKENHÄUSER │  VERSORGUNGSANALYSE │  MAßNAHMEN     │
├────────────────┼──────────────────┼──────────────────┤
│                │                  │                  │
│ ☑ UKSH Lübeck │ Lücken-Matrix:  │ 🗓️  TIMELINE:    │
│   12/15 LG ✓   │ ┌─────────────┐ │                  │
│   Qualität: ✓  │ │ Unfallchi   │ │ ✓ Dec 20        │
│   ⚠️  Personal │ │ Neuro      │ │   - Audits      │
│                │ │ Gefäßchi   │ │                  │
│ ☑ Sana Lübeck │ │ ...        │ │ ⏳ Dec 31       │
│   8/8 LG ✓     │ └─────────────┘ │   - Frist       │
│   Qualität: ✓  │                  │                  │
│                │ Patientenstrom:  │ 🔴 OFFENE PUNKTE:│
│ ☑ Eutin Hosp. │ → Bremen: +12%   │ - Personal UKSH │
│   4/4 LG ✓     │ ← Kiel: -5%     │ - LG Neuro offen│
│   Qualität: ✓  │                  │                  │
│                │ Erreichbarkeit:  │                  │
│                │ Kardiologie:     │                  │
│                │ 98% <60min ✓     │                  │
│                │                  │                  │
└────────────────┴──────────────────┴──────────────────┘
```

---

**Ende des Konzeptdokuments**