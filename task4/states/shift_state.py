from states.state import ParserState


class ShiftState(ParserState):
    def handle(self, parser, stack, input_tokens, action):
        next_state = abs(int(action))
        stack.append((next_state, input_tokens.pop(0)))
