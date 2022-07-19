from domain.model.request import Request
from domain.model.service import Service


class Queue:
    def __init__(self):
        # todo: using two queues to handle priority
        self.queue = []
        self.consumers = []

    def add_consumer(self, consumer: Service):
        self.consumers.append(consumer)

    def add_request(self, request: Request):
        self.queue.append(request)
