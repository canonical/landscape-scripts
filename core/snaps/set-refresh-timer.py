#!/usr/bin/env python3

from landscape.client import snap_http

# set the refresh timer,
# allowing the device to be put in managed mode
snap_http.set_conf(
    "system",
    {
        "refresh.timer": "19:00-07:00",
    },
)
