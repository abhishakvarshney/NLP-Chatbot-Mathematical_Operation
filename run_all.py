from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging

from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from core.bot_server_channel import BotServerInputChannel

logger = logging.getLogger(__name__)


# Creating the Interpreter and Agent
def load_agent():
    action_endpoint = EndpointConfig(url="http://localhost:8000/webhook")
    interpreter = RasaNLUInterpreter("./models/default/nlu")

    agent = Agent.load(
        "./models/dialogue",
        interpreter=interpreter,
        action_endpoint=action_endpoint,
    )
    return agent


# Creating the server
def main_server():
    agent = load_agent()
    print(agent)
    web_channel = BotServerInputChannel(agent)
    agent.handle_channels([web_channel], http_port=8001, serve_forever=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="debug log for development and production"
    )
    parser.add_argument("-d", "--debug", help="Set the logging level")
    args = parser.parse_args()
    if args == "debug":
        logging.DEBUG = True
    else:
        logging.DEBUG = False
    main_server()
