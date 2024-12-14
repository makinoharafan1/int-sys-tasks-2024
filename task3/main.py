import argparse
import ast

from src.elevator import Elevator


parser = argparse.ArgumentParser()

parser.add_argument(
    "--n_floor",
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

n_floor, elevator_floors, requests = args.n_floor, ast.literal_eval(args.elevator_floors), ast.literal_eval(args.requests)

elevators = []

for i in range(len(elevator_floors)):
    elevators.append(Elevator(id=i, current_floor=elevator_floors[i]))

for elevator in elevators:
    print(elevator._current_floor)
