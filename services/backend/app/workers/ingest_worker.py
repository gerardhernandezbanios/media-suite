# services/backend/app/workers/ingest_worker.py

import time
from core.container import Container
from media.domain.value_objects.job_status import JobStatus

def run_worker(poll_interval: int = 2):
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])

    job_port = container.job_port()
    process_job = container.process_job_use_case()

    print("Worker iniciado. Esperando jobs...")

    while True:
        pending_jobs = job_port.list_pending_jobs()

        if not pending_jobs:
            time.sleep(poll_interval)
            continue

        for job in pending_jobs:
            print(f"Procesando job {job.job_id}")
            try:
                process_job.execute(job.job_id)
                print(f"Job {job.job_id} completado")
            except Exception as e:
                print(f"Error procesando job {job.job_id}: {e}")

        time.sleep(poll_interval)

