#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:36:19 2019

@author: rajat-mehta
"""

from rasa.core.channels.slack import SlackInput
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.utils.endpoints import EndpointConfig

# Replace <model_directory> with your models directory
nlu_interpreter = RasaNLUInterpreter('./models/nlu')
# Load agent with created models and connect to action server endpoint, replace <action_server_endpoint> with your endpoint
agent = Agent.load('./models/', interpreter = nlu_interpreter, action_endpoint = EndpointConfig('http://localhost:5055/webhook'))

input_channel = SlackInput(
    # this is the `bot_user_o_auth_access_token`
    slack_token="",
    slack_channel="@jasper_muj_bot"
    # the name of your channel to which the bot posts (optional)
    )
s = agent.handle_channels([input_channel], 5005)
