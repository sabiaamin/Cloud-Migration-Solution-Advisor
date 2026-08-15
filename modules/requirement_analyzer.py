# Analyze technical requirements

def analyze_requirements(application_type,
                         users,
                         infrastructure,
                         database,
                         traffic,
                         availability,
                         security,
                         storage):
    """Analyze application inputs and identify technical requirements."""

    requirements = []

    # Scalability
    if users >= 10000 or traffic == "High":
        requirements.append({
            "category": "Scalability",
            "requirement": "Application should support scalable compute resources."
        })

    # Availability
    if availability in ["99.9%", "99.99%"]:
        requirements.append({
            "category": "Availability",
            "requirement": "Application should provide high availability."
        })

    # Security
    if security == "High":
        requirements.append({
            "category": "Security",
            "requirement": "Application should provide strong identity and access controls."
        })

    # Storage
    if storage in ["500 GB - 2 TB", "More than 2 TB"]:
        requirements.append({
            "category": "Storage",
            "requirement": "Application requires scalable and reliable object storage."
        })

    # Database
    if database in ["MySQL", "PostgreSQL", "SQL Server"]:
        requirements.append({
            "category": "Database",
            "requirement": "Application requires a managed relational database."
        })

    # Infrastructure
    if infrastructure == "On-Premise":
        requirements.append({
            "category": "Migration",
            "requirement": "Existing infrastructure requires a structured cloud migration approach."
        })

    return requirements
