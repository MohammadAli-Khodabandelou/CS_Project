from domain.enumeration import EServiceType
import numpy as np


class Service:
    def __init__(self, service_type: EServiceType, service_time_mean: int, error_rate: float):
        self.service_type = service_type
        self.service_time_mean = service_time_mean
        self.error_rate = error_rate

    def gen_service_time_teller1(self):
        return -np.log(1 - (np.random.uniform(low=0.0, high=1.0))) * self.service_time_mean

