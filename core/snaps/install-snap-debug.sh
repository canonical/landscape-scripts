#!/bin/bash
{
python3 - << EOF

import requests
import socket
import json
import pprint

from urllib3.connection import HTTPConnection
from urllib3.connectionpool import HTTPConnectionPool
from requests.adapters import HTTPAdapter

class SnapdConnection(HTTPConnection):
    def __init__(self):
        super().__init__("localhost")

    def connect(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.connect("/run/snapd.socket")

class SnapdConnectionPool(HTTPConnectionPool):
    def __init__(self):
        super().__init__("localhost")

    def _new_conn(self):
        return SnapdConnection()

class SnapdAdapter(HTTPAdapter):
    def get_connection(self, url, proxies=None):
        return SnapdConnectionPool()


session = requests.Session()
session.mount("http://snapd/", SnapdAdapter())
response = session.post("http://snapd/v2/snaps/nano-strict",
                      data=json.dumps({"action": "install", "channel": "stable"}),
                       )
pprint.pprint(response.json())
EOF
} > /tmp/scriptoutput