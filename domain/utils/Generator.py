import random

from domain.enumeration.ERequestType import ERequestType
from domain.model.Request import Request
from typing import List


class Generator:
    def __init__(self, request_per_second: int, occurrence_probs: dict, orders: dict, waiting_times: dict):
        self.request_per_second = request_per_second
        self.occurrence_proba = occurrence_probs
        self.orders = orders
        self.waiting_times = waiting_times
        self.requests: List[Request] = []
        for request_type in ERequestType:
            self.requests.append(
                Request(request_type, self.occurrence_proba[request_type], self.orders[request_type], self.waiting_times[request_type]))

    def generate_request_samples(self):
        return random.choices(list(self.requests), weights=[request.occurrence_prob for request in self.requests], k=self.request_per_second)
