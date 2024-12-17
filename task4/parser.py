class LR1Parser:
    def __init__(self, action_table, goto_table, rules):
        self.action_table = action_table
        self.goto_table = goto_table
        self.rules = rules

    def parse(self, input_tokens):
        stack = [(0, '')]
        input_tokens = input_tokens + ["$end"]

        while True:
            state = stack[-1][0]
            lookahead = input_tokens[0]

            if lookahead in self.action_table[state]:
                action = self.action_table[state][lookahead]

                if action > 0:  # Shift
                    next_state = abs(int(action))
                    stack.append((next_state, lookahead))
                    input_tokens.pop(0)

                elif action < 0:  # Reduce
                    rule_index = abs(int(action))
                    lhs, rhs = self.rules[rule_index]

                    for _ in range(len(rhs)):
                        stack.pop()

                    state = stack[-1][0]
                    stack.append((self.goto_table[state][lhs], lhs))

                elif action == 0:  # Accept
                    print("Accepted!")
                    return True

            else:
                print("Parsing error!")
                print(f"Unexpected symbol: {lookahead}")
                print(f"Stack at error: {stack}")
                print(f"Remaining input: {input_tokens}")
                print(f"Current state: {state}")
                if lookahead in self.action_table[state]:
                    expected_symbols = list(self.action_table[state].keys())
                    print(f"Expected symbols at state {state}: {expected_symbols}")
                return False
