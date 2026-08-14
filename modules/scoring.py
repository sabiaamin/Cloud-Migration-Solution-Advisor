def calculate_cloud_readiness(users,
                              infrastructure,
                              traffic,
                              availability,
                              security,
                              storage):

    score = 100

    # Infrastructure
    if infrastructure == "On-Premise":
        score -= 10

    # Scalability
    if users >= 50000 and traffic == "High":
        score -= 10
    elif users >= 10000:
        score -= 5

    # Availability
    if availability == "99.99%":
        score -= 5

    # Security
    if security == "High":
        score -= 5

    # Storage
    if storage == "More than 2 TB":
        score -= 5

    return max(score, 0)