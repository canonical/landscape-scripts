#!/usr/bin/env python3
from pprint import pprint

from landscape.client import snap_http

# Get all configuration for a snap.
response = snap_http.get_conf("system")
pprint(response.result)

# Get specific configuration keys.
response = snap_http.get_conf("system", keys=["experimental", "refresh"])
pprint(response.result)
