#!/usr/bin/env python3
from pprint import pprint

from landscape.client import snap_http

response = snap_http.http.get(
    "/connections",
    query_params={"snap": "landscape-client"},
)

pprint(response.result)
