from abc import ABC, abstractmethod


class SupportHandler(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass

    @abstractmethod
    def set_next_handler(self, next_handler):
        pass


class AuthHandler(SupportHandler):
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, next_handler):
        self.next_handler = next_handler

    def handle_request(self, request):
        if not request.get("auth"):
            return False
        print("Auth passed ")
        if self.next_handler:
            return self.next_handler.handle_request(request)
        return True


class RateHandler(SupportHandler):
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, next_handler):
        self.next_handler = next_handler

    def handle_request(self, request):
        if request.get("rate", 0) > 100:
            return False
        print("Rate check passed ")
        if self.next_handler:
            return self.next_handler.handle_request(request)
        return True


class ContentHandler(SupportHandler):
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, next_handler):
        self.next_handler = next_handler

    def handle_request(self, request):
        if "virus" in request.get("content", ""):
            return False
        print("Content validation passed ")
        if self.next_handler:
            return self.next_handler.handle_request(request)
        return True
