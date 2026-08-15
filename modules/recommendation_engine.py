# Generate Azure recommendations

def generate_recommendations(application_type,
                              database,
                              storage,
                              security,
                              traffic):
    """Generate Azure service recommendations based on application requirements."""

    recommendations = []

    # Application hosting
    recommendations.append({
        "requirement": "Application Hosting",
        "azure_service": "Azure App Service",
        "reason": "Provides managed hosting for web applications without requiring direct server management."
    })

    # Database
    if database in ["MySQL", "PostgreSQL", "SQL Server"]:
        if database == "PostgreSQL":
            service = "Azure Database for PostgreSQL"
        elif database == "MySQL":
            service = "Azure Database for MySQL"
        else:
            service = "Azure SQL Database"

        recommendations.append({
            "requirement": "Relational Database",
            "azure_service": service,
            "reason": "Provides a managed relational database environment."
        })

    # Storage
    if storage in ["500 GB - 2 TB", "More than 2 TB"]:
        recommendations.append({
            "requirement": "File/Object Storage",
            "azure_service": "Azure Blob Storage",
            "reason": "Suitable for storing large volumes of unstructured data."
        })

    # Security
    if security == "High":
        recommendations.append({
            "requirement": "Identity & Access",
            "azure_service": "Microsoft Entra ID",
            "reason": "Provides identity and access management capabilities."
        })

    # Monitoring
    recommendations.append({
        "requirement": "Application Monitoring",
        "azure_service": "Azure Monitor",
        "reason": "Provides monitoring and visibility into application performance and health."
    })

    return recommendations