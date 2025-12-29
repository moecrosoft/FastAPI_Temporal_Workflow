# import activity module from temporalio

from temporalio import activity 

# decorate the function as a Temporal activity
@activity.defn
async def compute_sum(numbers, fail_first_attempt=False):
    attempt = activity.info().attempt
    # if fail_first_attempt is True and this is the first attempt, retry
    if fail_first_attempt and attempt == 1:
        raise Exception('Intentional failure on first attempt')
    # compute and return the sum of the numbers
    return sum(numbers)