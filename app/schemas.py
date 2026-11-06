from typing import Annotated

from pydantic import BaseModel, StringConstraints, ConfigDict, Field

StudentIDStr = Annotated[str, StringConstraints(pattern=r"^ST-\d{4}$")]
DescriptionStr = Annotated[str, StringConstraints(min_length=5, max_length=100)]

class RequestCreate(BaseModel):
    equipment_id: int = Field(gt=0)
    student_id: StudentIDStr
    description: DescriptionStr
    priority: int = Field(gt=0, lt=6)
    status: str = Field("OPEN")

class RequestRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id:int
    equipment_id: int = Field(gt=0)
    student_id: StudentIDStr
    description: DescriptionStr
    priority: int = Field(gt=0, lt=6)
    status: str = Field("OPEN")
