from domain.model.service import Service


class MicroService:
    def __init__(self, service_type, service_time_mean: int, error_rate: float, instance_count=1):
        self.input_queues = []
        self.output_queues = []
        self.service_type = service_type
        self.instance_count = instance_count
        self.instances = self.make_instances(service_time_mean, error_rate)

    def make_instances(self, mean, error_rate):
        result = []
        for i in range(self.instance_count):
            result.append(Service(self.service_type, mean, error_rate))
        return result

    def add_input_queue(self, queue):
        self.input_queues.append(queue)

    def add_output_queue(self, queue):
        self.output_queues.append(queue)

    def _idle_service_exist(self):
        pass
