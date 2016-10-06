import logging
import time
from datetime import datetime
from logging import FileHandler, basicConfig, DEBUG

from hisc.dragon.eb.event_client import EventClient
from hisc.dragon.eb.events.pong import Pong
from hisc.dragon.eb.filter.event_filter import EventFilter
from hisc.dragon.rabbitmq.receiver import Receiver
from hisc.dragon.rabbitmq.sender import Sender
from service import Service


class Ponger(EventClient):
    def __init__(self):
        super(Ponger, self).__init__(Sender(EventClient.EXCHANGE), Receiver(EventClient.EXCHANGE), EventFilter('PING'))
        basicConfig(filename='ponger.log', level=DEBUG)
        self.receive_with(self.__pong)
        logging.info('ponger waiting...')

    def __pong(self, ping):
        logging.info('ponger: received %s' % ping)
        self.send(Pong())


class MyService(Service):
    def __init__(self, *args, **kwargs):
        super(MyService, self).__init__(*args, **kwargs)
        self.logger.addHandler(FileHandler('myservice.log'))
        self.logger.setLevel(DEBUG)
        self.ponger = Ponger()

    def run(self):
        while not self.got_sigterm():
            self.logger.info("I'm working..." + str(datetime.now()))
            time.sleep(5)
        self.logger.info("i quit")


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        sys.exit('Syntax: %s COMMAND' % sys.argv[0])

    cmd = sys.argv[1].lower()
    service = MyService('my_service', pid_dir='/tmp')

    if cmd == 'start':
        service.start()
    elif cmd == 'stop':
        service.stop()
    elif cmd == 'status':
        if service.is_running():
            print("Service is running.")
        else:
            print("Service is not running.")
    else:
        sys.exit('Unknown command "%s".' % cmd)
