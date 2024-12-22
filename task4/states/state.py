from abc import ABC, abstractmethod


class ParserState(ABC):
    @abstractmethod
    def handle(self, parser, stack, input_tokens, action):
        pass
