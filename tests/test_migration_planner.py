from modules.migration_planner import create_migration_plan

def test_migration_plan_created():
    plan = create_migration_plan("On-Premise")

    assert plan

def test_migration_plan_has_seven_phases():
    plan = create_migration_plan("On-Premise")

    assert len(plan) == 7

def test_migration_plan_phases():
    plan = create_migration_plan("On-Premise")

    assert plan[0]["phase"] == "1. Assessment"
    assert plan[-1]["phase"] == "7. Monitoring"

