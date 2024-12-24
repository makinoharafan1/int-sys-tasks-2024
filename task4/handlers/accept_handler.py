from handlers.handler import Handler


class AcceptHandler(Handler):
    def handle(self, parser, stack, input_tokens, action):
        print("Accepted!")
        parser.done = True
