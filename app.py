"""
Krankenhausreform Schleswig-Holstein Dashboard
Interactive Dashboard for Hospital Reform Monitoring
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Import mock data
from mock_data import (
    get_state_kpis,
    get_regional_status,
    get_critical_alerts,
    get_hospitals_for_region,
    get_hospital_details,
    get_quality_data_for_lg,
    get_quality_trends,
    get_hospital_comparison,
    get_timeline_events,
    get_regional_coverage_analysis,
    REGIONS,
    LEISTUNGSGRUPPEN,
    HOSPITALS,
)

# Page configuration
st.set_page_config(
    page_title="Krankenhausreform SH Dashboard",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .status-success {
        color: #28a745;
        font-weight: bold;
    }
    .status-warning {
        color: #ffc107;
        font-weight: bold;
    }
    .status-critical {
        color: #dc3545;
        font-weight: bold;
    }
    .alert-box {
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .alert-critical {
        background-color: #f8d7da;
        border-left: 5px solid #dc3545;
    }
    .alert-warning {
        background-color: #fff3cd;
        border-left: 5px solid #ffc107;
    }
    .progress-bar-container {
        background-color: #e9ecef;
        border-radius: 5px;
        height: 30px;
        margin: 10px 0;
    }
    .progress-bar {
        background-color: #007bff;
        height: 100%;
        border-radius: 5px;
        text-align: center;
        color: white;
        line-height: 30px;
    }
</style>
""", unsafe_allow_html=True)


def render_header():
    """Render the dashboard header"""
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        st.image("https://via.placeholder.com/150x50?text=SH+Logo", width=150)
    with col2:
        st.title("🏥 Krankenhausreform Schleswig-Holstein Dashboard")
    with col3:
        st.write(f"**Stand:** {datetime.now().strftime('%d.%m.%Y')}")


def render_progress_bar(current, total, label=""):
    """Render a progress bar"""
    percentage = int((current / total) * 100)
    bar_html = f"""
    <div style="margin: 10px 0;">
        <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
            <span>{label}</span>
            <span><b>{current}/{total} ({percentage}%)</b></span>
        </div>
        <div style="background-color: #e9ecef; border-radius: 5px; height: 25px; overflow: hidden;">
            <div style="background-color: {'#28a745' if percentage >= 90 else '#ffc107' if percentage >= 70 else '#dc3545'};
                        width: {percentage}%; height: 100%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">
                {percentage}%
            </div>
        </div>
    </div>
    """
    st.markdown(bar_html, unsafe_allow_html=True)


def render_status_badge(status):
    """Render a status badge"""
    colors = {
        "success": "🟢",
        "warning": "🟡",
        "critical": "🔴",
        "pending": "⚪"
    }
    return colors.get(status, "⚪")


def view_overview():
    """Render the Overview (Landesebene) view"""
    st.header("📊 Überblick - Landesebene")

    # Get state KPIs
    kpis = get_state_kpis()

    # Top section: Reform Progress
    st.subheader("Reform-Fortschrittsanzeige")

    col1, col2 = st.columns([2, 1])

    with col1:
        # Progress bars
        render_progress_bar(
            kpis["lg_approved"]["current"],
            kpis["lg_approved"]["total"],
            "LEISTUNGSGRUPPEN-ZUWEISUNG"
        )
        st.caption(f"Ziel: {kpis['lg_approved']['target']}% bis 01.01.2027 | Trend: {kpis['lg_approved']['trend']}")

        render_progress_bar(
            kpis["quality_fulfilled"]["current"],
            kpis["quality_fulfilled"]["total"],
            "QUALITÄTSKRITERIEN-ERFÜLLUNG"
        )
        st.caption(f"Ziel: {kpis['quality_fulfilled']['target']}%+ | Trend: {kpis['quality_fulfilled']['trend']}")

        render_progress_bar(
            kpis["funds_allocated"]["current"],
            kpis["funds_allocated"]["total"],
            "TRANSFORMATIONSFONDS (in Mio. €)"
        )
        st.caption(f"Ziel: {kpis['funds_allocated']['target']}% | Trend: {kpis['funds_allocated']['trend']}")

    with col2:
        st.metric("Notfallversorgung erreichbar", f"{kpis['emergency_accessible']['percentage']}%",
                  kpis['emergency_accessible']['trend'])
        st.metric("Bettenauslastung (Ø)", f"{kpis['bed_occupancy']['current']}%",
                  kpis['bed_occupancy']['trend'])
        st.caption(f"Zielbereich: {kpis['bed_occupancy']['target_min']}-{kpis['bed_occupancy']['target_max']}%")

    st.divider()

    # Middle section: Regional Overview and Critical Alerts
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("🗺️ Regionale Übersicht")

        # Get regional status
        regional_df = get_regional_status()

        # Create a simple map visualization using plotly
        fig = go.Figure()

        # Simulated coordinates for regions (fictional positioning for visualization)
        region_coords = {
            "Flensburg": (54.8, 9.4),
            "Kiel": (54.3, 10.1),
            "Lübeck": (53.9, 10.7),
            "Neumünster": (54.1, 9.9),
            "Rendsburg": (54.3, 9.7),
        }

        for _, row in regional_df.iterrows():
            lat, lon = region_coords[row["region"]]
            color = {"success": "green", "warning": "yellow", "critical": "red"}[row["status"]]

            fig.add_trace(go.Scattergeo(
                lon=[lon],
                lat=[lat],
                text=f"{row['region']}<br>Status: {render_status_badge(row['status'])}<br>Krankenhäuser: {row['hospitals']}<br>LG genehmigt: {row['lg_approved_pct']}%",
                mode='markers+text',
                marker=dict(size=20, color=color),
                textposition="top center",
                name=row["region"]
            ))

        fig.update_geos(
            center=dict(lat=54.2, lon=10.0),
            projection_scale=15,
            showcountries=False,
            showcoastlines=True,
            showland=True,
            landcolor="lightgray"
        )

        fig.update_layout(
            height=400,
            margin={"r": 0, "t": 0, "l": 0, "b": 0},
            showlegend=False
        )

        st.plotly_chart(fig, use_container_width=True)

        # Regional status table
        st.write("**Status nach Regionen:**")
        for _, row in regional_df.iterrows():
            col_a, col_b, col_c, col_d = st.columns([2, 1, 1, 1])
            with col_a:
                st.write(f"{render_status_badge(row['status'])} **{row['region']}**")
            with col_b:
                st.write(f"{row['hospitals']} Standorte")
            with col_c:
                st.write(f"{row['lg_approved_pct']}% LG")
            with col_d:
                st.write(f"{row['quality_fulfilled_pct']}% Qualität")

    with col2:
        st.subheader("⚠️ Offene Punkte")

        alerts = get_critical_alerts()

        for alert in alerts:
            alert_class = "alert-critical" if alert["priority"] == "critical" else "alert-warning"
            priority_icon = "🔴" if alert["priority"] == "critical" else "🟡"

            alert_html = f"""
            <div class="alert-box {alert_class}">
                <div style="font-weight: bold;">{priority_icon} {alert['region']}</div>
                <div style="margin: 5px 0;">{alert['issue']}</div>
                {f"<div style='font-size: 0.9em; color: #666;'>Krankenhaus: {alert['hospital']}</div>" if alert['hospital'] else ""}
                <div style="font-size: 0.9em; color: #666;">Frist: {alert['deadline']}</div>
            </div>
            """
            st.markdown(alert_html, unsafe_allow_html=True)

    st.divider()

    # Bottom section: KPI Scoreboard
    st.subheader("📈 KPI-Scoreboard")

    kpi_data = [
        ["LG genehmigt (%)", f"{kpis['lg_approved']['percentage']}%", f"{kpis['lg_approved']['target']}%", kpis['lg_approved']['trend']],
        ["Qualität erfüllt (%)", f"{kpis['quality_fulfilled']['percentage']}%", f"{kpis['quality_fulfilled']['target']}%", kpis['quality_fulfilled']['trend']],
        ["Fonds allokiert (%)", f"{kpis['funds_allocated']['percentage']}%", f"{kpis['funds_allocated']['target']}%", kpis['funds_allocated']['trend']],
        ["Notfallversorgung erreichbar (%)", f"{kpis['emergency_accessible']['percentage']}%", f"{kpis['emergency_accessible']['target']}%", kpis['emergency_accessible']['trend']],
        ["Bettenauslastung (Ø)", f"{kpis['bed_occupancy']['current']}%", f"{kpis['bed_occupancy']['target_min']}-{kpis['bed_occupancy']['target_max']}%", kpis['bed_occupancy']['trend']],
    ]

    df_kpi = pd.DataFrame(kpi_data, columns=["Metrik", "Aktuell", "Ziel", "Trend"])
    st.dataframe(df_kpi, use_container_width=True, hide_index=True)


def view_regional():
    """Render the Regional view"""
    st.header("🗺️ Regional - Detailansicht")

    # Region selector
    selected_region = st.selectbox("Region auswählen:", REGIONS)

    if selected_region:
        st.subheader(f"Region: {selected_region}")

        # Get hospitals and coverage analysis
        hospitals = get_hospitals_for_region(selected_region)
        coverage = get_regional_coverage_analysis(selected_region)

        col1, col2, col3 = st.columns([2, 2, 2])

        # Left column: Hospitals in region
        with col1:
            st.write("### 🏥 Krankenhäuser")

            for hosp in hospitals:
                status_icon = render_status_badge(hosp["status"])
                with st.expander(f"{status_icon} {hosp['name']}", expanded=False):
                    st.write(f"**Status:** {hosp['level']}")
                    st.write(f"**Planbetten:** {hosp['beds']}")
                    st.write(f"**Mitarbeiter:** {hosp['staff']}")

                    render_progress_bar(hosp["lg_approved"], hosp["lg_total"], "Leistungsgruppen")

                    if hosp["quality_fulfilled"]:
                        st.success("✓ Qualitätskriterien erfüllt")
                    else:
                        st.error("✗ Qualitätskriterien nicht erfüllt")

                    if hosp["warnings"]:
                        for warning in hosp["warnings"]:
                            st.warning(f"⚠️ {warning}")

        # Middle column: Coverage analysis
        with col2:
            st.write("### 📊 Versorgungsanalyse")

            st.write("**Demographie:**")
            st.metric("Bevölkerung", f"{coverage['demographics']['population']:,}")
            st.metric("Durchschnittsalter", f"{coverage['demographics']['avg_age']} Jahre")
            st.metric("Prognose 2030", f"{coverage['demographics']['forecast_2030']:+d}%")

            st.write("**Erreichbarkeit:**")
            st.metric("Notfallversorgung (<30 min)", f"{coverage['accessibility']['emergency_30min']}%")
            st.metric("Spezialisierte Leistungen (<60 min)", f"{coverage['accessibility']['specialized_60min']}%")

            st.write("**Versorgungslücken:**")
            for gap in coverage["coverage_gaps"]:
                if gap["status"] == "missing":
                    st.error(f"🔴 {gap['lg']}: Fehlt komplett")
                else:
                    st.warning(f"🟡 {gap['lg']}: Unterversorgt")

        # Right column: Patient migration and timeline
        with col3:
            st.write("### 📈 Patientenstrom")

            st.write("**Abwanderung:**")
            for dest, pct in coverage["patient_migration"]["outbound"].items():
                st.write(f"→ {dest}: +{pct}%")

            st.write("**Zuwanderung:**")
            for source, pct in coverage["patient_migration"]["inbound"].items():
                st.write(f"← {source}: +{pct}%")

            st.divider()

            st.write("### 🗓️ Anstehende Termine")
            st.info("📅 20.12.2025: Audits Qualitätskriterien")
            st.info("📅 31.12.2025: Frist LG-Zuweisung")
            st.warning("⚠️ 15.01.2026: Personalausstattung-Nachweis")


def view_locations():
    """Render the Locations (Standorte) view"""
    st.header("🏥 Standorte - Krankenhausprofile")

    # Get all hospitals
    all_hospitals = []
    for region, hosps in HOSPITALS.items():
        for hosp in hosps:
            all_hospitals.append(hosp["name"])

    selected_hospital = st.selectbox("Krankenhaus auswählen:", all_hospitals)

    if selected_hospital:
        details = get_hospital_details(selected_hospital)

        if details:
            col1, col2 = st.columns([1, 2])

            # Left column: Hospital master data
            with col1:
                st.subheader("Stammdaten")

                st.write(f"**Name:** {details['name']}")
                st.write(f"**Versorgungsstufe:** {details['level']}")
                st.write(f"**Planungsbereich:** {details['region']}")
                st.write(f"**Planbetten:** {details['beds']}")
                st.write(f"**Mitarbeiter:** {details['staff']}")

                st.divider()

                st.write("**Qualitätskriterien:**")

                if details["quality"]["staff_ok"]:
                    st.success("✓ Personalausstattung erfüllt")
                else:
                    st.error("✗ Personalausstattung: 2 Ärzte fehlen")

                if details["quality"]["equipment_ok"]:
                    st.success("✓ Sachausstattung erfüllt")
                else:
                    st.error("✗ Sachausstattung nicht erfüllt")

                if details["quality"]["related_lg_ok"]:
                    st.success("✓ Verwandte LG vorhanden")
                else:
                    st.error("✗ Verwandte LG fehlen")

                st.divider()

                st.write("**Qualitätsindikatoren (letzte 6 Monate):**")
                st.metric("Komplikationsrate", f"{details['quality_indicators']['complication_rate']}%",
                         "Target: <2.5%")
                st.metric("30-Tage-Sterberate", f"{details['quality_indicators']['mortality_rate']}%",
                         "Target: <1.5%")
                st.metric("Patientenzufriedenheit", f"{details['quality_indicators']['satisfaction']}/5.0",
                         "Target: ≥3.5")

            # Right column: Leistungsgruppen status
            with col2:
                st.subheader("Leistungsgruppen-Status")

                total_lg = len(details["lg_approved"]) + len(details["lg_in_progress"]) + len(details["lg_rejected"])
                approved_lg = len(details["lg_approved"])

                render_progress_bar(approved_lg, total_lg, f"Gesamt: {approved_lg}/{total_lg}")

                st.divider()

                # Approved LGs
                st.write(f"**✅ Genehmigt ({len(details['lg_approved'])}):**")
                for lg in details["lg_approved"]:
                    st.success(f"✓ {lg}")

                st.divider()

                # In progress LGs
                if details["lg_in_progress"]:
                    st.write(f"**🕐 In Bearbeitung ({len(details['lg_in_progress'])}):**")
                    for lg in details["lg_in_progress"]:
                        st.warning(f"⟳ {lg['name']}\n\nStatus: {lg['status']} ({lg['date']})")

                    st.divider()

                # Rejected LGs
                if details["lg_rejected"]:
                    st.write(f"**❌ Abgelehnt ({len(details['lg_rejected'])}):**")
                    for lg in details["lg_rejected"]:
                        st.error(f"✗ {lg['name']}\n\nGrund: {lg['reason']}")


def view_quality():
    """Render the Quality (Qualität) view"""
    st.header("📊 Qualität - Klinische Indikatoren")

    # LG selector
    selected_lg = st.selectbox("Leistungsgruppe auswählen:", LEISTUNGSGRUPPEN)

    if selected_lg:
        st.subheader(f"Leistungsgruppe: {selected_lg}")

        # Get quality data
        quality_data = get_quality_data_for_lg(selected_lg)

        # Top section: Quality KPIs
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Komplikationsrate",
                f"{quality_data['complication_rate']['current']}%",
                f"Ziel: <{quality_data['complication_rate']['target']}%"
            )
            if quality_data['complication_rate']['current'] <= quality_data['complication_rate']['target']:
                st.success("✓ Im Plan")
            else:
                st.error("✗ Über Ziel")

        with col2:
            st.metric(
                "30-Tage-Mortalität",
                f"{quality_data['mortality_rate']['current']}%",
                f"Ziel: <{quality_data['mortality_rate']['target']}%"
            )
            if quality_data['mortality_rate']['current'] <= quality_data['mortality_rate']['target']:
                st.success("✓ Im Plan")
            else:
                st.error("✗ Über Ziel")

        with col3:
            st.metric(
                "Verweildauer (Ø)",
                f"{quality_data['avg_stay']['current']} Tage",
                f"Ziel: {quality_data['avg_stay']['target']}±{quality_data['avg_stay']['range']} Tag"
            )
            if abs(quality_data['avg_stay']['current'] - quality_data['avg_stay']['target']) <= quality_data['avg_stay']['range']:
                st.success("✓ Im Plan")
            else:
                st.warning("⚠ Abweichung")

        st.divider()

        # Trend chart
        st.subheader("📈 Trend-Entwicklung (12 Monate)")

        trend_df = get_quality_trends(selected_lg)

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=trend_df["month"],
            y=trend_df["complication_rate_sh"],
            mode='lines+markers',
            name='Schleswig-Holstein',
            line=dict(color='#007bff', width=3)
        ))

        fig.add_trace(go.Scatter(
            x=trend_df["month"],
            y=trend_df["complication_rate_bund"],
            mode='lines',
            name='Bundesweit (Baseline)',
            line=dict(color='#6c757d', width=2, dash='dash')
        ))

        fig.add_hline(
            y=quality_data['complication_rate']['target'],
            line_dash="dot",
            line_color="red",
            annotation_text="Zielwert"
        )

        fig.update_layout(
            title="Komplikationsrate über Zeit",
            xaxis_title="Monat",
            yaxis_title="Komplikationsrate (%)",
            height=400,
            hovermode='x unified'
        )

        st.plotly_chart(fig, use_container_width=True)

        st.divider()

        # Hospital comparison
        st.subheader("🏥 Standort-Vergleich")
        st.write(f"Qualitätsindikatoren für {selected_lg} - Vergleich aller Standorte")

        comparison_data = get_hospital_comparison(selected_lg)

        # Create heatmap-style table
        for comp in comparison_data:
            col_a, col_b, col_c, col_d, col_e = st.columns([3, 1, 1, 1, 1])

            with col_a:
                st.write(f"**{comp['hospital']}**")
            with col_b:
                st.write(render_status_badge(comp['complication']))
            with col_c:
                st.write(render_status_badge(comp['mortality']))
            with col_d:
                st.write(render_status_badge(comp['satisfaction']))
            with col_e:
                st.write(render_status_badge(comp['stay_duration']))

        # Legend
        st.caption("Legende: 🟢 Über Ziel | 🟡 Im Plan | 🔴 Unter Ziel")


def view_planning():
    """Render the Planning (Planung) view"""
    st.header("🗓️ Planung - Zeitstrahl & Meilensteine")

    st.subheader("Krankenhausreform Schleswig-Holstein: Zeitstrahl")

    events = get_timeline_events()

    # Group by quarter
    quarters = {}
    for event in events:
        quarter = event["quarter"]
        if quarter not in quarters:
            quarters[quarter] = []
        quarters[quarter].append(event)

    # Render timeline
    for quarter, quarter_events in quarters.items():
        st.write(f"### {quarter}")

        for event in quarter_events:
            # Status icon
            status_icons = {
                "completed": "✅",
                "in_progress": "🕐",
                "upcoming": "⏳",
                "planned": "📅",
                "goal": "🎯"
            }
            icon = status_icons.get(event["status"], "📅")

            # Status color
            if event["status"] == "completed":
                st.success(f"{icon} **{event['date']}** - {event['title']}")
                st.caption(event["description"])
            elif event["status"] == "in_progress":
                st.info(f"{icon} **{event['date']}** - {event['title']} *(aktuell)*")
                st.caption(event["description"])
            elif event["status"] == "upcoming":
                st.warning(f"{icon} **{event['date']}** - {event['title']}")
                st.caption(event["description"])
            elif event["status"] == "goal":
                st.error(f"{icon} **{event['date']}** - {event['title']}")
                st.caption(event["description"])
            else:
                st.write(f"{icon} **{event['date']}** - {event['title']}")
                st.caption(event["description"])

        st.divider()

    # Footer with data sources
    st.write("---")
    st.caption(f"**Letzte Aktualisierung:** {datetime.now().strftime('%d.%m.%Y %H:%M')} Uhr")
    st.caption("**Nächste Auto-Refresh:** 06.12.2025 17:00 Uhr")
    st.caption("**Datenquellen:** Ministerium, Landesverband der Krankenkassen, MDK, Routinedaten")


def main():
    """Main application"""
    # Render header
    render_header()

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Ansicht wählen:",
        ["📊 Überblick", "🗺️ Regional", "🏥 Standorte", "📈 Qualität", "🗓️ Planung"]
    )

    st.sidebar.divider()

    # Additional info
    st.sidebar.write("### 📍 Regionalkonferenzen")
    st.sidebar.write("• Flensburg")
    st.sidebar.write("• Kiel")
    st.sidebar.write("• Lübeck")
    st.sidebar.write("• Neumünster")
    st.sidebar.write("• Rendsburg")

    st.sidebar.divider()
    st.sidebar.write("### ℹ️ Info")
    st.sidebar.info("Dieses Dashboard zeigt den aktuellen Stand der Krankenhausreform in Schleswig-Holstein.")
    st.sidebar.caption("**Ziel:** 01.01.2027 - Alle Leistungsgruppen zugewiesen")

    # Route to selected page
    if page == "📊 Überblick":
        view_overview()
    elif page == "🗺️ Regional":
        view_regional()
    elif page == "🏥 Standorte":
        view_locations()
    elif page == "📈 Qualität":
        view_quality()
    elif page == "🗓️ Planung":
        view_planning()


if __name__ == "__main__":
    main()
