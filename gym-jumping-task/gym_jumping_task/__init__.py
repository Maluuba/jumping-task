from gym.envs.registration import register

register(
    id='jumping-task-v0',
    entry_point='gym_jumping_task.envs:JumpTaskEnv',
)