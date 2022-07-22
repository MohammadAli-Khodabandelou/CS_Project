from domain.model.request import Request
from domain.model.service import Service


class Queue:
    def __init__(self):
        self.high_priority_queue = []
        self.low_priority_queue = []
        self.consumers = []

    def add_request(self, request: Request):
        request.reset_timer()  # Reset the timeout timer of the new request.
        if request.order == 1:
            self.high_priority_queue.append(request)
        else:
            self.low_priority_queue.append(request)

    def __len__(self):
        return len(self.high_priority_queue) + len(self.low_priority_queue)

    def get_request(self):
        if len(self.high_priority_queue) > 0:
            return self.high_priority_queue.pop(0)
        elif len(self.low_priority_queue) > 0:
            return self.low_priority_queue.pop(0)
        return None

    def update_queue(self):
        # This method checks if each request in the queue is in timeout status. If yes, removes from queue.
        for i in range(len(self.high_priority_queue)):
            r = self.high_priority_queue[i]
            r.timer.tick()
            if r.timer.is_finished():
                self.high_priority_queue.pop(i)
                # TODO: Change the status of the request to TIMEOUT ?
        for i in range(len(self.low_priority_queue)):
            r = self.high_priority_queue[i]
            r.timer.tick()
            if r.timer.is_finished():
                self.high_priority_queue.pop(i)
                # TODO: Change the status of the request to TIMEOUT ?
