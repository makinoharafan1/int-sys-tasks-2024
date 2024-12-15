import argparse
import ast

from src.elevator import Elevator
from src.elevator_manager import ElevatorManager


parser = argparse.ArgumentParser()

parser.add_argument(
    "--n_floors",
    type=int,
    required=True
)

parser.add_argument(
    "--elevator_floors",
    type=str,
    required=True
)

parser.add_argument(
    "--requests",
    type=str,
    required=True
)

args = parser.parse_args()

n_floors = args.n_floors
elevator_floors = ast.literal_eval(args.elevator_floors)
requests = ast.literal_eval(args.requests)

elevators = []

for i in range(len(elevator_floors)):
    elevators.append(Elevator(id=i, current_floor=elevator_floors[i]))

manager = ElevatorManager(elevators, n_floors=n_floors)

manager.process_all_requests(requests)
