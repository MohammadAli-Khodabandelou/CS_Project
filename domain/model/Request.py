from domain.enumeration.ERequestType import ERequestType
from domain.enumeration.EServiceType import EServiceType
from domain.utils.timer import Timer


class Request:
    dependency_chain_map = {
        ERequestType.ORDER_REQUEST_MOBILE: [EServiceType.MOBILE_GATEWAY, EServiceType.ORDER_MANAGEMENT,
                                            EServiceType.PAYMENT],
        ERequestType.ORDER_REQUEST_WEB: [EServiceType.WEB_GATEWAY, EServiceType.ORDER_MANAGEMENT, EServiceType.PAYMENT],
        ERequestType.MESSAGE_TO_DELIVERY: [EServiceType.MOBILE_GATEWAY, EServiceType.CUSTOMER_MANAGEMENT,
                                           EServiceType.DELIVERY_COMMUNICATION],
        ERequestType.INFORMATION_REQUEST_MOBILE: [EServiceType.MOBILE_GATEWAY, EServiceType.RESTAURANT_MANAGEMENT],
        ERequestType.INFORMATION_REQUEST_WEB: [EServiceType.WEB_GATEWAY, EServiceType.ORDER_MANAGEMENT,
                                               EServiceType.PAYMENT],
        ERequestType.DELIVERY_REQUEST: [EServiceType.WEB_GATEWAY, EServiceType.RESTAURANT_MANAGEMENT,
                                        EServiceType.DELIVERY_COMMUNICATION],
        ERequestType.ORDER_MONITORING: [EServiceType.MOBILE_GATEWAY, EServiceType.ORDER_MANAGEMENT],
    }

    def __init__(self, request_type: ERequestType, occurrence_prob: float, order: int, waiting_time: int):
        self.request_type = request_type
        self.occurrence_prob = occurrence_prob
        self.chain = (Request.dependency_chain_map[self.request_type])[:]
        self.order = order
        self.waiting_time = waiting_time
        self.timer = Timer()
        self.timer.set_period(waiting_time)
        self.timeout = False  # We set this field if the request timeouts.
        self.error = False
        self.time_in_queue = 0

    def reset_timer(self):
        # When the request is moved to a new service, this method must be called
        self.timer.set_period(self.waiting_time)

    def set_timeout(self):
        self.timeout = True

    @property
    def next_service_type(self):
        if len(self.chain) > 0:
            self.chain.pop(0)
        if len(self.chain) > 0:
            return self.chain[0]
        return None
