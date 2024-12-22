from handlers.handler import Handler


class ReduceHandler(Handler):
    def handle(self, parser, stack, input_tokens, action):
        rule_index = abs(int(action))
        lhs, rhs = parser.rules[rule_index]
        for _ in range(len(rhs)):
            stack.pop()
        state = stack[-1][0]
        stack.append((parser.goto_table[state][lhs], lhs))
