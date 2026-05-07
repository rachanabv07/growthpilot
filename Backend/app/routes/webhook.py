from fastapi import (
    APIRouter,
    Depends,
    BackgroundTasks
)
from sqlalchemy.orm import Session
from app.workers.job_runners import process_job
from pydantic import BaseModel

import uuid

from app.db.deps import get_db

from app.db.crud.jobs import (
    create_job,
    update_job
)

from app.workers.workflow import run_workflow

router = APIRouter()


class EventInput(BaseModel):
    event: str
    note: str
    date: str


@router.post("/webhook")
async def webhook(
    data: EventInput,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):

    job_id = str(uuid.uuid4())

    # Create DB Job
    create_job(
        db=db,
        job_id=job_id,
        input_data=data.dict()
    )

    background_tasks.add_task(
        process_job,
        job_id,
        data.dict()
    )

    # Update status -> running
    update_job(
        db=db,
        job_id=job_id,
        status="running"
    )

    # try:

    #     result = run_workflow(data.dict())

    #     update_job(
    #         db=db,
    #         job_id=job_id,
    #         status="completed",
    #         result=result
    #     )

    # except Exception as e:

    #     update_job(
    #         db=db,
    #         job_id=job_id,
    #         status="failed",
    #         result={"error": str(e)}
    #     )

    return {
        "job_id": job_id,
        "status": "accepted"
    }
