from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def handle(self, parser, stack, input_tokens, action):
        pass
