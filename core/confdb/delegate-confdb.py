#!/usr/bin/env python3

from landscape.client import snap_http

# Grant an operator the ability to remotely manage confdb views on this device.
snap_http.delegate_confdb(
    "f22PSauKuNkwQTM9Wz67ZCjNACuSjjhN",  # operator account-id
    authentications=["operator-key", "store"],
    views=[
        "f22PSauKuNkwQTM9Wz67ZCjNACuSjjhN/network/proxy-admin",
        "f22PSauKuNkwQTM9Wz67ZCjNACuSjjhN/network/proxy-state",
    ],
)
