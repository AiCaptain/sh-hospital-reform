# Krankenhausreform Schleswig-Holstein Dashboard

Ein interaktives Dashboard zur Überwachung und Steuerung der Krankenhausreform in Schleswig-Holstein.

## 🚀 Quick Start

### Installation

1. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

### Dashboard starten

```bash
streamlit run app.py
```

Das Dashboard öffnet sich automatisch im Browser unter `http://localhost:8501`

## 📊 Dashboard-Ansichten

Das Dashboard bietet 5 Hauptansichten:

### 1. 📊 Überblick (Landesebene)
- Reform-Fortschrittsanzeige mit Leistungsgruppen-Zuweisung
- Qualitätskriterien-Erfüllung
- Transformationsfonds-Allokation
- Regionale Übersicht mit Karten-Visualisierung
- Kritische Alerts und offene Punkte
- KPI-Scoreboard

### 2. 🗺️ Regional
- Detailansicht für jede der 5 Regionalkonferenzen:
  - Flensburg
  - Kiel
  - Lübeck
  - Neumünster
  - Rendsburg
- Krankenhäuser pro Region
- Versorgungsanalyse (Demographie, Erreichbarkeit, Lücken)
- Patientenströme (Zu-/Abwanderung)
- Anstehende Termine

### 3. 🏥 Standorte
- Einzelne Krankenhausprofile
- Stammdaten (Versorgungsstufe, Betten, Mitarbeiter)
- Leistungsgruppen-Status (genehmigt/in Bearbeitung/abgelehnt)
- Qualitätskriterien-Erfüllung
- Qualitätsindikatoren (Komplikationen, Mortalität, Zufriedenheit)

### 4. 📈 Qualität
- Klinische Qualitätsindikatoren pro Leistungsgruppe
- Trend-Entwicklung über 12 Monate
- Vergleich mit bundesweiten Baseline-Werten
- Standort-Vergleich (Heatmap-Visualisierung)

### 5. 🗓️ Planung
- Zeitstrahl mit Meilensteinen
- Status: Abgeschlossen / In Bearbeitung / Kommend / Geplant
- Quartalsweise Gruppierung
- Fristüberwachung bis zum Ziel 01.01.2027

## 🎨 Features

- **Interaktive Navigation** über Seitenleiste
- **Farbcodierung** nach Status:
  - 🟢 Grün: Im Plan / Erfolgreich
  - 🟡 Gelb: Warnung / Abweichung
  - 🔴 Rot: Kritisch / Handlung erforderlich
  - ⚪ Grau: Nicht relevant / Daten ausstehend
- **Responsive Design** mit Multi-Column-Layout
- **Plotly-Diagramme** für interaktive Visualisierungen
- **Progress Bars** für Fortschrittsanzeige
- **Alert-System** für kritische Punkte

## 📁 Projektstruktur

```
sh-hospital-reform/
├── app.py                          # Haupt-Streamlit-Anwendung
├── mock_data.py                    # Mock-Daten-Generator
├── requirements.txt                # Python-Abhängigkeiten
├── .streamlit/
│   └── config.toml                # Streamlit-Konfiguration
├── CLAUDE.md                       # Guidance für Claude Code
├── kh-reform-dashboard-konzept.md # Dashboard-Konzept
└── kh-reform-fachlicher-hintergrund.md # Fachlicher Hintergrund
```

## 🔧 Technologie-Stack

- **Frontend:** Streamlit 1.29.0
- **Visualisierung:** Plotly 5.18.0
- **Datenverarbeitung:** Pandas 2.1.4, NumPy 1.26.2
- **Sprache:** Python 3.8+

## 📝 Hinweis

Dieses Dashboard ist ein **Mockup-Prototyp** mit fiktiven Daten. Die reale Implementierung erfordert:

1. Anbindung an echte Datenquellen:
   - Ministerium (Leistungsgruppen-Anträge)
   - Landesverband der Krankenkassen (Stammdaten)
   - MDK (Qualitätsaudits)
   - Abrechnungsdaten (§21 KHEntgG)

2. Datenbank-Backend (PostgreSQL + TimescaleDB)

3. Authentifizierung & Autorisierung (LDAP/AD)

4. ETL-Pipeline für Datenintegration

Details zur vollständigen Implementierung finden sich in `kh-reform-dashboard-konzept.md`.

## 📚 Weitere Dokumentation

- `CLAUDE.md` - Guidance für zukünftige Entwicklung
- `kh-reform-dashboard-konzept.md` - Vollständiges Dashboard-Konzept
- `kh-reform-fachlicher-hintergrund.md` - Erfolgskriterien und Informationsbedarf

## 🎯 Ziel

**01.01.2027** - Alle 61 Leistungsgruppen den Krankenhäusern in Schleswig-Holstein zugewiesen.
