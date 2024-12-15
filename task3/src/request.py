class Request:
    def __init__(self, calling_floor: int, destination_floor: int, n_floors: int):
        if not (1 <= calling_floor <= n_floors) or not (1 <= destination_floor <= n_floors):
            raise ValueError(
                f"Invalid request: floors must be between 1 and {n_floors}. Got: "
                f"calling_floor={calling_floor}, destination_floor={destination_floor}"
            )
        self.calling_floor = calling_floor
        self.destination_floor = destination_floor

    def __repr__(self):
        return f"request from {self.calling_floor} to {self.destination_floor}"
