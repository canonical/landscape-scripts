#!/usr/bin/env python3

from landscape.client import snap_http

# Make sure you install the test-snapd-service snap (beta)
#  published by test-snaps-canonical.
# Restart all services in the test-snapd-service snap.
snap_http.restart("test-snapd-service")
