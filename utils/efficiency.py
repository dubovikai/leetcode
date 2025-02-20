import sys
from functools import wraps
from time import perf_counter
from memory_profiler import profile

def check_efficiency(f):
    """
    A decorator to check the efficiency of a function in terms of both time and memory usage.
    Important: it works with debugpy debugger.
    
    This decorator runs the target function multiple times to measure its average execution time and 
    also prints memory usage statistics using the memory profiler.

    The efficiency assessment is skipped if the function is being debugged (i.e., 'debugpy' is present in sys.modules).
    
    Args:
        f (function): The function to be wrapped for efficiency assessment.

    Returns:
        The result of the function call.
    """
    
    @wraps(f)
    def wrap(*args, **kwargs):
        # First call to get the result
        result = f(*args, **kwargs)
        print(f"Result: {result}")

        if sys.modules.get('debugpy'):
            print("The solution is under debug; The assessment will be skipped...")
        else:
            print("No debugging; The assessment will proceed...")
            n = 100000  # Number of iterations to calculate time

            # Use perf_counter for more accurate timing
            start_time = perf_counter()
            for _ in range(n):
                f(*args, **kwargs)
            end_time = perf_counter()
            elapsed_time = end_time - start_time

            # Print the time taken for each call
            print()
            print('-' * 80)
            print(f"Time: {elapsed_time / n:.3e} s per call")
            print('-' * 80)
            print()

            # Perform memory profiling
            print("Memory profile:")
            profile(f, precision=4)(*args, **kwargs)

        return result

    return wrap
