#!/usr/bin/env python3

from landscape.client import snap_http

# make sure you install the test-snapd-service snap (beta)
#  published by test-snaps-canonical
# restart all services in the test-snapd-service snap
snap_http.restart("test-snapd-service")
