import numpy as np
import matplotlib.pyplot as plt


class Analyzer:
    def __init__(self, simulator):
        self.requests = simulator.all_requests
        self.service_graph = simulator.service_graph
        self.simulation_time = simulator.simulation_time

    def analyze_mean_queue_length(self):
        for ms in self.service_graph.micro_services:
            print(f'{ms.service_type}:\n'
                  f'Instance Count = {ms.instance_count}\n'
                  f'Mean queue length = {np.mean(ms.queue_lengths)}\n')
            print('=' * 45)

    def analyze_mean_waiting_time(self, plot=False):
        mean_waiting_time = 0
        for r in self.requests:
            mean_waiting_time += r.time_in_queue
        print(f'MEAN WAITING TIME = {mean_waiting_time / len(self.requests)}')
        if plot:
            y = [r.time_in_queue for r in self.requests]
            plt.hist(y, bins=7)
            plt.xlabel('Request No.')
            plt.ylabel('Waiting time')
            plt.show()

    def analyze_utilization(self):
        for ms in self.service_graph.micro_services:
            print(f'{ms.service_type}:')
            for i in range(len(ms.instances)):
                print(f'\t[INSTANCE {i + 1}] utilization = {ms.instances[i].busy_time / self.simulation_time}')

    def analyze_timed_out_requests(self):
        timed_out_count = len(list(filter(lambda r: r.timeout is True, self.requests)))
        print(f'Timeout requests percentage = {timed_out_count / len(self.requests)}')
