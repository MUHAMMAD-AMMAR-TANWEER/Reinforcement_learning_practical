import os
import gym
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.vec_env import DummyVecEnv

environment_name = "CarRacing-v0"
env = gym.make(environment_name)

env.reset()
