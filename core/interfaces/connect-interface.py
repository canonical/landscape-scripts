#!/usr/bin/env python3

from landscape.client import snap_http

snap_http.http.post(
    "/interfaces",
    {
        "action": "connect",
        "slots": [{"slot": "account-control"}],
        "plugs": [{"snap": "landscape-client", "plug": "account-control"}],
    },
)
