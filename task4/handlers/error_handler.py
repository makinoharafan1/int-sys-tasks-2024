from handlers.handler import Handler


class ErrorHandler(Handler):
    def handle(self, parser, stack, input_tokens, action):
        lookahead = input_tokens[0]
        state = stack[-1][0]
        print("Parsing error!")
        print(f"Unexpected symbol: {lookahead}")
        print(f"Stack at error: {stack}")
        print(f"Remaining input: {input_tokens}")
        print(f"Current state: {state}")
        
        try:
            expected_symbols = list(parser.action_table[state].keys())
            print(f"Expected symbols at state {state}: {expected_symbols}")
        except KeyError:
            print(f"No valid actions defined for state {state}")
        
        parser.done = True
