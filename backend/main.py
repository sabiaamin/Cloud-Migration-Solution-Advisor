from fastapi import FastAPI

from backend.schemas import AssessmentRequest, AssessmentResponse

from modules.assessment_service import run_assessment

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Cloud Migration Solution Advisor API"
    }


@app.post(
    "/assessment",
    response_model=AssessmentResponse
)
def create_assessment(assessment: AssessmentRequest):
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

    return result