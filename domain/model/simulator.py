from domain.enumeration.ERequestType import ERequestType
from domain.enumeration.EServiceType import EServiceType


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
        ERequestType.ORDER_REQUEST_MOBILE: 0.2,
        ERequestType.ORDER_REQUEST_WEB: 0.1,
        ERequestType.MESSAGE_TO_DELIVERY: 0.05,
        ERequestType.INFORMATION_REQUEST_MOBILE: 0.25,
        ERequestType.INFORMATION_REQUEST_WEB: 0.15,
        ERequestType.DELIVERY_REQUEST: 0.2,
        ERequestType.ORDER_MONITORING: 0.05
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
        pass
