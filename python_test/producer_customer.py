import threading
import random
import logging
from concurrent.futures import ThreadPoolExecutor
"""
    Simple Producer and Customer model
"""
class Pipeline:
    def __init__(self):
        self.myMessage = None
        self.myCustomerLock = threading.Lock()
        self.myProducerLock = threading.Lock()
        self.myCustomerLock.acquire()

    def set_message(self, aMessage, aName):
        logging.debug("%s:about to acquire setlock", aName)
        self.myProducerLock.acquire()
        logging.debug("%s:have setlock", aName)
        self.myMessage = aMessage
        logging.debug("%s:about to release getlock", aName)
        self.myCustomerLock.release()
        logging.debug("%s:getlock released", aName)

    def get_message(self, aName):
        logging.debug("%s:about to acquire getlock", aName)
        self.myCustomerLock.acquire()
        logging.debug("%s:have getlock", aName)
        message = self.myMessage
        logging.debug("%s:about to release setlock", aName)
        self.myProducerLock.release()
        logging.debug("%s:setlock released", aName)
        return message


SENTINEL = object()

def producer(aPipeline):
    for _ in range(10):
        message = random.randint(1, 100)
        logging.info(f"set message value {message}")
        aPipeline.set_message(message, "Producer")
        
    aPipeline.set_message(SENTINEL, "Producer")

def customer(aPipeline):
    for _ in range(10):
        message = aPipeline.get_message("Customer")
        if message is not SENTINEL:
            logging.info(f"get message value {message}")


"""
    Use queue create producer and customer

"""

if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")
    # logging.getLogger().setLevel(logging.INFO)

    pipeLine = Pipeline()

    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeLine)
        executor.submit(customer, pipeLine)
        

