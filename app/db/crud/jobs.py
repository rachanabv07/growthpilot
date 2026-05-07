from app.db.models import Job


def create_job(db, job_id, input_data):

    job = Job(
        id=job_id,
        status="pending",
        input_data=input_data,
        result=None
    )

    db.add(job)

    db.commit()

    db.refresh(job)

    return job

def update_job(
    db,
    job_id,
    status=None,
    result=None
):

    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        return None

    if status:
        job.status = status

    if result:
        job.result = result

    db.commit()

    db.refresh(job)

    return job

def get_all_jobs(db):

    return db.query(Job).all()

def add_step(
    db,
    job_id,
    step_name,
    status
):

    job = db.query(Job).filter(
        Job.id == job_id
    ).first()

    if not job:
        return None

    steps = job.steps or []

    steps.append({
        "step": step_name,
        "status": status
    })

    job.steps = steps

    db.commit()

    db.refresh(job)

    return job