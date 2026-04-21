#!/usr/bin/env python3

from landscape.client import snap_http

# Set values in a confdb view.
snap_http.set_confdb(
    "f22PSauKuNkwQTM9Wz67ZCjNACuSjjhN",    # account-id
    "network",                             # confdb-schema name
    "proxy-admin",                         # view name
    {
        "https.url": "http://proxy.example.com:8080",
        "https.bypass": ["localhost", "192.168.0.0/24"],
        "ftp.url": "ftp://proxy.example.com:8080",
    },
)

# Unset a value by passing None.
snap_http.set_confdb(
    "f22PSauKuNkwQTM9Wz67ZCjNACuSjjhN",
    "network",
    "proxy-admin",
    {"ftp": None},
)
