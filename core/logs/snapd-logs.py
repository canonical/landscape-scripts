#!/usr/bin/env python3
import json

from landscape.client import snap_http

# get the last 100 log items
response = snap_http.http.get("/logs", query_params={"n": "100"})

# print each log item
json_seq_str = response.result.decode()

log_items = []
while json_seq_str.find("\x1e") != -1:
    start = json_seq_str.find("\x1e")
    end = json_seq_str.find("\x1e", start + 1)

    log_items.append(json.loads(json_seq_str[start+1:end]))

    json_seq_str = json_seq_str[end:]

print(log_items)
