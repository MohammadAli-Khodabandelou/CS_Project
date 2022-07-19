from domain.model.request import Request
from domain.model.service import Service


class Queue:
    def __init__(self):
        self.high_priority_queue = []
        self.low_priority_queue = []
        self.producers = []
        self.consumers = []

    def add_producer(self, producer: Service):
        self.producers.append(producer)

    def add_consumer(self, consumer: Service):
        self.consumers.append(consumer)

    def add_request(self, request: Request):
        if request.order == 1:
            self.high_priority_queue.append(request)
        else:
            self.low_priority_queue.append(request)

    def pass_request_to_consumer(self):
        # todo
        pass

    def __len__(self):
        return len(self.high_priority_queue) + len(self.low_priority_queue)

    def get_request(self):
        if len(self.high_priority_queue) > 0:
            return self.high_priority_queue.pop(0)
        elif len(self.low_priority_queue) > 0:
            return self.low_priority_queue.pop(0)
        return None
