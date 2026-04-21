#!/bin/bash
{
python3 - << EOF
from pprint import pprint

from landscape.client import snap_http

response = snap_http.install("nano-strict")
pprint(response.result)
EOF
} > /tmp/scriptoutput
