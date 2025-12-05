"""
Mock data generator for the Hospital Reform Dashboard
Generates fictional data for prototyping purposes
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Constants
REGIONS = ["Flensburg", "Kiel", "Lübeck", "Neumünster", "Rendsburg"]

HOSPITALS = {
    "Flensburg": [
        {"name": "Malteser Krankenhaus St. Franziskus-Hospital", "level": "Regelversorgung", "beds": 320},
        {"name": "Diakonissenkrankenhaus Flensburg", "level": "Regelversorgung", "beds": 280},
    ],
    "Kiel": [
        {"name": "UKSH Campus Kiel", "level": "Maximalversorgung", "beds": 850},
        {"name": "Städtisches Krankenhaus Kiel", "level": "Schwerpunktversorgung", "beds": 450},
        {"name": "Helios Klinik Kiel", "level": "Regelversorgung", "beds": 380},
    ],
    "Lübeck": [
        {"name": "UKSH Campus Lübeck", "level": "Maximalversorgung", "beds": 650},
        {"name": "Sana-Klinik Lübeck", "level": "Regelversorgung", "beds": 320},
        {"name": "Lübeck Hospital", "level": "Regelversorgung", "beds": 240},
    ],
    "Neumünster": [
        {"name": "FEK Friedrich-Ebert-Krankenhaus", "level": "Schwerpunktversorgung", "beds": 520},
        {"name": "Klinikum Neumünster", "level": "Regelversorgung", "beds": 390},
    ],
    "Rendsburg": [
        {"name": "Schön Klinik Rendsburg", "level": "Schwerpunktversorgung", "beds": 480},
        {"name": "Imland Klinik Rendsburg", "level": "Regelversorgung", "beds": 350},
    ]
}

LEISTUNGSGRUPPEN = [
    "Innere Medizin - Kardiologie",
    "Innere Medizin - Pneumologie",
    "Innere Medizin - Gastroenterologie",
    "Chirurgie - Allgemein",
    "Unfallchirurgie",
    "Neurochirurgie",
    "Gefäßchirurgie",
    "Orthopädie",
    "Urologie",
    "Gynäkologie",
    "HNO",
    "Augenheilkunde",
    "Radiologie",
    "Anästhesiologie",
    "Intensivmedizin",
]


def get_state_kpis():
    """Generate state-level KPIs for the overview dashboard"""
    return {
        "lg_approved": {"current": 47, "total": 61, "percentage": 77, "target": 100, "trend": "+3pp"},
        "quality_fulfilled": {"current": 156, "total": 164, "percentage": 95, "target": 95, "trend": "→ stabil"},
        "funds_allocated": {"current": 48, "total": 60, "percentage": 80, "target": 100, "trend": "+5pp"},
        "emergency_accessible": {"current": 98, "total": 100, "percentage": 98, "target": 100, "trend": "→ stabil"},
        "bed_occupancy": {"current": 78, "target_min": 75, "target_max": 85, "trend": "+2pp"},
    }


def get_regional_status():
    """Generate status for each region"""
    statuses = ["success", "warning", "critical"]
    weights = [0.5, 0.3, 0.2]  # 50% success, 30% warning, 20% critical

    regional_data = []
    for region in REGIONS:
        hospitals_count = len(HOSPITALS[region])
        status = random.choices(statuses, weights=weights)[0]

        regional_data.append({
            "region": region,
            "status": status,
            "hospitals": hospitals_count,
            "lg_approved_pct": random.randint(70, 100),
            "quality_fulfilled_pct": random.randint(85, 100),
            "population": random.randint(100000, 500000),
        })

    return pd.DataFrame(regional_data)


def get_critical_alerts():
    """Generate critical alerts for the dashboard"""
    alerts = [
        {
            "priority": "critical",
            "region": "Lübeck",
            "hospital": "UKSH Campus Lübeck",
            "issue": "Personalausstattung Chirurgie nicht ausreichend",
            "deadline": "15.01.2026",
            "type": "Personal"
        },
        {
            "priority": "critical",
            "region": "Lübeck",
            "hospital": None,
            "issue": "Kardiologie-LG noch nicht genehmigt",
            "deadline": "31.12.2025",
            "type": "LG-Genehmigung"
        },
        {
            "priority": "warning",
            "region": "Kiel",
            "hospital": None,
            "issue": "Pneumologie: 2 Standorte unter Mindestmenge",
            "deadline": "31.03.2026",
            "type": "Mindestmenge"
        },
    ]
    return alerts


def get_hospitals_for_region(region):
    """Get detailed hospital data for a specific region"""
    hospitals = HOSPITALS.get(region, [])
    detailed_hospitals = []

    for hosp in hospitals:
        total_lg = random.randint(8, 15)
        approved_lg = random.randint(int(total_lg * 0.6), total_lg)
        quality_ok = random.choice([True, True, True, False])  # 75% chance of OK

        status = "success"
        warnings = []

        if approved_lg < total_lg:
            status = "warning"
            warnings.append(f"{total_lg - approved_lg} LG noch nicht genehmigt")

        if not quality_ok:
            status = "critical" if status == "warning" else "warning"
            warnings.append("Personalausstattung nicht ausreichend")

        detailed_hospitals.append({
            "name": hosp["name"],
            "level": hosp["level"],
            "beds": hosp["beds"],
            "lg_total": total_lg,
            "lg_approved": approved_lg,
            "lg_percentage": int((approved_lg / total_lg) * 100),
            "quality_fulfilled": quality_ok,
            "status": status,
            "warnings": warnings,
            "staff": random.randint(200, 3500),
        })

    return detailed_hospitals


def get_hospital_details(hospital_name):
    """Get detailed information for a specific hospital"""
    # Find the hospital in the regions
    region = None
    hospital_base = None

    for reg, hosps in HOSPITALS.items():
        for hosp in hosps:
            if hosp["name"] == hospital_name:
                region = reg
                hospital_base = hosp
                break
        if hospital_base:
            break

    if not hospital_base:
        return None

    total_lg = random.randint(10, 15)
    approved_lg = random.randint(int(total_lg * 0.6), total_lg - 2)  # Leave room for in_progress
    in_progress_lg = random.randint(1, min(3, total_lg - approved_lg))
    rejected_lg = max(0, total_lg - approved_lg - in_progress_lg)

    # Generate approved Leistungsgruppen
    approved = random.sample(LEISTUNGSGRUPPEN, min(approved_lg, len(LEISTUNGSGRUPPEN)))

    remaining_lg = [lg for lg in LEISTUNGSGRUPPEN if lg not in approved]
    in_progress = random.sample(remaining_lg, min(in_progress_lg, len(remaining_lg)))

    remaining_lg = [lg for lg in remaining_lg if lg not in in_progress]
    rejected = random.sample(remaining_lg, min(rejected_lg, len(remaining_lg))) if rejected_lg > 0 else []

    return {
        "name": hospital_name,
        "region": region,
        "level": hospital_base["level"],
        "beds": hospital_base["beds"],
        "staff": random.randint(200, 3500),
        "lg_approved": approved,
        "lg_in_progress": [
            {"name": lg, "status": "Audit geplant", "date": "20.12.2025"} for lg in in_progress
        ],
        "lg_rejected": [
            {"name": lg, "reason": "Mindestmenge nicht erreichbar"} for lg in rejected
        ],
        "quality": {
            "staff_ok": random.choice([True, False]),
            "equipment_ok": True,
            "related_lg_ok": True,
        },
        "quality_indicators": {
            "complication_rate": round(random.uniform(1.5, 3.5), 1),
            "mortality_rate": round(random.uniform(0.8, 1.8), 1),
            "satisfaction": round(random.uniform(3.2, 4.5), 1),
        }
    }


def get_quality_data_for_lg(leistungsgruppe):
    """Get quality data for a specific Leistungsgruppe"""
    return {
        "complication_rate": {
            "current": round(random.uniform(1.8, 2.8), 1),
            "target": 2.5,
            "status": "success"
        },
        "mortality_rate": {
            "current": round(random.uniform(0.8, 1.4), 1),
            "target": 1.5,
            "status": "success"
        },
        "avg_stay": {
            "current": round(random.uniform(4.5, 6.0), 1),
            "target": 5.0,
            "range": 1,
            "status": "success"
        }
    }


def get_quality_trends(leistungsgruppe, months=12):
    """Generate trend data for quality indicators"""
    dates = [(datetime.now() - timedelta(days=30*i)).strftime("%b %Y") for i in range(months)]
    dates.reverse()

    # Generate trending data
    base_complication = 2.8
    trend = -0.05  # Improving trend

    data = {
        "month": dates,
        "complication_rate_sh": [max(1.5, base_complication + trend * i + random.uniform(-0.2, 0.2)) for i in range(months)],
        "complication_rate_bund": [2.4 + random.uniform(-0.1, 0.1) for _ in range(months)],
    }

    return pd.DataFrame(data)


def get_hospital_comparison(leistungsgruppe):
    """Get comparison data for hospitals for a specific LG"""
    all_hospitals = []
    for region, hosps in HOSPITALS.items():
        for hosp in hosps:
            all_hospitals.append(hosp["name"])

    comparison_data = []
    for hosp_name in all_hospitals[:8]:  # Limit to 8 for display
        comparison_data.append({
            "hospital": hosp_name,
            "complication": random.choice(["success", "success", "warning"]),
            "mortality": random.choice(["success", "success", "warning"]),
            "satisfaction": random.choice(["success", "success", "warning"]),
            "stay_duration": random.choice(["success", "success", "success"]),
        })

    return comparison_data


def get_timeline_events():
    """Get timeline events for the planning view"""
    events = [
        {
            "date": "01.12.2025",
            "status": "completed",
            "title": "Frist: Leistungsgruppen-Anträge eingereicht",
            "description": "Status: 61/61 Anträge eingegangen",
            "quarter": "Q4 2025"
        },
        {
            "date": "15.12.2025",
            "status": "in_progress",
            "title": "Audits Qualitätskriterien",
            "description": "Status: 3/5 abgeschlossen",
            "quarter": "Q4 2025"
        },
        {
            "date": "31.12.2025",
            "status": "upcoming",
            "title": "Frist: Qualitätskriterien-Erfüllung",
            "description": "Warnung: 4 Standorte im kritischen Bereich",
            "quarter": "Q4 2025"
        },
        {
            "date": "10.01.2026",
            "status": "planned",
            "title": "Regionalkonferenzen (5 Regionen)",
            "description": "Agenda: Endgültige LG-Zuweisung",
            "quarter": "Q1 2026"
        },
        {
            "date": "31.03.2026",
            "status": "planned",
            "title": "Evaluation 1. Reformphase",
            "description": "Metriken: Qualität, Erreichbarkeit, Kosten",
            "quarter": "Q1 2026"
        },
        {
            "date": "01.01.2027",
            "status": "goal",
            "title": "Alle Leistungsgruppen in Kraft",
            "description": "Status: 77% der LG genehmigt (aktuell)",
            "quarter": "Q1 2027"
        },
    ]
    return events


def get_regional_coverage_analysis(region):
    """Get coverage analysis for a region"""
    return {
        "coverage_gaps": [
            {"lg": "Neurochirurgie", "status": "missing"},
            {"lg": "Gefäßchirurgie", "status": "under_capacity"},
        ],
        "patient_migration": {
            "outbound": {"Bremen": 12, "Hamburg": 8, "Niedersachsen": 5},
            "inbound": {"Hamburg": 3, "Mecklenburg-Vorpommern": 2},
        },
        "accessibility": {
            "emergency_30min": 98,
            "specialized_60min": 95,
        },
        "demographics": {
            "population": random.randint(150000, 450000),
            "avg_age": random.randint(42, 48),
            "forecast_2030": random.randint(-8, 2),
        }
    }
