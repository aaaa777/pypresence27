import inspect
import json
import os
import struct
import sys
import tempfile

from .payloads import Payload
from .exceptions import *

class BaseClient(object):

	def __init__(self, client_id, **kwargs):
		pipe = kwargs.get('pipe', 0)
		client_id = str(client_id)

		#this mod works on windows only(other OS not supported)
		if sys.platform == 'win32':
			self.ipc_path = r'\\.\pipe\discord-ipc-' + str(pipe)

		#connect to named pipe
		self.ipc_io = open(self.ipc_path, 'r+b', 0)
		self.client_id = client_id


	def read_output(self):
		
		data = self.ipc_io.read()

		status_code, length = struct.unpack('<II', data[:8])
		payload = json.loads(data[8:].decode('utf-8'))
		if payload["evt"] == "ERROR":
			print(payload["data"]["message"])
			raise ServerError(payload["data"]["message"])
		return payload

	def handshake(self):

		self.send_data(0, {'v': 1, 'client_id': self.client_id})
		data = self.ipc_io.read()
		code, length = struct.unpack('<ii', data[:8])
		#if self._events_on:
			#self.sock_reader.feed_data = self.on_event

	def send_data(self, op, payload):
		if isinstance(payload, Payload):
			payload = payload.data
		payload = json.dumps(payload)
		self.ipc_io.write(
			struct.pack(
				'<II',
                op,
                len(payload)) +
			payload.encode('utf-8'))


