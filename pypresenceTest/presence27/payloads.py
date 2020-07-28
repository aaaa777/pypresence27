import time
import os
from utils import remove_none


class Payload:

    def __init__(self, data, clear_none=True):
        if clear_none:
            data = remove_none(data)
        self.data = data

    def __str__(self):
        return json.dumps(self.data, indent=2)

    @staticmethod
    def time():
        return time.time()

    @classmethod
    def set_activity(cls, pid = os.getpid(), state= None, details = None,
                    start = None, end = None,
                    large_image = None, large_text = None,
                    small_image = None, small_text = None,
                    party_id = None, party_size = None,
                    join = None, spectate = None, match = None, instance = True,
                    activity = True,
                    _rn = True):
        
        if activity == None:
            act_details = None
            clear = True
        else:
            act_details = {
                    "state": state,
                    "details": details,
                    "timestamps": {
                        "start": start,
                        "end": end
                    },
                    "assets": {
                        "large_image": large_image,
                        "large_text": large_text,
                        "small_image": small_image,
                        "small_text": small_text
                    },
                    "party": {
                        "id": party_id,
                        "size": party_size
                    },
                    "secrets": {
                        "join": join,
                        "spectate": spectate,
                        "match": match
                    },
                    "instance": instance
                }
            clear = False

        payload = {
            "cmd": "SET_ACTIVITY",
            "args": {
                "pid": pid,
                "activity": act_details
            },
            "nonce": '{:.20f}'.format(cls.time())
        }
        if _rn:
            clear = _rn
        return cls(payload, clear)