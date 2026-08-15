# Identify risks

def assess_risks(users,
                 infrastructure,
                 traffic,
                 availability,
                 security,
                 storage):
    """Identify migration risks based on application characteristics."""

    risks = []

    # Scalability risk
    if users >= 10000 and traffic == "High":
        risks.append({
            "category": "Scalability",
            "severity": "High",
            "reason": "High user volume and traffic may cause performance degradation.",
            "mitigation": "Use scalable cloud compute resources and monitor application load."
        })

    elif users >= 5000:
        risks.append({
            "category": "Scalability",
            "severity": "Medium",
            "reason": "Increasing user volume may require additional compute capacity.",
            "mitigation": "Plan for scalable application infrastructure."
        })

    # Availability risk
    if infrastructure == "On-Premise" and availability in ["99.9%", "99.99%"]:
        risks.append({
            "category": "Availability",
            "severity": "High",
            "reason": "The existing infrastructure may not provide sufficient redundancy.",
            "mitigation": "Use highly available cloud infrastructure and appropriate monitoring."
        })

    # Security risk
    if security == "High":
        risks.append({
            "category": "Security",
            "severity": "Medium",
            "reason": "Sensitive workloads require stronger identity and access controls.",
            "mitigation": "Use managed identity and access-control mechanisms."
        })

    # Migration risk
    if infrastructure == "On-Premise":
        risks.append({
            "category": "Migration",
            "severity": "Medium",
            "reason": "Moving an existing application may introduce compatibility and downtime risks.",
            "mitigation": "Use a phased migration approach with testing before production deployment."
        })

    # Storage risk
    if storage == "More than 2 TB":
        risks.append({
            "category": "Storage",
            "severity": "Medium",
            "reason": "Large storage requirements can increase migration time and management complexity.",
            "mitigation": "Use scalable cloud storage and migrate data in controlled stages."
        })

    return risks