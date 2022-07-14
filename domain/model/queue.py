from domain.model.request import Request
from domain.model.service import Service


class Queue:
    def __init__(self):
        self.queue = []
        self.producers = []
        self.consumers = []

    def add_producer(self, producer: Service):
        self.producers.append(producer)

    def add_consumer(self, consumer: Service):
        self.consumers.append(consumer)

    def add_request(self, request: Request):
        self.queue.append(request)

    def pass_request_to_consumer(self):
        # todo
        pass

