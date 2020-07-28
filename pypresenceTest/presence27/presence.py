import json
import os
import time

from .baseclient import BaseClient
from .payloads import Payload
from .utils import remove_none

class Presence(BaseClient):

    def __init__(self, *args, **kwargs):
        super(Presence, self).__init__(*args, **kwargs)

    def update(self, pid = os.getpid(),
                     state = None, details = None,
                     start = None, end = None,
                     large_image = None, large_text = None,
                     small_image = None, small_text = None,
                     party_id = None, party_size = None,
                     join = None, spectate = None,
                     match = None, instance = True,
                     _donotuse=True):

        if _donotuse is True:
            payload = Payload.set_activity(pid, state, details, start, end, large_image, large_text,
                                           small_image, small_text, party_id, party_size, join, spectate,
                                           match, instance, activity=True)
        else:
            payload = _donotuse
        self.send_data(1, payload)
        return self.read_output()

    def connect(self):
        self.handshake()

    def close(self):
        self.send_data(2, {'v': 1, 'client_id': self.client_id})
        self.sock_writer.close()

    def clear(self, pid = os.getpid()):
        payload = Payload.set_activity(pid, activity=None)
        self.send_data(1, payload)
