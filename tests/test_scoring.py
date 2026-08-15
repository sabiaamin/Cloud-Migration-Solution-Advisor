from modules.scoring import (
    calculate_infrastructure_score,
    calculate_scalability_score,
    calculate_availability_score,
    calculate_security_score,
    calculate_storage_score,
    calculate_database_score,
    calculate_cloud_readiness
)
def test_infrastructure_score():
    assert calculate_infrastructure_score("Cloud") == 100
    assert calculate_infrastructure_score("Hybrid") == 80
    assert calculate_infrastructure_score("On-Premise") == 60

def test_availability_score():
    assert calculate_availability_score("99%") == 100
    assert calculate_availability_score("99.9%") == 85
    assert calculate_availability_score("99.99%") == 70

def test_security_score():
    assert calculate_security_score("Low") == 100
    assert calculate_security_score("Medium") == 85
    assert calculate_security_score("High") == 70

def test_storage_score():
    assert calculate_storage_score("Less than 500 GB") == 100
    assert calculate_storage_score("500 GB - 2 TB") == 85
    assert calculate_storage_score("More than 2 TB") == 70

def test_database_score():
    assert calculate_database_score("MySQL") == 90
    assert calculate_database_score("PostgreSQL") == 90
    assert calculate_database_score("SQL Server") == 80
    assert calculate_database_score("None") == 100

def test_scalability_score():
    assert calculate_scalability_score(5000, "Low") == 90
    assert calculate_scalability_score(5000, "Medium") == 80
    assert calculate_scalability_score(5000, "High") == 70

    assert calculate_scalability_score(20000, "Low") == 85
    assert calculate_scalability_score(20000, "Medium") == 75
    assert calculate_scalability_score(20000, "High") == 65

    assert calculate_scalability_score(50000, "Low") == 80
    assert calculate_scalability_score(50000, "Medium") == 70
    assert calculate_scalability_score(50000, "High") == 60

def test_cloud_readiness_score():
    result = calculate_cloud_readiness(
        10000,
        "Cloud",
        "Medium",
        "99.9%",
        "Medium",
        "500 GB - 2 TB",
        "PostgreSQL"
    )

    assert result["overall_score"] == 86
    assert result["infrastructure"] == 100
    assert result["scalability"] == 75
    assert result["availability"] == 85
    assert result["security"] == 85
    assert result["storage"] == 85
    assert result["database"] == 90