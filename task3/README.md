# DFA in elevator system

## State-transition table

| Current state | Event         | Action            | Next state |
|:-------------:|:-------------:|:-----------------:|:----------:|
| Idle          | current < req |                   | Move up    |
| Idle          | current > req |                   | Move down  |
| Idle          | current = req |                   | Open doors |
| Move up       | current < req | Move 1 floor up   | Move up    |
| Move up       | current = req |                   | Open doors |
| Move down     | current > req | Move 1 floor down | Move down  |
| Move down     | current = req |                   | Open doors |
| Open doors    | current = req | Open doors        | Close doors|
| Close doors   | current = req | Close doors       | Idle       |
