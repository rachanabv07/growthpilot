from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.db.deps import get_db

from app.db.crud.jobs import get_all_jobs
from app.db.schemas import JobResponse
from typing import List


router = APIRouter()


@router.get(
    "/jobs",
    response_model=List[JobResponse]
)
async def jobs(
    db: Session = Depends(get_db)
):

    all_jobs = get_all_jobs(db)

    return all_jobs