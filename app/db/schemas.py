from pydantic import BaseModel
from typing import Optional
from typing import List

class JobResponse(BaseModel):

    id: str

    status: str

    input_data: dict

    steps: List[dict] = []

    result: Optional[dict]

    class Config:
        from_attributes = True