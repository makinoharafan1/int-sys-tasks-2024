from typing import Dict

from src.fsm.state import State 


class StateMachine:
    def __init__(self, elevator):
        self.elevator = elevator
        self.transition_table: Dict[str, State] = self._create_transition_table()
        self.current_state = "IDLE"

    def _create_transition_table(self) -> Dict[str, State]:
        return {
            "IDLE": State({
                1: ("MOVE_UP", lambda: None),
               -1: ("MOVE_DOWN", lambda: None),
                0: ("OPEN_DOORS", lambda: None),
            }),
            "MOVE_UP": State({
                1: ("MOVE_UP", self.elevator.move_up),
                0: ("OPEN_DOORS", lambda: None),
            }),
            "MOVE_DOWN": State({
               -1: ("MOVE_DOWN", self.elevator.move_down),
                0: ("OPEN_DOORS",lambda: None),
            }),
            "OPEN_DOORS": State({
                0: ("CLOSE_DOORS", self.elevator.open_doors),
            }),
            "CLOSE_DOORS": State({
                0: ("IDLE", self.elevator.close_doors),
            }),
        }

    def transition(self, event: int):
        state_obj = self.transition_table[self.current_state]
        self.current_state, action = state_obj.handle_event(event)
        action()
