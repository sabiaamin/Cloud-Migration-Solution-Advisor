from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text
)
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

# This Python classes represents database table.

class Assessment(Base):
    __tablename__ = "assessments"

    id = Column(Integer, primary_key=True, index=True)

    application_type = Column(String(100), nullable=False)
    users = Column(Integer, nullable=False)

    infrastructure = Column(String(50), nullable=False)
    database = Column(String(50), nullable=False)

    traffic = Column(String(50), nullable=False)
    availability = Column(String(20), nullable=False)

    security = Column(String(50), nullable=False)
    storage = Column(String(50), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    requirements = relationship(
        "Requirement",
        back_populates="assessment",
        cascade="all, delete-orphan"
    )

    risks = relationship(
        "Risk",
        back_populates="assessment",
        cascade="all, delete-orphan"
    )

    recommendations = relationship(
        "Recommendation",
        back_populates="assessment",
        cascade="all, delete-orphan"
    )


class Requirement(Base):
    __tablename__ = "requirements"

    id = Column(Integer, primary_key=True, index=True)

    assessment_id = Column(
        Integer,
        ForeignKey("assessments.id"),
        nullable=False
    )

    category = Column(String(100), nullable=False)
    requirement = Column(Text, nullable=False)

    assessment = relationship(
        "Assessment",
        back_populates="requirements"
    )


class Risk(Base):
    __tablename__ = "risks"

    id = Column(Integer, primary_key=True, index=True)

    assessment_id = Column(
        Integer,
        ForeignKey("assessments.id"),
        nullable=False
    )

    category = Column(String(100), nullable=False)
    severity = Column(String(50), nullable=False)
    reason = Column(Text, nullable=False)
    mitigation = Column(Text, nullable=False)

    assessment = relationship(
        "Assessment",
        back_populates="risks"
    )


class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)

    assessment_id = Column(
        Integer,
        ForeignKey("assessments.id"),
        nullable=False
    )

    azure_service = Column(String(100), nullable=False)
    requirement = Column(Text, nullable=False)
    reason = Column(Text, nullable=False)

    assessment = relationship(
        "Assessment",
        back_populates="recommendations"
    )
