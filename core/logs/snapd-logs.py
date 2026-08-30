#!/usr/bin/env python3
from pprint import pprint

from landscape.client import snap_http

response = snap_http.logs(names=["landscape-client"], entries=100)
pprint(response.result)
