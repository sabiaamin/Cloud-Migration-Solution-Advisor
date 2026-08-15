from modules.risk_engine import assess_risks

def test_high_scalability_risk():
    risks = assess_risks(
        10000,
        "Cloud",
        "High",
        "99%",
        "Low",
        "Less than 500 GB"
    )

    assert any(
        risk["category"] == "Scalability"
        and risk["severity"] == "High"
        for risk in risks
    )

def test_availability_risk():
    risks = assess_risks(
        1000,
        "On-Premise",
        "Low",
        "99.99%",
        "Low",
        "Less than 500 GB"
    )

    assert any(
        risk["category"] == "Availability"
        and risk["severity"] == "High"
        for risk in risks
    )

def test_security_risk():
    risks = assess_risks(
        1000,
        "Cloud",
        "Low",
        "99%",
        "High",
        "Less than 500 GB"
    )

    assert any(
        risk["category"] == "Security"
        and risk["severity"] == "Medium"
        for risk in risks
    )
def test_storage_risk():
    risks = assess_risks(
        1000,
        "Cloud",
        "Low",
        "99%",
        "Low",
        "More than 2 TB"
    )

    assert any(
        risk["category"] == "Storage"
        and risk["severity"] == "Medium"
        for risk in risks
    )

def test_no_major_risks():
    risks = assess_risks(

        1000,
        "Cloud",
        "Low",
        "99%",
        "Low",
        "Less than 500 GB"
    )

    assert risks == []

