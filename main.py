from domain.enumeration.ERequestType import ERequestType
from domain.model.Request import Request
from domain.model.Simulator import Simulator
from domain.utils.Analyzer import Analyzer
from domain.utils.Generator import Generator

if __name__ == '__main__':
    simulator = Simulator()
    simulator.simulate()
    analyzer = Analyzer(simulator)
    analyzer.analyze_mean_queue_length()
    analyzer.analyze_mean_waiting_time()
    analyzer.analyze_utilization()
    analyzer.analyze_timed_out_requests()
    # generator = Generator(Simulator.request_rate, Simulator.request_probs, Simulator.request_orders, Simulator.request_waiting_times)
    # samples = generator.generate_request_samples()
    # print(samples)
