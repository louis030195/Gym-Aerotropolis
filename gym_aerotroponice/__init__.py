import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Aerotropolis-v0',
    entry_point='gym_aerotropolis.envs:AerotropolisEnv',
)
