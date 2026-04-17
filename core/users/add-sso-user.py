#!/usr/bin/env python3

from landscape.client import snap_http

# Add an Ubuntu SSO user to a Core device.
# Use `force_managed` if the device is already managed.
snap_http.add_user(
    "username",
    "username@example.com",
    force_managed=True,
)
