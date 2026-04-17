#!/usr/bin/env python3

from landscape.client import snap_http

snap_http.disconnect_interface(
    in_snap="system",
    in_slot="account-control",
    out_snap="landscape-client",
    out_plug="account-control",
)
