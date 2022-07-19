from domain.enumeration.ERequestType import ERequestType
from domain.enumeration.EServiceType import EServiceType


class Request:
    dependency_chain_map = {
        ERequestType.ORDER_REQUEST_MOBILE: [EServiceType.MOBILE_GATEWAY, EServiceType.ORDER_MANAGEMENT, EServiceType.PAYMENT],
        ERequestType.ORDER_REQUEST_WEB: [EServiceType.WEB_GATEWAY, EServiceType.ORDER_MANAGEMENT, EServiceType.PAYMENT],
        ERequestType.MESSAGE_TO_DELIVERY: [EServiceType.MOBILE_GATEWAY, EServiceType.CUSTOMER_MANAGEMENT, EServiceType.DELIVERY_COMMUNICATION],
        ERequestType.INFORMATION_REQUEST_MOBILE: [EServiceType.MOBILE_GATEWAY, EServiceType.RESTAURANT_MANAGEMENT],
        ERequestType.INFORMATION_REQUEST_WEB: [EServiceType.WEB_GATEWAY, EServiceType.ORDER_MANAGEMENT, EServiceType.PAYMENT],
        ERequestType.DELIVERY_REQUEST: [EServiceType.WEB_GATEWAY, EServiceType.RESTAURANT_MANAGEMENT, EServiceType.DELIVERY_COMMUNICATION],
        ERequestType.ORDER_MONITORING: [EServiceType.MOBILE_GATEWAY, EServiceType.ORDER_MANAGEMENT],
    }

    def __init__(self, request_type: ERequestType, occurrence_prob: float, order: int):
        self.request_type = request_type
        self.occurrence_prob = occurrence_prob
        self.order = order
        self.chain = self.dependency_chain_map.get(self.request_type)

    @property
    def next_service_type(self):
        if len(self.chain) == 0:
            return None
        return self.chain.pop(0)
