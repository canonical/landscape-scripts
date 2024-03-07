#!/usr/bin/env python3

from landscape.client import snap_http

snap_http.hold_all(["firefox", "chromium"])
