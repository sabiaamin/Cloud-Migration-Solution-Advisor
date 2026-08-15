from app import run_assessment

def test_run_assessment():
    assessment = run_assessment(
        "E-commerce",
        10000,
        "Cloud",
        "PostgreSQL",
        "Medium",
        "99.9%",
        "Medium",
        "500 GB - 2 TB"
    )

    assert "requirements" in assessment
    assert "risks" in assessment
    assert "recommendations" in assessment
    assert "migration_plan" in assessment
    assert "scoring" in assessment
    assert "overall_score" in assessment["scoring"]

