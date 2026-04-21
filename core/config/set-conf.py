#!/usr/bin/env python3

from landscape.client import snap_http

# Set configuration.
snap_http.set_conf(
    "landscape-client",
    {
        "account-name": "standalone",
        "computer-title": "my-device",
        "url": "https://landscape.example.com/message-system",
        "ping-url": "http://landscape.example.com/ping",
    },
)

# Unset a configuration option by passing None.
snap_http.set_conf(
    "landscape-client",
    {
        "some-url": None,
    },
)
