import numpy as np


class Analyzer:
    def __init__(self, simulator):
        self.requests = simulator.all_requests
        self.service_graph = simulator.service_graph

    def analyze_mean_queue_length(self):
        for ms in self.service_graph.micro_services:
            print(f'{ms.service_type}:\n'
                  f'Instance Count = {ms.instance_count}\n'
                  f'Mean queue length = {np.mean(ms.queue_lengths)}\n')
            print('=' * 45)

    def analyze_mean_waiting_time(self):
        pass

    def analyze_utilization(self):
        pass

    def analyze_timed_out_requests(self):
        pass
