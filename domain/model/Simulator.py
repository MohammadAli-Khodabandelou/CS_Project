from domain.enumeration.ERequestType import ERequestType
from domain.enumeration.EServiceType import EServiceType
from domain.model.ServiceGraph import ServiceGraph
from domain.utils.Generator import Generator


class Simulator:
    service_time_means = {
        EServiceType.RESTAURANT_MANAGEMENT: 8,
        EServiceType.CUSTOMER_MANAGEMENT: 5,
        EServiceType.ORDER_MANAGEMENT: 6,
        EServiceType.DELIVERY_COMMUNICATION: 9,
        EServiceType.PAYMENT: 12,
        EServiceType.WEB_GATEWAY: 2,
        EServiceType.MOBILE_GATEWAY: 3
    }

    error_rates = {
        EServiceType.RESTAURANT_MANAGEMENT: 0.02,
        EServiceType.CUSTOMER_MANAGEMENT: 0.02,
        EServiceType.ORDER_MANAGEMENT: 0.03,
        EServiceType.DELIVERY_COMMUNICATION: 0.1,
        EServiceType.PAYMENT: 0.2,
        EServiceType.WEB_GATEWAY: 0.01,
        EServiceType.MOBILE_GATEWAY: 0.01
    }

    instance_numbers = {
        EServiceType.RESTAURANT_MANAGEMENT: 1,
        EServiceType.CUSTOMER_MANAGEMENT: 1,
        EServiceType.ORDER_MANAGEMENT: 1,
        EServiceType.DELIVERY_COMMUNICATION: 2,
        EServiceType.PAYMENT: 5,
        EServiceType.WEB_GATEWAY: 3,
        EServiceType.MOBILE_GATEWAY: 2
    }

    request_probs = {
        ERequestType.ORDER_REQUEST_MOBILE: 20,
        ERequestType.ORDER_REQUEST_WEB: 10,
        ERequestType.MESSAGE_TO_DELIVERY: 5,
        ERequestType.INFORMATION_REQUEST_MOBILE: 25,
        ERequestType.INFORMATION_REQUEST_WEB: 15,
        ERequestType.DELIVERY_REQUEST: 20,
        ERequestType.ORDER_MONITORING: 5
    }

    request_orders = {
        ERequestType.ORDER_REQUEST_MOBILE: 1,
        ERequestType.ORDER_REQUEST_WEB: 1,
        ERequestType.MESSAGE_TO_DELIVERY: 2,
        ERequestType.INFORMATION_REQUEST_MOBILE: 2,
        ERequestType.INFORMATION_REQUEST_WEB: 2,
        ERequestType.DELIVERY_REQUEST: 1,
        ERequestType.ORDER_MONITORING: 2
    }

    request_waiting_times = {
        ERequestType.ORDER_REQUEST_MOBILE: 25,
        ERequestType.ORDER_REQUEST_WEB: 30,
        ERequestType.MESSAGE_TO_DELIVERY: 25,
        ERequestType.INFORMATION_REQUEST_MOBILE: 30,
        ERequestType.INFORMATION_REQUEST_WEB: 30,
        ERequestType.DELIVERY_REQUEST: 40,
        ERequestType.ORDER_MONITORING: 20
    }

    request_rate = 30
    simulation_time = 28800

    def __init__(self):
        self.generator = Generator(Simulator.request_rate, Simulator.request_probs, Simulator.request_orders, Simulator.request_waiting_times)
        self.service_graph = ServiceGraph(Simulator.service_time_means, Simulator.instance_numbers, Simulator.error_rates)
        self.all_requests = []

    def simulate(self):
        for time in range(Simulator.simulation_time + 1):
            samples = self.generator.generate_request_samples()
            self.all_requests.__add__(samples)
            self.service_graph.push_request(samples)
            self.service_graph.update()
            if time % 1000 == 0:
                print(f'time: {time}\n{self.service_graph}\n\n')
