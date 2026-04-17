#!/usr/bin/env python3

from landscape.client import snap_http

snap_http.set_conf(
    "system",
    {
        "refresh.timer": "19:00-07:00",
    },
)
