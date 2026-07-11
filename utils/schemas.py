from pydantic import BaseModel


class PatientInformation(BaseModel):
    name: str
    age: str
    gender: str
    report_date: str


class AbnormalFinding(BaseModel):
    test: str
    result: str
    normal_range: str
    status: str
    explanation: str


class MedicalReport(BaseModel):
    patient_information: PatientInformation
    executive_summary: str
    abnormal_findings: list[AbnormalFinding]
    normal_findings: list[str]
    recommendations: list[str]
    disclaimer: str