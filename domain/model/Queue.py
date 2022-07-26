from domain.model.Request import Request


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
        high_priority_to_delete = []
        low_priority_to_delete = []

        for i in range(len(self.high_priority_queue)):
            r = self.high_priority_queue[i]
            r.timer.tick()
            if r.timer.is_finished():
                high_priority_to_delete.append(i)
                r.set_timeout()
        for i in range(len(self.low_priority_queue)):
            r = self.low_priority_queue[i]
            r.timer.tick()
            if r.timer.is_finished():
                low_priority_to_delete.append(i)
                r.set_timeout()

        self.high_priority_queue = [self.high_priority_queue[i]
                                    for i in range(len(self.high_priority_queue))
                                    if i not in high_priority_to_delete]
        self.low_priority_queue = [self.low_priority_queue[i]
                                   for i in range(len(self.low_priority_queue))
                                   if i not in low_priority_to_delete]

