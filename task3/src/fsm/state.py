from typing import Dict, Callable, Tuple


class State:
    def __init__(self, transitions: Dict[int, Tuple[str, Callable]]):
        self.transitions = transitions

    def handle_event(self, event: int) -> Tuple[str, Callable]:
        if event not in self.transitions:
            raise ValueError(f"Unhandled event {event} in state")
        return self.transitions[event]
