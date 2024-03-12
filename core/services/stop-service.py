#!/usr/bin/env python3

from landscape.client import snap_http

# make sure you install the test-snapd-service snap (beta)
#  published by test-snaps-canonical
# stop all services in the test-snapd-service snap
snap_http.stop("test-snapd-service")
