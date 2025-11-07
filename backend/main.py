# FastAPI app entrypoint
from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from .converters import pdf_to_text, image_to_png
from .storage import set_status, get_status
import uuid
app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...), background_tasks: BackgroundTasks = None):
    # TODO: save uploaded file to disk
    task_id = str(uuid.uuid4())
    set_status(task_id, "queued")
    # background_tasks.add_task(convert_worker, task_id, saved_path, file.content_type)
    return {"task_id": task_id}

@app.get("/status/{task_id}")
def status(task_id: str):
    return get_status(task_id)
