#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Gym dependencies
import gym
from gym import spaces

# Vectors
import numpy as np

class AerotropolisEnv(gym.Env):

  def __init__(self):
    self.state = None
    self.action_space = spaces.Discrete(10)
    self.observation_space = spaces.Box(low=0,
               high=255,
               shape=10,
               dtype=np.uint8)


  def step(self, action):
    """
    The agent takes a step in the environment.
    Parameters
    ----------
    action : int
    Returns
    -------
    ob, reward, episode_over, info : tuple
        ob (object) :
            an environment-specific object representing your observation of
            the environment.
        reward (float) :
            amount of reward achieved by the previous action. The scale
            varies between environments, but the goal is always to increase
            your total reward.
        episode_over (bool) :
            whether it's time to reset the environment again. Most (but not
            all) tasks are divided up into well-defined episodes, and done
            being True indicates the episode has terminated. (For example,
            perhaps the pole tipped too far, or you lost your last life.)
        info (dict) :
             diagnostic information useful for debugging. It can sometimes
             be useful for learning (for example, it might contain the raw
             probabilities behind the environment's last state change).
             However, official evaluations of your agent are not allowed to
             use this for learning.
    """

    return _, 0, False, {}

  def reset(self):
    return self.state