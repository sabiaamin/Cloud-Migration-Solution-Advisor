from modules.recommendation_engine import generate_recommendations

def test_database_recommendation():
    recommendations = generate_recommendations(
        "E-commerce",
        "PostgreSQL",
        "Less than 500 GB",
        "Low",
        "Low"
    )

    assert any(
        recommendation["azure_service"] == "Azure Database for PostgreSQL"
        for recommendation in recommendations
    )

def test_storage_recommendation():
    recommendations = generate_recommendations(
        "E-commerce",
        "None",
        "More than 2 TB",
        "Low",
        "Low"
    )

    assert any(
        recommendation["azure_service"] == "Azure Blob Storage"
        for recommendation in recommendations
    )

def test_security_recommendation():
    recommendations = generate_recommendations(
        "E-commerce",
        "None",
        "Less than 500 GB",
        "High",
        "Low"
    )

    assert any(
        recommendation["azure_service"] == "Microsoft Entra ID"
        for recommendation in recommendations
    )

def test_application_hosting_recommendation():
    recommendations = generate_recommendations(
        "E-commerce",
        "None",
        "Less than 500 GB",
        "Low",
        "Low"
    )

    assert any(
        recommendation["azure_service"] == "Azure App Service"
        for recommendation in recommendations
    )

