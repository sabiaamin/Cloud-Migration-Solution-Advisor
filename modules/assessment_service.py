from modules.requirement_analyzer import analyze_requirements
from modules.risk_engine import assess_risks
from modules.recommendation_engine import generate_recommendations
from modules.migration_planner import create_migration_plan
from modules.scoring import calculate_cloud_readiness

# Assessement Logic

def run_assessment(
    application_type,
    users,
    infrastructure,
    database,
    traffic,
    availability,
    security,
    storage
):
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

    risks = assess_risks(
        users,
        infrastructure,
        traffic,
        availability,
        security,
        storage
    )

    recommendations = generate_recommendations(
        application_type,
        database,
        storage,
        security,
        traffic
    )

    migration_plan = create_migration_plan(
        infrastructure
    )

    score = calculate_cloud_readiness(
        users,
        infrastructure,
        traffic,
        availability,
        security,
        storage,
        database
    )

    return {
        "requirements": requirements,
        "risks": risks,
        "recommendations": recommendations,
        "migration_plan": migration_plan,
        "scoring": score
    }