#!/usr/bin/env python3 

from landscape.client import snap_http

snap_http.set_conf(
    "system",
    {
        "refresh.hold": "forever",
    },
)