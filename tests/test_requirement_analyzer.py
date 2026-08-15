from modules.requirement_analyzer import analyze_requirements

def test_scalability_requirement():
    requirements = analyze_requirements(
        "E-commerce",
        10000,
        "Cloud",
        "PostgreSQL",
        "Low",
        "99%",
        "Low",
        "Less than 500 GB"
    )

    assert any(
        requirement["category"] == "Scalability"
        for requirement in requirements
    )

def test_availability_requirement():
    requirements = analyze_requirements(
        "E-commerce",
        1000,
        "Cloud",
        "PostgreSQL",
        "Low",
        "99.9%",
        "Low",
        "Less than 500 GB"
    )

    assert any(
        requirement["category"] == "Availability"
        for requirement in requirements
    )

def test_security_requirement():
    requirements = analyze_requirements(
        "E-commerce",
        1000,
        "Cloud",
        "PostgreSQL",
        "Low",
        "99%",
        "High",
        "Less than 500 GB"
    )

    assert any(
        requirement["category"] == "Security"
        for requirement in requirements
    )

def test_database_requirement():
    requirements = analyze_requirements(
        "E-commerce",
        1000,
        "Cloud",
        "PostgreSQL",
        "Low",
        "99%",
        "Low",
        "Less than 500 GB"
    )

    assert any(
        requirement["category"] == "Database"
        for requirement in requirements
    )

def test_migration_requirement():
    requirements = analyze_requirements(
        "E-commerce",
        1000,
        "On-Premise",
        "PostgreSQL",
        "Low",
        "99%",
        "Low",
        "Less than 500 GB"
    )

    assert any(
        requirement["category"] == "Migration"
        for requirement in requirements
    )