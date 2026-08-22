# contains the structures describing API data

from typing import Literal

from pydantic import BaseModel,Field


class AssessmentRequest(BaseModel):
    application_type: Literal[
        "E-commerce",
        "Education",
        "Healthcare",
        "Finance",
        "Enterprise Application",
        "Other"
    ]

    users: int = Field(ge=100, le=1_000_000)

    infrastructure: Literal[
        "On-Premise",
        "Cloud",
        "Hybrid"
    ]

    database: Literal[
        "PostgreSQL",
        "MySQL",
        "SQL Server",
        "None"
    ]

    traffic: Literal[
        "Low",
        "Medium",
        "High"
    ]

    availability: Literal[
        "99%",
        "99.9%",
        "99.99%"
    ]

    security: Literal[
        "Low",
        "Medium",
        "High"
    ]

    storage: Literal[
        "Less than 500 GB",
        "500 GB - 2 TB",
        "More than 2 TB"
    ]

class AssessmentResponse(BaseModel):
    requirements: list
    risks: list
    recommendations: list
    migration_plan: list
    scoring: dict