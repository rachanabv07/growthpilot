from app.db.session import SessionLocal

from app.db.crud.jobs import update_job, add_step

from app.workers.workflow import run_workflow


def process_job(job_id, input_data):
    db = SessionLocal()

    try:
        update_job(db=db, job_id=job_id, status="running")

        

        result = run_workflow(input_data)
        add_step(db, job_id, "content_generation", "running")

        update_job(db=db, job_id=job_id, status="completed", result=result)
        add_step(db, job_id, "content_generation", "completed")
    except Exception as e:
        update_job(db=db, job_id=job_id, status="failed", result={"error": str(e)})

    finally:
        db.close()
