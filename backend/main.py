from fastapi import Depends
from sqlalchemy.orm import Session

from backend.database.database import get_db
from backend.database.models import (
    Assessment,
    Requirement,
    Risk,
    Recommendation
)

from fastapi import FastAPI

from backend.schemas import AssessmentRequest, AssessmentResponse

from modules.assessment_service import run_assessment

from fastapi import Depends, HTTPException

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Cloud Migration Solution Advisor API"
    }

@app.get("/assessment/{assessment_id}")
def get_assessment(
    assessment_id: int,
    db: Session = Depends(get_db)
):
    db_assessment = db.get(Assessment, assessment_id)

    if db_assessment is None:
        raise HTTPException(
            status_code=404,
            detail="Assessment not found"
        )
    return {
        "id": db_assessment.id,
        "application_type": db_assessment.application_type,
        "users": db_assessment.users,
        "infrastructure": db_assessment.infrastructure,
        "database": db_assessment.database,
        "traffic": db_assessment.traffic,
        "availability": db_assessment.availability,
        "security": db_assessment.security,
        "storage": db_assessment.storage,

        "requirements": [
            {
                "id": item.id,
                "category": item.category,
                "requirement": item.requirement
            }
            for item in db_assessment.requirements
        ],

        "risks": [
            {
                "id": item.id,
                "category": item.category,
                "severity": item.severity,
                "reason": item.reason,
                "mitigation": item.mitigation
            }
            for item in db_assessment.risks
        ],

        "recommendations": [
            {
                "id": item.id,
                "requirement": item.requirement,
                "azure_service": item.azure_service,
                "reason": item.reason
            }
            for item in db_assessment.recommendations
        ]
    }

@app.post(
    "/assessment",
    response_model=AssessmentResponse
)
def create_assessment(
        assessment: AssessmentRequest,
        db: Session = Depends(get_db)
                      ):
    result = run_assessment(
        assessment.application_type,
        assessment.users,
        assessment.infrastructure,
        assessment.database,
        assessment.traffic,
        assessment.availability,
        assessment.security,
        assessment.storage
    )
    db_assessment = Assessment(
        application_type=assessment.application_type,
        users=assessment.users,
        infrastructure=assessment.infrastructure,
        database=assessment.database,
        traffic=assessment.traffic,
        availability=assessment.availability,
        security=assessment.security,
        storage=assessment.storage
    )
    try:
        db.add(db_assessment)
        db.flush()

        for item in result["requirements"]:
            requirement = Requirement(
                assessment_id=db_assessment.id,
                category=item["category"],
                requirement=item["requirement"]
            )
            db.add(requirement)

        for item in result["risks"]:
            risk = Risk(
                assessment_id=db_assessment.id,
                category=item["category"],
                severity=item["severity"],
                reason=item["reason"],
                mitigation=item["mitigation"]
            )
            db.add(risk)

        for item in result["recommendations"]:
            recommendation = Recommendation(
                assessment_id=db_assessment.id,
                azure_service=item["azure_service"],
                requirement=item["requirement"],
                reason=item["reason"]
            )
            db.add(recommendation)

        db.commit()
    except Exception:
        db.rollback()
        raise

    return result

