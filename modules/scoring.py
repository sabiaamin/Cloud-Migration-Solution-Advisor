# Calculate cloud-readiness score

# weighted dimensions

INFRASTRUCTURE_WEIGHT = 0.15
SCALABILITY_WEIGHT = 0.20
AVAILABILITY_WEIGHT = 0.15
SECURITY_WEIGHT = 0.20
STORAGE_WEIGHT = 0.10
DATABASE_WEIGHT = 0.20


def calculate_infrastructure_score(infrastructure):
    if infrastructure == "Cloud":
        return 100
    elif infrastructure == "Hybrid":
        return 80
    else:
        return 60


def calculate_scalability_score(users, traffic):
    if users < 10000:
        if traffic == "Low":
            return 90
        elif traffic == "Medium":
            return 80
        else:
            return 70

    elif users < 50000:
        if traffic == "Low":
            return 85
        elif traffic == "Medium":
            return 75
        else:
            return 65

    else:
        if traffic == "Low":
            return 80
        elif traffic == "Medium":
            return 70
        else:
            return 60


def calculate_availability_score(availability):
    if availability == "99%":
        return 100
    elif availability == "99.9%":
        return 85
    else:
        return 70


def calculate_security_score(security):
    if security == "Low":
        return 100
    elif security == "Medium":
        return 85
    else:
        return 70


def calculate_storage_score(storage):
    if storage == "Less than 500 GB":
        return 100
    elif storage == "500 GB - 2 TB":
        return 85
    else:
        return 70


def calculate_database_score(database):
    if database == "MySQL":
        return 90
    elif database == "PostgreSQL":
        return 90
    elif database == "SQL Server":
        return 80
    else:
        return 100


def calculate_cloud_readiness(
    users,
    infrastructure,
    traffic,
    availability,
    security,
    storage,
    database
):
    """Calculate the application's overall cloud readiness score."""

    infrastructure_score = calculate_infrastructure_score(
        infrastructure
    )

    scalability_score = calculate_scalability_score(
        users,
        traffic
    )

    availability_score = calculate_availability_score(
        availability
    )

    security_score = calculate_security_score(
        security
    )

    storage_score = calculate_storage_score(
        storage
    )

    database_score = calculate_database_score(
        database
    )

    overall_score = (
        infrastructure_score * INFRASTRUCTURE_WEIGHT
        + scalability_score * SCALABILITY_WEIGHT
        + availability_score * AVAILABILITY_WEIGHT
        + security_score * SECURITY_WEIGHT
        + storage_score * STORAGE_WEIGHT
        + database_score * DATABASE_WEIGHT
    )

    return {
        "overall_score": round(overall_score),
        "infrastructure": infrastructure_score,
        "scalability": scalability_score,
        "availability": availability_score,
        "security": security_score,
        "storage": storage_score,
        "database": database_score
    }