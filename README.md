
# jumping-task

This is a Python3 implementation of the environment used in [Learning Invariances for Policy Generalization](https://openreview.net/pdf?id=BJHRaK1PG). As described in the paper:

We consider an extremely simple video game consisting of a black background, a floor and
two rectangles. The grey rectangle starts on the left of the screen and can be moved with
two actions, ”Right” and ”Jump”. The goal of the game is to reach the right of the screen while
avoiding the white obstacle. There is only one specific distance (measured in number of pixels) to
the obstacle where the agent has to chose the action ”Jump” in order to pass over the obstacle. If
jumping is chosen at any other point, the agent will inevitably crash into the obstacle. A reward of
+1 is granted anytime the agent moves one pixel to the right (even in the air). The episode terminates
if the agent reaches the right of the screen or touches the obstacle.

## Setup

To run the environment, all you need to do is import the class JumpTaskEnv defined in `jumping_task.py` and initialize it. To reproduce the setup from the aforementioned paper, create the environment with:

```
env = JumpTaskEnv(scr_w=60, scr_h=60)
```

Then at the beginning of each training epoch, reset it with:

```
env.reset(floor_height=f_h, obstable_position=o_p)
```

where `f_h` is randomly sampled from [10,20] and `o_p` from [5, 15, 25].
To get the current state of the game, run:

```
state = env.get_state()
```
This will in particular allow you to fill your history.

To perform action `a` (where a=0 corresponds to "Right" and a=1 to "Jump"), run:

```
state, reward, terminal = env.step(a)
```
In that case, `state` corresponds to the state reached after taking `a`, reward is the reward obtained by taking that action, and `terminal` is a boolean stating whether the reached state is terminal.