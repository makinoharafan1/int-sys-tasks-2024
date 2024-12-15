from typing import List, Tuple

from src.elevator import Elevator
from src.request import Request
from src.fsm.state_machine import StateMachine
from utils.cmp import cmp


class ElevatorManager:
    def __init__(self, elevators: List[Elevator], n_floors: int):
        self.elevators = elevators
        self.state_machines = {e.id: StateMachine(e) for e in elevators}
        self.n_floors = n_floors

    def process_all_requests(self, requests: List[Tuple[int, int]]):
        for calling_floor, destination_floor in requests:
            try:
                request = Request(calling_floor, destination_floor, self.n_floors)
                self.assign_request(request)
            except ValueError as e:
                print(e)

    def assign_request(self, request: Request):
        nearest_elevator = min(
            self.elevators,
            key=lambda e: abs(e.current_floor - request.calling_floor)
        )

        print(f"Assigned {request} to {nearest_elevator}")
        self.process_request(nearest_elevator.id, request.calling_floor)
        self.process_request(nearest_elevator.id, request.destination_floor)

    def process_request(self, elevator_id: int, request: int):
        elevator = self.elevators[elevator_id]
        state_machine = self.state_machines[elevator_id]

        event = cmp(elevator.current_floor, request)
        state_machine.transition(event)
        while state_machine.current_state != "IDLE":
            event = cmp(elevator.current_floor, request)
            state_machine.transition(event)
