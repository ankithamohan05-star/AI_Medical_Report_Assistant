from pydantic import BaseModel


# ---------------- Patient Information ---------------- #

class PatientInformation(BaseModel):
    name: str
    age: str
    gender: str
    report_date: str


# ---------------- Abnormal Findings ---------------- #

class AbnormalFinding(BaseModel):

    test: str

    result: str

    numeric_result: float | None

    unit: str

    normal_range: str

    status: str

    severity: str

    priority: str

    explanation: str


# ---------------- Normal Findings ---------------- #

class NormalFindingGroup(BaseModel):

    category: str

    tests: list[str]


# ---------------- Comparison Result ---------------- #

class ComparisonResult(BaseModel):

    test: str

    previous_result: str

    current_result: str

    previous_numeric: float | None

    current_numeric: float | None

    unit: str

    difference: float | None

    trend: str


# ---------------- Medical Report ---------------- #

class MedicalReport(BaseModel):

    patient_information: PatientInformation

    executive_summary: str

    abnormal_findings: list[AbnormalFinding]

    normal_findings: list[NormalFindingGroup]

    recommendations: list[str]

    disclaimer: str