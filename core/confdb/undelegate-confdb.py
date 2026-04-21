#!/usr/bin/env python3

from landscape.client import snap_http

# Revoke all delegated confdb access from an operator.
snap_http.undelegate_confdb("f22PSauKuNkwQTM9Wz67ZCjNACuSjjhN")

# To revoke access to specific views or authentication methods only,
# pass views and/or authentications.
snap_http.undelegate_confdb(
    "f22PSauKuNkwQTM9Wz67ZCjNACuSjjhN",
    authentications=["store"],
    views=["f22PSauKuNkwQTM9Wz67ZCjNACuSjjhN/network/proxy-admin"],
)
