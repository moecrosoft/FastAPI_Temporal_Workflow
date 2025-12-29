import asyncio

# import Client and Worker modules from temporalio
from temporalio.client import Client
from temporalio.worker import Worker

# import the workflow and activity modules
from worker.workflows import SumWorkflow
from worker.activities import compute_sum

async def main():
    # connect to Temporal server
    client = await Client.connect("localhost:7233")
    # create a worker
    worker = Worker(
        client,
        task_queue='sum-numbers',
        workflows=[SumWorkflow],
        activities=[compute_sum]
    )
    # run the worker
    await worker.run()

# when this script is run, execute the main function
if __name__ == '__main__':
    asyncio.run(main())
