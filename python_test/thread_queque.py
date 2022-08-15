import logging
import threading
import random
import time
import queue
from concurrent.futures import ThreadPoolExecutor

"""
    使用threading.Event模块
        - event允许线程发出信号, 当其他线程正在等待开始时
        * producer_customer.py中使用简单的全局变量作为结束和开始的信号
"""
class Pipeline(queue.Queue):
    def __init__(self):
        super().__init__(maxsize=10)

    def set_message(self, aMessage, aName):
        logging.debug(f"ready to put to {aMessage} the queue")
        self.put(aMessage)
        logging.debug(f"puted {aMessage} to queue")

    def get_message(self, aName):
        logging.debug(f"ready to get value from queue")
        value = self.get()
        logging.debug(f"get value {value} from queue")
        return value


def producer(aPipeline, aEvent):
    while not aEvent.is_set():
        message = random.randint(1, 100)
        logging.info(f"set message value {message}")
        aPipeline.set_message(message, "Producer")
        
    logging.info("Producer received EXIT event. Exiting")

def customer(aPipeline, aEvent):
    while not aEvent.is_set() or not aPipeline.empty():
        message = aPipeline.get_message("Customer")
        logging.info(
            "Consumer storing message: %s  (queue size=%s)",
            message,
            aPipeline.qsize(),
        )

    logging.info("Consumer received EXIT event. Exiting")

if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")

    pipline = Pipeline()
    event = threading.Event()

    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipline, event)
        executor.submit(customer, pipline, event)
    
        time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()
