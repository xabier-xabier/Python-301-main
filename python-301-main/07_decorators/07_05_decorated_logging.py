# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.

import time


def timer(func):
    def timer_wrapper(*args):
        start_time = time.perf_counter()
        result = func(*args)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args}  Took {total_time:.4f} seconds')
        return result
    return timer_wrapper


@timer
def eq_calculation(num):
    total = sum((x for x in range(0, num**2+4*num)))
    return total

if __name__ == '__main__':
    eq_calculation(10)
    eq_calculation(100)
    eq_calculation(1000)
    eq_calculation(5000)
    eq_calculation(10000)