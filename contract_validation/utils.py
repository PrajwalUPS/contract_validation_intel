import logging
from time import time

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_and_profile(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        logging.info(f"Starting '{func.__name__}' function")
        result = func(*args, **kwargs)
        end_time = time()
        logging.info(f"Finished '{func.__name__}' function in {end_time - start_time:.2f} seconds")
        return result
    return wrapper
