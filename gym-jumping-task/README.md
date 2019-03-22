# jumping-task

For the full documentation, see the README in the parent folder.

## Setup as a gym environment

To install and use the jumping task as a gym environment, run the following command from the parent folder:
```
pip install -e gym-jumping-task
```

You can then create an environment with:
```
import gym
import gym_jumping_task
env = gym.make('jumping-task-v0')
```

## Run experiments

Calling the reset function will reset the game with a random position from the 6 positions used in the original paper.
If you wish to reset the game with an other position, call e.g.:
```
env._reset(obstacle_position=30, floor_height=10)
```

In order to test generalization like in the paper, run your agent the following way:
```
for obstacle_position in range(env.min_x_position, max_x_position):
  for floor_height in range(env.min_y_position, max_y_position):
    env._reset(obstacle_position=obstacle_position, floor_height=floor_height)
    # TEST YOUR AGENT ON THAT TASK
```