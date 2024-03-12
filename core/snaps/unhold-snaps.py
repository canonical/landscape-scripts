#!/usr/bin/env python3

from landscape.client import snap_http

snap_http.unhold("firefox")
snap_http.unhold("chromium")
