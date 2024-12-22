from states.state import ParserState


class AcceptState(ParserState):
    def handle(self, parser, stack, input_tokens, action):
        print("Accepted!")
        parser.done = True
