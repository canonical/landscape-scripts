#!/usr/bin/env python3
from pprint import pprint

from landscape.client import snap_http

# Get all configuration for a snap.
response = snap_http.get_conf("landscape-client")
pprint(response.result)

# Get specific configuration keys.
response = snap_http.get_conf(
    "landscape-client",
    keys=["account-name", "url", "ping-url"],
)
pprint(response.result)
