class Elevator:
    def __init__(self, id: int, current_floor: int):
        self.id = id
        self.current_floor = current_floor

    def __repr__(self):
        return f"elevator {self.id} (current_floor: {self.current_floor})"
    
    def move_up(self):
        self.current_floor += 1
        print(f"elevator {self.id} moved up to floor {self.current_floor}")

    def move_down(self):
        self.current_floor -= 1
        print(f"elevator {self.id} moved down to floor {self.current_floor}")

    def open_doors(self):
        print(f"elevator {self.id} opened doors on floor {self.current_floor}")

    def close_doors(self):
        print(f"elevator {self.id} closed doors on floor {self.current_floor}")
