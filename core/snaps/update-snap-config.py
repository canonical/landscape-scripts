#!/usr/bin/env python3

from landscape.client import snap_http

# get the system configuration
print(snap_http.get_conf("system"))

# enable some experimental features
snap_http.set_conf(
    "system",
    {
        "experimental.parallel-instances": True,
    },
)
