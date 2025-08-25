import threading
import os
import inspect
import concurrent.futures

# for testing purpose, we will use logging as output 
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='./logs/output.log',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    encoding='utf-8',
                    level=logging.DEBUG)

def worker(id : int = 0):
    logging.info("Worker thread running")
    filename = f"./data/worker_{(id%2)+1}.txt"
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            logger.info(f"Worker {id}: File {filename} found: {[line.strip() for line in lines]}")
    except:
        logger.warning(f"Worker {id}: File {filename} not found")

def task(internal_id):
    logging.info("Task \"{}\" assigned to thread: {}".format(inspect.currentframe().f_code.co_name, threading.current_thread().name))
    logging.info("ID of process running task {}: {}".format(internal_id, os.getpid()))

if __name__ == "__main__":
    logging.info("Using threading library: ")
    logging.info("ID of process running main program: {}".format(os.getpid()))
    logging.info("Main thread name: {}".format(threading.current_thread().name))

    threads = []
    for _ in range(1, 10+1):
        thread = threading.Thread(target=task, name=f't{_}', args=(_,))
        threads.append(thread)
        thread.start()

    for thread in threads:  # iterates over the threads
        thread.join()  

    logging.info('---' * 10)
    logging.info("For a threading pool:")
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=20)
    for _ in range(10):
        pool.submit(worker, (_+1))
    pool.shutdown(wait=True)

    logging.info("Main thread continuing to run")
    logging.info('---' * 10)