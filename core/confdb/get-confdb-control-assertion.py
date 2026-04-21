#!/usr/bin/env python3

from landscape.client import snap_http

# Retrieve the confdb-control assertion, which records which operators have
# been granted delegated access to confdb views on this device.
response = snap_http.get_assertions("confdb-control")
print(response.result.decode())
