import random

from domain.enumeration.ERequestType import ERequestType
from domain.enumeration.EServiceType import EServiceType
from domain.model.MicroService import MicroService
from domain.model.Request import Request

microservice1 = MicroService(EServiceType.MOBILE_GATEWAY, 4, 0, 2)
microservice2 = MicroService(EServiceType.ORDER_MANAGEMENT, 7, 0, 2)
microservice1.add_next_microservice(microservice2)
time_intervals = [1, 3, 5, 6, 9, 11, 12, 14, 18, 21, 25, 27, 30]
time = 0
while time < 50:
    if len(time_intervals) > 0 and time == time_intervals[0]:
        time_intervals = time_intervals[1:]
        r = Request(ERequestType.ORDER_MONITORING, 0.2, random.randint(1, 3), random.randint(2, 4))
        microservice1.push_request(r)
    print(time)
    microservice1.update()
    microservice2.update()
    time += 1
    print(microservice1)
    print(microservice2)
    print('=' * 30)
