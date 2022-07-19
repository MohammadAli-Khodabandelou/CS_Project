from domain.enumeration import EServiceType
import numpy as np

from domain.model.queue import Queue


class Service:
    def __init__(self, service_type: EServiceType, service_time_mean: int, error_rate: float, consumer: Queue):
        self.service_type = service_type
        self.service_time_mean = service_time_mean
        self.error_rate = error_rate
        self.consumer = consumer
        self.request = None

    def gen_service_time(self):
        return -np.log(1 - (np.random.uniform(low=0.0, high=1.0))) * self.service_time_mean
