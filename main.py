from domain.enumeration.ERequestType import ERequestType
from domain.model.Request import Request
from domain.model.Simulator import Simulator
from domain.utils.Generator import Generator

if __name__ == '__main__':
    simulator = Simulator()
    simulator.simulate()
    # generator = Generator(Simulator.request_rate, Simulator.request_probs, Simulator.request_orders, Simulator.request_waiting_times)
    # samples = generator.generate_request_samples()
    # print(samples)
