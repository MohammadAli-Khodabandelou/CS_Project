from domain.enumeration.ERequestType import ERequestType
from domain.model.request import Request

if __name__ == '__main__':
    print(Request.dependency_chain_map[ERequestType.INFORMATION_REQUEST_MOBILE])

