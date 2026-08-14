import streamlit as st

from modules.requirement_analyzer import analyze_requirements
from modules.risk_engine import assess_risks
from modules.recommendation_engine import generate_recommendations
from modules.migration_planner import create_migration_plan
from modules.scoring import calculate_cloud_readiness


# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Cloud Migration & Solution Advisor",
    page_icon="☁️",
    layout="wide"
)


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.title("Cloud Migration & Solution Advisor")

st.write(
    "Assess application requirements, identify common migration risks, "
    "and receive preliminary Azure service recommendations."
)

st.divider()


# ---------------------------------------------------------
# Application Information
# ---------------------------------------------------------

st.header("Application Assessment")

col1, col2 = st.columns(2)

with col1:

    application_type = st.selectbox(
        "Application Type",
        [
            "E-commerce",
            "Education",
            "Healthcare",
            "Finance",
            "Enterprise Application",
            "Other"
        ]
    )

    users = st.number_input(
        "Expected Number of Users",
        min_value=100,
        max_value=1000000,
        value=10000,
        step=1000
    )

    infrastructure = st.selectbox(
        "Current Infrastructure",
        [
            "On-Premise",
            "Cloud",
            "Hybrid"
        ]
    )

    database = st.selectbox(
        "Database",
        [
            "PostgreSQL",
            "MySQL",
            "SQL Server",
            "None"
        ]
    )

with col2:

    traffic = st.selectbox(
        "Expected Traffic",
        [
            "Low",
            "Medium",
            "High"
        ]
    )

    availability = st.selectbox(
        "Availability Requirement",
        [
            "99%",
            "99.9%",
            "99.99%"
        ]
    )

    security = st.selectbox(
        "Security Requirement",
        [
            "Low",
            "Medium",
            "High"
        ]
    )

    storage = st.selectbox(
        "Storage Requirement",
        [
            "Less than 500 GB",
            "500 GB - 2 TB",
            "More than 2 TB"
        ]
    )


st.divider()


# ---------------------------------------------------------
# Analyze Button
# ---------------------------------------------------------

if st.button("Analyze Application", type="primary"):

    # Requirement analysis
    requirements = analyze_requirements(
        application_type,
        users,
        infrastructure,
        database,
        traffic,
        availability,
        security,
        storage
    )

    # Risk analysis
    risks = assess_risks(
        users,
        infrastructure,
        traffic,
        availability,
        security,
        storage
    )

    # Azure recommendations
    recommendations = generate_recommendations(
        application_type,
        database,
        storage,
        security,
        traffic
    )

    # Migration roadmap
    migration_plan = create_migration_plan(
        infrastructure
    )

    # Cloud readiness score
    score = calculate_cloud_readiness(
        users,
        infrastructure,
        traffic,
        availability,
        security,
        storage
    )


    # -----------------------------------------------------
    # Results
    # -----------------------------------------------------

    st.header("Assessment Results")

    score_col, risk_col = st.columns(2)

    with score_col:

        st.metric(
            "Cloud Readiness Score",
            f"{score}/100"
        )

    with risk_col:

        st.metric(
            "Risks Identified",
            len(risks)
        )


    # -----------------------------------------------------
    # Technical Requirements
    # -----------------------------------------------------

    st.subheader("Technical Requirements")

    if requirements:

        for requirement in requirements:

            st.write(
                f"**{requirement['category']}** — "
                f"{requirement['requirement']}"
            )

    else:

        st.info(
            "No additional technical requirements were identified."
        )


    # -----------------------------------------------------
    # Risk Assessment
    # -----------------------------------------------------

    st.subheader("Risk Assessment")

    if risks:

        for risk in risks:

            if risk["severity"] == "High":

                st.error(
                    f"**{risk['category']} — {risk['severity']}**\n\n"
                    f"{risk['reason']}\n\n"
                    f"**Mitigation:** {risk['mitigation']}"
                )

            else:

                st.warning(
                    f"**{risk['category']} — {risk['severity']}**\n\n"
                    f"{risk['reason']}\n\n"
                    f"**Mitigation:** {risk['mitigation']}"
                )

    else:

        st.success("No major risks identified.")


    # -----------------------------------------------------
    # Azure Recommendations
    # -----------------------------------------------------

    st.subheader("Recommended Azure Services")

    for recommendation in recommendations:

        with st.container(border=True):

            st.write(
                f"**{recommendation['requirement']}**"
            )

            st.write(
                f"**Recommended Service:** "
                f"{recommendation['azure_service']}"
            )

            st.write(
                recommendation["reason"]
            )


    # -----------------------------------------------------
    # Migration Roadmap
    # -----------------------------------------------------

    st.subheader("Migration Roadmap")

    for step in migration_plan:

        st.write(
            f"**{step['phase']}**"
        )

        st.write(
            step["activities"]
        )

        st.write("")