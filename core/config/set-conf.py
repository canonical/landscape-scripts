#!/usr/bin/env python3

from landscape.client import snap_http

# Set configuration.
snap_http.set_conf(
    "system",  # snap name
    {
        "experimental.confdb": True,
        "experimental.confdb-control": True,
        "experimental.remote-device-management": True,
    },
)

# Unset a configuration option by passing None.
snap_http.set_conf(
    "system",
    {
        "experimental.remote-device-management": None,
    },
)
