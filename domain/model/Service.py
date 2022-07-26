from domain.enumeration import EServiceType
import numpy as np

from domain.model.Request import Request
from domain.utils.timer import Timer


class Service:
    def __init__(self, service_type: EServiceType, service_time_mean: int, error_rate: float):
        self.service_type = service_type
        self.service_time_mean = service_time_mean
        self.error_rate = error_rate
        self.timer = Timer()
        self.current_request = None

    def gen_service_time(self):
        # Make sure that the minimum service time is 1
        return max(1, int(-np.log(1 - (np.random.uniform(low=0.0, high=1.0))) * self.service_time_mean))

    def is_idle(self):
        return self.timer.is_finished()

    def set_request(self, request: Request):
        self.current_request = request
        service_time = int(self.gen_service_time())
        self.timer.set_period(service_time)

    def delete_request(self):
        r = self.current_request
        self.current_request = None
        return r

    def update(self):
        # Update the timer
        self.timer.tick()
