# import workflow module from temporalio
from temporalio import workflow
# import the compute_sum activity from activitie.py
from worker.activities import compute_sum

from temporalio.common import RetryPolicy

# decorate the class as a Temporal workflow
@workflow.defn
class SumWorkflow:
    # decorate the function to run in the workflow
    @workflow.run
    # fail_first_attempt is False by default
    async def run(self,numbers,fail_first_attempt=False):
        # execute the compute_sum activity with passed in arguments
        result = await workflow.execute_activity(
            compute_sum,
            numbers,
            fail_first_attempt=fail_first_attempt,
            schedule_to_close_timeout=10,
            retry_policy=RetryPolicy(maximum_attempts=3)
        )
        # return the result of the activity
        return result