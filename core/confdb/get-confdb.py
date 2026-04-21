#!/usr/bin/env python3
import time
from pprint import pprint

from landscape.client import snap_http

# Get all values accessible through a confdb view.
# confdb reads are async so the result must be retrieved by
# polling the returned change.
response = snap_http.get_confdb(
    "f22PSauKuNkwQTM9Wz67ZCjNACuSjjhN",    # account-id
    "network",                             # confdb-schema name
    "proxy-state",                         # view name
)
while True:
    change = snap_http.check_change(response.change)
    if change.result["status"] == "Done":
        pprint(change.result["data"]["values"])
        break
    time.sleep(0.1)

# Get specific keys from a confdb view.
response = snap_http.get_confdb(
    "f22PSauKuNkwQTM9Wz67ZCjNACuSjjhN",
    "network",
    "proxy-state",
    keys=["https"],
)
while True:
    change = snap_http.check_change(response.change)
    if change.result["status"] == "Done":
        pprint(change.result["data"]["values"])
        break
    time.sleep(0.1)
