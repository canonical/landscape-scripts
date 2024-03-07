#!/usr/bin/env python3

from landscape.client import snap_http

# make sure you install the test-snapd-service snap (beta)
#  published by test-snaps-canonical
# enable the service inside the test-snapd-service snap
snap_http.start("test-snapd-service.service", enable=True)
