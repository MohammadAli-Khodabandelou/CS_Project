from domain.model.queue import Queue
from domain.model.request import Request
from domain.model.service import Service


class MicroService:
    def __init__(self, service_type,
                 service_time_mean: int,
                 error_rate: float,
                 instance_count=1):
        self.queue = Queue()
        self.next_microservices = []
        self.service_type = service_type
        self.instance_count = instance_count
        self.instances = self._make_instances(service_time_mean, error_rate)

    def _make_instances(self, mean, error_rate):
        result = []
        for i in range(self.instance_count):
            result.append(Service(self.service_type, mean, error_rate))
        return result

    def _get_idle_instance(self):
        # Returns an idle instance if exists, otherwise None
        for s in self.instances:
            if s.is_idle():
                return s
        return None

    def _process_queue(self):
        # Checks if there is an idle instance, then pass a request to the service
        idle_service = self._get_idle_instance()
        if idle_service is not None:
            request = self.queue.get_request()
            idle_service.set_request(request)

    def _update_instances(self):
        # Checks each instance to see if it becomes idle. Passes the request to the next if necessary.
        for s in self.instances:
            s.update()
            if s.timer.is_finished():
                request = s.delete_request()
                if request is not None:
                    self._pass_request_to_next(request)

    def _pass_request_to_next(self, request):
        next_service_type = request.next_service_type
        if next_service_type is None:
            # The request has reached to the end of the pipeline
            del request
            return
        for microservice in self.next_microservices:
            if microservice.service_type.value == next_service_type.value:
                microservice.push_request(request)
                break

    def add_next_microservice(self, microservice):
        self.next_microservices.append(microservice)

    def push_request(self, request: Request):
        # Push a new request to the end of the queue
        self.queue.add_request(request)
        self._process_queue()  # The added request must be processed if there is an idle instance

    def update(self):
        # This method do all necessary functionalities and implements the main logic of the class
        self._update_instances()
        self._process_queue()

    def __str__(self):
        result = ""
        result += f"Request in queue = {len(self.queue)}\n"
        for i in range(len(self.instances)):
            s = self.instances[i]
            result += f"[Instance {i + 1}]: Is_Idle: {s.is_idle()}, Remaining time = {s.timer.period}\n"
        return result
