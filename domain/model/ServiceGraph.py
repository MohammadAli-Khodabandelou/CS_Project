from domain.enumeration.EServiceType import EServiceType
from domain.model.MicroService import MicroService
from typing import List

from domain.model.Request import Request


class ServiceGraph:

    def __init__(self, service_time_means: dict, instance_numbers: dict, error_rates: dict):
        self.web_gateway = MicroService(EServiceType.WEB_GATEWAY, service_time_means[EServiceType.WEB_GATEWAY], error_rates[EServiceType.WEB_GATEWAY], instance_numbers[EServiceType.WEB_GATEWAY])
        self.mobile_gateway = MicroService(EServiceType.MOBILE_GATEWAY, service_time_means[EServiceType.MOBILE_GATEWAY], error_rates[EServiceType.MOBILE_GATEWAY], instance_numbers[EServiceType.MOBILE_GATEWAY])
        restaurant_management = MicroService(EServiceType.RESTAURANT_MANAGEMENT, service_time_means[EServiceType.RESTAURANT_MANAGEMENT], error_rates[EServiceType.RESTAURANT_MANAGEMENT], instance_numbers[EServiceType.RESTAURANT_MANAGEMENT])
        customer_management = MicroService(EServiceType.CUSTOMER_MANAGEMENT, service_time_means[EServiceType.CUSTOMER_MANAGEMENT], error_rates[EServiceType.CUSTOMER_MANAGEMENT], instance_numbers[EServiceType.CUSTOMER_MANAGEMENT])
        order_management = MicroService(EServiceType.ORDER_MANAGEMENT, service_time_means[EServiceType.ORDER_MANAGEMENT], error_rates[EServiceType.ORDER_MANAGEMENT], instance_numbers[EServiceType.ORDER_MANAGEMENT])
        delivery_communication = MicroService(EServiceType.DELIVERY_COMMUNICATION, service_time_means[EServiceType.DELIVERY_COMMUNICATION], error_rates[EServiceType.DELIVERY_COMMUNICATION], instance_numbers[EServiceType.DELIVERY_COMMUNICATION])
        payment = MicroService(EServiceType.PAYMENT, service_time_means[EServiceType.PAYMENT], error_rates[EServiceType.PAYMENT], instance_numbers[EServiceType.PAYMENT])

        # web gateway
        self.web_gateway.add_next_microservice(restaurant_management)
        self.web_gateway.add_next_microservice(customer_management)
        self.web_gateway.add_next_microservice(order_management)

        # mobile gateway
        self.mobile_gateway.add_next_microservice(order_management)
        self.mobile_gateway.add_next_microservice(customer_management)
        self.mobile_gateway.add_next_microservice(order_management)

        # restaurant management
        restaurant_management.add_next_microservice(delivery_communication)

        # customer management
        customer_management.add_next_microservice(delivery_communication)

        # order management
        order_management.add_next_microservice(payment)
        self.micro_services = [
            self.web_gateway,
            self.mobile_gateway,
            restaurant_management,
            customer_management,
            order_management,
            delivery_communication,
            payment,
        ]

    def update(self):
        for micro_service in self.micro_services:
            micro_service.update()

    def push_request(self, requests: List[Request]):
        for request in requests:
            if Request.dependency_chain_map[request.request_type][0] == EServiceType.WEB_GATEWAY:
                self.web_gateway.push_request(request)
            else:
                self.mobile_gateway.push_request(request)

    def __str__(self):
        log = ''
        for micro_service in self.micro_services:
            log += f'{str(micro_service)}\n'
        return log
