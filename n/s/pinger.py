
import logging

from hisc.dragon.eb.event_client import EventClient
from hisc.dragon.eb.events.ping import Ping
from hisc.dragon.rabbitmq.receiver import Receiver
from hisc.dragon.rabbitmq.sender import Sender


class Pinger(EventClient):
    def __init__(self):
        super(Pinger, self).__init__(Sender(EventClient.EXCHANGE), Receiver(EventClient.EXCHANGE))
        logging.basicConfig(filename='pinger.log', level=logging.DEBUG)

    def send_ping(self):
        logging.info('pinger: sending...')
        self.send(Ping())

if __name__ == '__main__':
    Pinger().send_ping()