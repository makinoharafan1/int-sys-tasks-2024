class LR1Analyzer:
    def __init__(self, action_table, goto_table, rules):
        self.action_table = action_table
        self.goto_table = goto_table
        self.rules = rules

    def shift(self, stack, input_tokens, action):
        next_state = abs(int(action))
        stack.append((next_state, input_tokens.pop(0)))

    def reduce(self, stack, input_tokens, action):
        rule_index = abs(int(action))
        lhs, rhs = self.rules[rule_index]

        for _ in range(len(rhs)):
            stack.pop()

        state = stack[-1][0]
        stack.append((self.goto_table[state][lhs], lhs))

    def accept(self, stack, input_tokens, action):
        print("Accepted!")
        return True

    def error(self, stack, input_tokens, action):
        lookahead = input_tokens[0]
        state = stack[-1][0]
        print("Parsing error!")
        print(f"Unexpected symbol: {lookahead}")
        print(f"Stack at error: {stack}")
        print(f"Remaining input: {input_tokens}")
        print(f"Current state: {state}")
        if lookahead in self.action_table[state]:
            expected_symbols = list(self.action_table[state].keys())
            print(f"Expected symbols at state {state}: {expected_symbols}")
        return False

    def parse(self, input_tokens):
        stack = [(0, '')]
        input_tokens = input_tokens + ["$end"]

        actions = {
            'shift': self.shift,
            'reduce': self.reduce,
            'accept': self.accept,
            'error': self.error
        }

        while True:
            state = stack[-1][0]
            lookahead = input_tokens[0]
        
            if lookahead in self.action_table[state]:
                action = self.action_table[state][lookahead]
                action_type = (
                    'shift' if action > 0 else
                    'reduce' if action < 0 else
                    'accept' if action == 0 else
                    'error'
                )
            else:
                action_type = 'error'

            result = actions[action_type](stack, input_tokens, action)
            if result is not None:
                return result
