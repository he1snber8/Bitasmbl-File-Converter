# simple in-memory store for task status and result URL
STATUS = {}

def set_status(task_id, state, url=None):
    STATUS[task_id] = {"task_id": task_id, "status": state, "url": url}

def get_status(task_id):
    return STATUS.get(task_id, {"task_id": task_id, "status": "unknown", "url": None})
