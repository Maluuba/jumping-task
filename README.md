
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

To run the environment, you will need the following dependencies:
```
pip install argparse numpy pygame
```

## Play

To play the game yourself, simply run:
```
ipython jumping_task.py
```
and use the arrows to control the agent. Check below for more game options (different obstacle locations, two obstacles...).
Press the `e` key to exit the game.

## Train

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

To perform action `a` (where `a=0` corresponds to `Right` and `a=1` to `Jump`), run:

```
state, reward, terminal = env.step(a)
```
The method returns state, reward, terminal, where `state` is the state reached after taking `a`, reward the reward obtained by taking that action, and `terminal` a boolean stating whether the reached state is terminal.

More implementation details can be found in the code itself.

## Advanced

To customize the environment, you can pass the following arguments to the constructor:

```
Args:
  scr_w: screen width, by default 84 pixels
  scr_h: screen height, by default 84 pixels
  floor_height: the height of the floor in pixels, by default 20 pixels
  agent_w: agent width, by default 5 pixels
  agent_h: agent height, by default 10 pixels
  agent_init_pos: initial x position of the agent (on the floor), defaults to the left of the screen
  agent_speed: agent lateral speed, measured in pixels per time step, by default 1 pixel
  obstacle_position: initial x position of the obstacle (on the floor), by default 0 pixels, which is the leftmost one
  obstacle_size: width and height of the obstacle, by default (9, 10)
  rendering: display the game screen, by default False
  zoom: zoom applied to the screen when rendering, by default 8
  slow_motion: if True, sleeps for 0.1 seconds at each time step.
            Allows to watch the game at "human" speed when played by the agent, by default False
  with_left_action: if True, the left action is allowed, by default False
  max_number_of_steps: the maximum number of steps for an episode, by default 600.
  two_obstacles: puts two obstacles on the floor at a given location.
                  The ultimate generalization test, by default False
  finish_jump: perform a full jump when the jump action is selected.
                Otherwise an action needs to be selected as usual, by default False
```

## Citation

If you find this code useful please cite us in your work:

```
@inproceedings{Tachet2018,
  title={Learning Invariances for Policy Generalization},
  author={Remi Tachet des Combes and Philip Bachman and Harm van Seijen},
  booktitle={ICLR Workshop Track},
  year={2018}
}
```
