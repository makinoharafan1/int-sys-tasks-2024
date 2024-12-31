from handlers.shift_handler import ShiftHandler
from handlers.reduce_handler import ReduceHandler
from handlers.accept_handler import AcceptHandler
from handlers.error_handler import ErrorHandler


class LR1Analyzer:
    def __init__(self, action_table, goto_table, rules):
        self.action_table = action_table
        self.goto_table = goto_table
        self.rules = rules

        self.action_dispatch = {
             1: ShiftHandler(),
            -1: ReduceHandler(),
             0: AcceptHandler(),
             None: ErrorHandler()
        }

    def get_state_handler(self, action):
        sign = lambda x: x and (1, -1)[x < 0]

        try:
            action = self.action_dispatch[sign(action)]
        except:
            action = None

        return action

    def parse(self, input_tokens):
        self.done = False
        stack = [(0, '')]
        input_tokens = input_tokens + ["$end"]

        while not self.done:
            state = stack[-1][0]
            lookahead = input_tokens[0]

            action = self.action_table.get(state, {}).get(lookahead, None)
            state_handler = self.get_state_handler(action)

            state_handler.handle(self, stack, input_tokens, action)
