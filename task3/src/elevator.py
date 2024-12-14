class Elevator:
    def __init__(self, id: int, current_floor: int):
        self._id = id
        self._current_floor = current_floor
        self._n_executed_commands = 0
        self._executed_commands = []

    @property
    def current_floor(self):
        return self._current_floor

    def idle(self):
        self._executed_commands.append()
    
    # def move_up(self):

    # def move_down(self):

    # def open_doors(self):

    # def close_doors(self):

