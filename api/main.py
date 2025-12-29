# import fastapi, temporalio client and the SumWorkflow
from fastapi import FastAPI
from temporalio.client import Client
from worker.workflows import SumWorkflow

# create a FastAPI app
app = FastAPI()
client = None

# when the fastapi is called, connect to Temporal server
@app.on_event('startup')
async def startup_event():
    global client
    client = await Client.connect('localhost:7233')

# function to run when a POST request is made to /jobs
@app.post('/jobs')
# accept a JSON input with numbers and fail_first_attempt option
async def start_job(payload: dict):
    numbers = payload['input']['numbers']
    fail_first = payload['options'].get('fail_first_attempt', False)
    # run ths SumWorkflow
    handle = await client.start_workflow(
        SumWorkflow.run,
        args=(numbers, fail_first),
        id=f'job-{id(numbers)}',
        task_queue='sum-numbers'
    )
    # return the job id
    return {'job-id': handle.id}

# function to run when a GET request is made to /jobs/{job_id}
@app.get('/jobs/{job_id}')
# accept job_id as input
async def get_job_status(job_id: str):
    # get handle of the job
    handle = client.get_workflow_handle(job_id)
    # get workflow info
    info = await handle.describe()  
    # check the status
    status = info.status.name  

    # get the result only when job is completed
    result = None
    if status == "COMPLETED":
        result = await handle.result()  

    progress = {"stage": "compute", "history_length": info.history_length}

    # return the dict response, fastapi will convert it to json
    return {
        "job_id": job_id,
        "status": status,
        "progress": progress,
        "result": result,
        "error": None
    }

